# contagem regressiva usando FOR

contador = 0
somador = 0
from time import sleep
for cont in range(1, 10):
    contador += 1
    somador += contador
    sleep(1)
    print(cont)
print('BUMMM!!! 💣 💢 💣 💢')
print (contador)
print (somador)
