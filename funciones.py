#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Bucles

CodificacionV2 = {'a':'e',
                  'b':'d',
                  'c':'j',
                  'd':'b',
                  'e':'a',
                  'f':'v',
                  'g':'g',
                  'h':'h',
                  'i':'o',
                  'j':'c',
                  'k':'l',
                  'l':'k',
                  'm':'w',
                  'n':'y',
                  'ñ':'ñ',
                  'o':'i',
                  'p':'x',
                  'q':'q',
                  'r':'t',
                  's':'z',
                  't':'r',
                  'u':'u',
                  'v':'f',
                  'w':'m',
                  'x':'p',
                  'y':'n',
                  'z':'s',
                  'á':'é',
                  'é':'á',
                  'í':'ó',
                  'ó':'í',
                  'ú':'ú',
                  '1':'3',
                  '2':'4',
                  '3':'1',
                  '4':'2',
                  '5':'7',
                  '6':'6',
                  '7':'5',
                  '8':'8',
                  '9':'0',
                  '0':'9',
                  ',':',',
                  '.':'.',
                  ';':';',
                  ' ':' ',
                  'A':'E',
                  'B':'D',
                  'C':'J',
                  'D':'B',
                  'E':'A',
                  'F':'V',
                  'G':'G',
                  'H':'H',
                  'I':'O',
                  'J':'C',
                  'K':'L',
                  'L':'K',
                  'M':'W',
                  'N':'Y',
                  'Ñ':'Ñ',
                  'O':'I',
                  'P':'X',
                  'Q':'Q',
                  'R':'T',
                  'S':'Z',
                  'T':'R',
                  'U':'U',
                  'V':'F',
                  'W':'M',
                  'X':'P',
                  'Y':'N',
                  'Z':'S',
                  'Á':'É',
                  'Í':'Ó',
                  'Ú':'Ú'} 


Mensaje = 'Diego Omar Garfagnoli'
Mensaje_Codificado = 'Gike wun duayiz boez. Wejto heri.'
Mensaje_Decodificado = ''
resultado = ''



def codifica_decodifica(Mensaje_Codificado, resultado):
    resultado = ''
    for letra in Mensaje_Codificado:
        resultado = resultado + CodificacionV2[letra]

    return resultado
    


print  codifica_decodifica(Mensaje, resultado)
Mensaje = 'GIKE WUN DUAYIZ BOEZ'
print codifica_decodifica(Mensaje, resultado)




    

    


