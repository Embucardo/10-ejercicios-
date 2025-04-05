segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
resto1 = segundos - (horas * 3600)
minutos = resto1 // 60
segundos_restantes = resto1 - (minutos * 60)
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)
