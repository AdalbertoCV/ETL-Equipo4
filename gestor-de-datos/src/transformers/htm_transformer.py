##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: csv_transformer.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define un procesador de datos que se encarga de transformar
#   y formatear el contenido de un archivo HTM
#-------------------------------------------------------------------------
from src.extractors.htm_extractor import HTMExtractor
from bs4 import BeautifulSoup
from os.path import join
import luigi, os, json

class HTMTransformer(luigi.Task):

    def requires(self):
        return HTMExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as htm_file:
                soup = BeautifulSoup(htm_file)
                table = soup.find("table", attrs={"class":"table-bordered"})
                headers = [th.get_text() for th in table.find("tr").find_all("th")]
                for row in table.find_all("tr")[1:]:
                    entry = dict(zip(headers, (td.get_text() for td in row.find_all("td"))))
                    result.append(
                        {
                            "description": entry["description_product"],
                            "quantity": entry["Qty"],
                            "price": entry["product_price"],
                            "total": float(entry["Qty"]) * float(entry["product_price"]),
                            "invoice": entry["order_invoice"],
                            "provider": entry["id_provider"],
                            "country": entry["country_location"]
                        }
                    )
        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "htm.json"))