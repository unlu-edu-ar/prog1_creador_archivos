# • Nro. de cuenta (n_cuenta:entero)
# • Movimiento(codi:entero)
# • Importe (importe:real)
from random import choice , randrange
import csv
contador = 0 
cuentas = 300
cantidad_movimientos_cuenta = 20
codi = [1,2]
reporte=[]
for cuenta in range(100,cuentas+101):
    for i in range(randrange(0,cantidad_movimientos_cuenta)):
        importe = float(randrange(10,400) * 100)
        reporte.append([cuenta,choice(codi),importe])
with open('archivos/movimientos.txt', 'w', ) as f:
    writer = csv.writer(f)
    for reg in reporte:
        writer.writerow(reg)