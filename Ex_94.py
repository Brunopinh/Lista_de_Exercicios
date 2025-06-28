# 94. Escreva um programa que concatene duas tuplas e remova elementos duplicados.

entrada1 = input("Digite elementos da primeira tupla separados por espaços: ")
tupla1 = tuple(entrada1.split())

entrada2 = input("Digite elementos da segunda tupla separados por espaços: ")
tupla2 = tuple(entrada2.split())

tupla_concatenada = tupla1 + tupla2
tupla_sem_duplicados = tuple(sorted(list(set(tupla_concatenada)))) # Converte para set para remover duplicados, depois lista para ordenar e tupla novamente

print(f"Tupla concatenada e sem duplicados: {tupla_sem_duplicados}")