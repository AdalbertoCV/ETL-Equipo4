##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: loader.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define el punto de ejecución del Microservicio
#
#-------------------------------------------------------------------------
from src.transformers.csv_transformer import CSVTransformer
from src.transformers.xml_transformer import XMLTransformer
from src.transformers.htm_transformer import HTMTransformer
from src.transformers.txt_transformer import TXTTransformer
from src.helpers.provider import Provider
from src.helpers.queries import Queries
from src.helpers.processor import Processor
import luigi, json, time


class Loader(luigi.Task):

    def requires(self):
        return CSVTransformer(), XMLTransformer(), HTMTransformer(), TXTTransformer()

    def run(self):
        # creates the schema
        Provider.perform_alter(Queries.get_schema())

        files = []
        for file in self.input():
            with file.open('r') as json_file:
                print(f"processing file {json_file.name}...")
                files.append(json_file.name)
                products = json.load(json_file)
                for p in products:

                    if not p["description"]:
                        continue
                    else:
                        p['description'] = p['description'].replace("\"", "'")

                    # location
                    loc_query_res = Provider.perform_query(Queries.query_name(p["country"]))
                    location = Processor.extract_query_uid(loc_query_res)
                    if not location:
                        mutation_res = Provider.perform_mutate(Queries.create_location(p["country"]))
                        location = Processor.extract_created_uid(mutation_res, "location")
                    
                    # provider
                    prov_query_res = Provider.perform_query(Queries.query_pid(p["provider"]))
                    provider = Processor.extract_query_uid(prov_query_res)
                    if not provider:
                        mutation_res = Provider.perform_mutate(Queries.create_provider(p['provider'], location))
                        provider = Processor.extract_created_uid(mutation_res, "provider")

                    # location and provider
                    loc_pro_query_res = Provider.perform_query(Queries.query_belongs(provider))
                    relations = Processor.extract_relation_uids(loc_pro_query_res, "belongs")
                    if not location in relations:
                        Provider.perform_mutate(Queries.add_belongs_relation(provider, location))

                    # order
                    ord_query_res = Provider.perform_query(Queries.query_invoice(p["invoice"]))
                    order = Processor.extract_query_uid(ord_query_res)
                    if not order:
                        date = Processor.compute_random_date()
                        mutation_res = Provider.perform_mutate(Queries.create_order(p["invoice"], p["quantity"], p["total"], date))
                        order = Processor.extract_created_uid(mutation_res, "order")
                    
                    # product
                    prod_query_res = Provider.perform_query(Queries.query_desc(p["description"]))
                    product = Processor.extract_query_uid(prod_query_res)
                    if not product:
                        mutation_res = Provider.perform_mutate(Queries.create_product(p["description"], p["price"]))
                        product = Processor.extract_created_uid(mutation_res, "product")

                    # product and order
                    prod_ord_query_res = Provider.perform_query(Queries.query_boughts(product))
                    relations = Processor.extract_relation_uids(prod_ord_query_res, "bought")
                    if not order in relations:
                        Provider.perform_mutate(Queries.add_bought_relation(product, order))

                    # product and provider
                    prod_prov_query_res = Provider.perform_query(Queries.query_sold(product))
                    relations = Processor.extract_relation_uids(prod_prov_query_res, "sold")
                    if not provider in relations:
                        Provider.perform_mutate(Queries.add_sold_relation(product, provider))
            print(f"...file {json_file.name} processed\n")

        with self.output().open('w') as f:
            for name in files:
                f.write('...file {name} processed\n'.format(name=name))

    def output(self):
        return luigi.LocalTarget('result.txt')


if __name__ == '__main__':
    retry = True
    while retry:
        retry = not luigi.run(main_task_cls=Loader, local_scheduler=True, cmdline_args=["--scheduler-retry-count=5", "--scheduler-retry-delay=3", "--scheduler-worker-disconnect-delay=3", "--no-lock"])
        time.sleep(10)
