#!/usr/bin/env python3
#coding=utf-8

import sys
import os

from mercader import Mercader
from leer_archivo import leer_archivo

RESPUESTA_POR_DEFECTO = "I have no idea what you are talking about"

def aprender_y_responder(archivo_entrada):
    info = leer_archivo(archivo_entrada)
    error_msjs = info['error_msj']

    if len(info['ref_palabras']) > 0:
        mercader = Mercader(RESPUESTA_POR_DEFECTO)
        resultado = mercader.aprender_conocimiento(info['ref_palabras'], info['precio_msj'])
        
        if resultado:
            error_msjs.extend(resultado)

        resultado = mercader.responder_preguntas(info['preguntas'])
        if resultado:
            print("\n".join(resultado))
        if error_msjs:
            print("\n".join(error_msjs))
    else:
        print("no ref words found")

if __name__ == '__main__':
    archivo_entrada = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    if not os.path.isfile(archivo_entrada):
        print("Can't find the input file: " + archivo_entrada)
        exit(1)    

    with open('output.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        aprender_y_responder(archivo_entrada)