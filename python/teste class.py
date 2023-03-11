import os
os.system('cls')
marca = input('digite uma marca de carro')
modelo = input('digite um modelo de carro')
ano = input('digite um ano de carro')
motor = input('digite o motor')

class carro:
    def __init__(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor

carro1 = carro(marca, modelo, ano, motor)
print(carro1.marca, carro1.modelo, carro1.ano, carro1.motor)
input('')