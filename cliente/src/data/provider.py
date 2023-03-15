##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: provider.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la conexión a la API donde
#   se encuentran los datos del sistema
#
#-------------------------------------------------------------------------
import requests

host = "http://dgraph"
port = "8080"

class Provider:

    @staticmethod
    def execute(query):
        headers = {
            "Content-Type": "application/dql"
        }
        response = requests.post(f"{host}:{port}/query", data=query, headers=headers)
        return response