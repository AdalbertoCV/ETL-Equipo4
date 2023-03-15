##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: htm_extractor.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define un procesador de datos que se encarga de extraer
#   el contenido de un archivo HTM
#-------------------------------------------------------------------------
import luigi, os
from os.path import isfile, join
from src.readers.zip_reader import ZIPReader

class HTMExtractor(luigi.Task):

    def requires(self):
        return ZIPReader()

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        assets_dir = join(project_dir, "assets")
        files = [f for f in os.listdir(assets_dir) if isfile(join(assets_dir, f))]
        htm_files = [f for f in files if f.endswith(".htm")]
        targets = []
        for file in htm_files:
            targets.append(luigi.LocalTarget(join(assets_dir, file)))
        return targets