##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: zip_decompressor.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define un procesador de datos que se encarga de leer y
#   descomprimir el contenido de un archivo ZIP
#-------------------------------------------------------------------------
import luigi, os
from os.path import isfile, join
import zipfile, time

class ZIPReader(luigi.Task):

    def run(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        assets_dir = join(project_dir, "assets")
        files = [f for f in os.listdir(assets_dir) if isfile(join(assets_dir, f))]
        zip_files = [f for f in files if f.endswith(".zip")]
        for zip_file in zip_files:
            file = luigi.LocalTarget(join(assets_dir, zip_file))
            zfile = zipfile.ZipFile(file.path)
            for name in zfile.namelist():
                zfile.extract(name, assets_dir)
                time.sleep(5)
            zfile.close()