#!/usr/bin/env python
#coding=utf-8

import os

def leer_archivo(archivo):

    ref_palabras=[]
    precio_msj=[]
    preguntas=[]
    error_msj=[]

    info={'ref_palabras':ref_palabras,'precio_msj':precio_msj,'preguntas':preguntas, 'error_msj':error_msj}

    with open(archivo) as f:
        for linea in f:
            msj = linea.strip()
            dividir_msj = msj.split()
            if dividir_msj[-1] == '?':
                preguntas.append(msj)
            elif dividir_msj[-1] == 'Credits' and 'is' in msj:
                precio_msj.append(msj)
            elif dividir_msj[-1] in 'IVXLCDM' and 'is' in msj:
                ref_palabras.append(msj)
            else:
                error_msj.append(msj)
    return info