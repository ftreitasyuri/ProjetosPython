medida = float(input('Uma distancia em metros: '))
cm = medida * 100 # centimentos
mm = medida * 1000 # milimetros
dm = medida * 10000 # decimetro
m =  medida # metros
dam = medida * 100000 # decametro
hm = medida * 1000000# Hequitometro
km = medida * 10000000# kilometro
print('Aqui estão os valores correspondentes ao número digitado.\n '.format(medida, cm, mm))
print('metros corresponde a {}m, decametro é {}dam hequitometro é {}hm e kilometro é {}km'.format(m, dam, hm, km))
