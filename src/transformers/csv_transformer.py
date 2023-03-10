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
#   y formatear el contenido de un archivo CSV
#-------------------------------------------------------------------------
from src.extractors.csv_extractor import CSVExtractor
from os.path import join
import luigi, os, csv, json, re

class CSVTransformer(luigi.Task):

    def requires(self):
        return CSVExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as csv_file:
                csv_reader = csv.reader(csv_file)
                header = []
                regex = re.compile('[^a-zA-Z]')
                header = [regex.sub('', column) for column in next(csv_reader)]
                for row in csv_reader:
                    entry = dict(zip(header, row))
                    
                    if not entry["productdesc"]:
                        continue

                    result.append(
                        {
                            "description": entry["productdesc"],
                            "quantity": entry["qty"],
                            "price": entry["rawprice"],
                            "total": float(entry["qty"]) * float(entry["rawprice"]),
                            "invoice": entry["inv"],
                            "provider": entry["provider"],
                            "country": entry["countryname"]
                        }
                    )
        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "csv.json"))