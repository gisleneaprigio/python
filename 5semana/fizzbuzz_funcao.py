# -*- coding:utf-8 -*-

def executaFizzBuzz(numero):
   
    if numero % 5 == 0 and numero % 3 == 0:
        return 'fizz-buzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'
    else:
        return numero
