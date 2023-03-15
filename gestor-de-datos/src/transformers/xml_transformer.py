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
#   y formatear el contenido de un archivo XML
#-------------------------------------------------------------------------
from src.extractors.xml_extractor import XMLExtractor
import xml.etree.ElementTree as ET
from os.path import join
import luigi, os, json

class XMLTransformer(luigi.Task):

    def requires(self):
        return XMLExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                for row in root.findall('row'):
                    result.append(
                        {
                            "description": row.find('desc').text,
                            "quantity": row.find('product_qty').text,
                            "price": row.find('current_price').text,
                            "total": float(row.find('product_qty').text) * float(row.find('current_price').text),
                            "invoice": row.find('order_inv').text,
                            "provider": row.find('provider_identifier').text,
                            "country": row.find('country_loc').text
                        }
                    )
        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "xml.json"))