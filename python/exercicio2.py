import random
import os
import time


def calculate(x, y):
    return x - y


# funçao
os.system('cls')
print('Olá, irei sortear o seu dinheiro')
time.sleep(1.8)

pergun = True
while pergun == True:
    x = random.randint(300, 900)
    print(x, "reais")
    pre = int(input('Quer sortear denovo?\n[1]Sim\n[2]Nao\nR:'))
    if pre == 1:
        os.system('cls')
        time.sleep(1)
    if pre == 2:
        pergun = False
        time.sleep(1)
time.sleep(4)
print('Bem vindo a loja Snaker BR')
time.sleep(2)
print('Temos snaker de varias marcas, escolha uma')
marcas = int(input('[1]Adidas, [2]Nike, [3]Puma\nR:'))
####
if marcas == 1:
    os.system('cls')
    print('Você está na snakers adidas')
    print('Seu saldo atual é {} Reais'.format(x))
    time.sleep(1)
    print('[1]TÊNIS ULTRABOOST 22 apenas R$899,99\n[2]TÊNIS FORUM LOW apenas R$599,99\n[3]TÊNIS OZNOVA apenas $299,99')
    time.sleep(1)
    tr1 = int(input('\n\n[1]Escolher um tenis [2] Trocar Marca'))
    if tr1 == 1:
        escl = int(input('Escolha um tenis'))
        if escl == 1:
            if x >= 899.99:
                y = 899.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
        if escl == 2:
            if x >= 599.99:
                y = 599.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
        if escl == 1:
            if x >= 299.99:
                y = 299.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
    if tr1 == 2:
        marcas = int(input('[2]Nike, [3]Puma'))
        os.system('cls')
####
if marcas == 2:
    print('Você escolheu nike')
    time.sleep(1)
    print('Seu saldo atual é {} Reais'.format(x))
    time.sleep(1)
    print('[1]Tênis Nike Air Force 1 "07 Masculino apenas 799,99\n[2]Tênis Nike Revolution 6 Next Nature Masculino apenas 319,99\n[3]Tênis Air Jordan 1 Low Masculino apenas $549,99')
    time.sleep(1)
    tr1 = int(input('\n\n[1]Escolher um tenis [2] Trocar Marca'))
    if tr1 == 1:
        escl = int(input('Escolha um tenis'))
        if escl == 1:
            if x >= 799.99:
                y = 799.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
        if escl == 2:
            if x >= 319.99:
                y = 319.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
        if escl == 1:
            if x >= 549.99:
                y = 549.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
    if tr1 == 2:
        marcas = int(input('[1]Adidas, [3]Puma'))
####
if marcas == 3:
    print('Você escolheu puma')
    time.sleep(1)
    print('Seu saldo atual é {} Reais'.format(x))
    time.sleep(1)
    print('[1]TÊNIS RS-X EFEKT REFLECTIVE apenas R$899,90\n[2]TÊNIS CAMOWAVE SUEDE apenas 699,90\n[3]TÊNIS CARINA FEMININO apenas $349,99')
    time.sleep(1)
    tr1 = int(input('\n\n[1]Escolher um tenis [2] Trocar Marca'))
    if tr1 == 1:
        escl = int(input('Escolha um tenis'))
        if escl == 1:
            if x >= 899.90:
                y = 899.90
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
        if escl == 2:
            if x >= 699.90:
                y = 699.90
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
        if escl == 1:
            if x >= 349.99:
                y = 349.99
                print('Voce recebeu {} de troco'.format(calculate(x, y)))
            else:
                print('\nVocê nao tem dinheiro suficiente')
                time.sleep(2.6)
                marcas = int(input('[2]Nike, [3]Puma'))
                os.system('cls')
    if tr1 == 2:
        marcas = int(input('[1]Adidas, [2]Nike'))
