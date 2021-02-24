#!/usr/bin/env python
# -*- coding: utf-8 -*

""" Criado por: Thais Andrade
    Data de Criação: 21/02/2021
    Referencias: 
        https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
        https://stackoverflow.com/questions/3391076/repeat-string-to-certain-length/3391106
        https://www.geeksforgeeks.org/vigenere-cipher/
"""


#funcao que repete a chave ate que ela fique do tamanho da mensagem a ser cifrada.
def gera_chave(chave, tamanho):
    upd_chave = chave * (tamanho//len(chave) + 1)
    nova_chave = upd_chave[:tamanho]
    return nova_chave


#funcao recebe uma lista com os caracteres da mensagem e a chave ja no tamanho correto e retorna a mensagem cifrada em codigo ascii.
def cifra_msg(mensagem, chave):
    msg_cifrada = []
    for item in range(len(mensagem)):
        cifra = (ord(mensagem[item]) + ord(chave[item])) %127 #127 é o tamanho da tabela ascii completa
        msg_cifrada.append(cifra)
    return msg_cifrada


#funcao recebe uma lista contendo os caracteres da mensagem cifrados e retorna uma lista com caracteres decifrados
def decifra_msg(msg_cifrada, chave):
    msg_decifrada = []
    for item in range(len(msg_cifrada)):
        decifra = (msg_cifrada[item] - ord(chave[item]) + 127) %127
        msg_decifrada.append(chr(decifra))     
    return msg_decifrada


def main():
    #mensagem        = 'eu amo batata, 100!' #mensagem a ser cifrada
    mensagem = input('Digite a mensagem a ser cifrada: ')
    chave           = 'seginfo' #chave de segurança 
    caracteres_msg  = list(mensagem)
    
    chave_ajustada  = gera_chave(chave, len(caracteres_msg)) 
    msg_cifrada     = cifra_msg(caracteres_msg, chave_ajustada)
    msg_decifrada   = decifra_msg(msg_cifrada, chave_ajustada) 

    msg_ascii = list(map(chr, msg_cifrada)) 
    str_cifrada = ""
    print("Mensagem cifrada: " + str_cifrada.join(msg_ascii))

    str_decifrada = ""
    print("Mensagem decifrada: " + str_decifrada.join(msg_decifrada))

if __name__ == '__main__':
    main()
