#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Bucles
a = 0
edad = 0
while a < 20:
    edad = edad + 1
    print 'Hola, tu edad: ' + str(edad)
    if edad == 15:
        break
    a = a + 1



lista = ['Elemento1', 'Elemento2','Elemento3']

for cosa in lista:
    print cosa

for letra in 'Esta es una cadena':
    if letra != 'a':
        print letra
    else: print 'XXX'

Codificacion = {'a':'z',
                'b':'y',
                'c':'x',
                'd':'d',
                'e':'o',
                'f':'w',
                'g':'v',
                'h':'u',
                'i':'t',
                'j':'j',
                'k':'k',
                'l':'m',
                'm':'l',
                'n':'n',
                'ñ':'ñ',
                'o':'e',
                'p':'q',
                'q':'p',
                'r':'r',
                's':'s',
                't':'i',
                'u':'h',
                'v':'g',
                'w':'f',
                'x':'c',
                'y':'b',
                'z':'a',
                '1':'4',
                '2':'3',
                '3':'2',
                '4':'1',
                '5':'5',
                '6':'6',
                '7':'9',
                '8':'7',
                '9':'8',
                '0':'0',
                ',':',',
                '.':'.',
                ';':';',
                ' ':' ',
                'A':'Z',
                'B':'Y',
                'C':'X',
                'D':'D',
                'E':'O',
                'F':'W',
                'G':'V',
                'H':'U',
                'I':'T',
                'J':'J',
                'K':'K',
                'L':'M',
                'M':'L',
                'N':'N',
                'Ñ':'Ñ',
                'O':'E',
                'P':'Q',
                'Q':'P',
                'R':'R',
                'S':'S',
                'T':'I',
                'U':'H',
                'V':'G',
                'W':'F',
                'X':'C',
                'Y':'B',
                'Z':'A'}

CodificacionV2 = {'a':'e',
                  'b':'d',
                  'c':'j',
                  'd':'b',
                  'e':'a',
                  'f':'v',
                  'g':'h',
                  'h':'g',
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
                  'G':'H',
                  'H':'G',
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


Mensaje = 'Hola muy buenos dias. Macri gato.'
Mensaje_Codificado = 'Gike wun duayiz boez. Wejto heri.'
Mensaje_Decodificado = ''
resultado = [' ']



def codifica_decodifica(Mensaje_Codificado, resultado):
    
    for letra in Mensaje_Codificado:
        resultado[0] = resultado[0] + CodificacionV2[letra]

    print resultado
    


codifica_decodifica(Mensaje_Codificado, resultado)





    

    


