##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: main.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define el punto de ejecución del Microservicio
#
#-------------------------------------------------------------------------
from src.application import app

if __name__ == '__main__':
    app.run_server("0.0.0.0", debug=True, port=5000)