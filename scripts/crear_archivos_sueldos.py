# • Código de sucursal (cod_suc: entero)
# • Código de empleado (cod_emp: entero)
# • Sueldo mensual(sueldo:real)
# import random
from random import sample , randrange
import csv
empleados_agregados =0 
sucursales = 40
empleados_x_suxcursal = 6

codigos_empleados = [a for a in range(10,empleados_x_suxcursal*sucursales)]
reporte = []
for sucursales in range(1,sucursales+1):
    if len(codigos_empleados ) >0 :
        seleccion_empleados =  sample(codigos_empleados,k=randrange(2,empleados_x_suxcursal))
        for empleado in seleccion_empleados:
            empleados_agregados +=1
            sueldo = float(randrange(50,650) * 1000)
            reporte.append([sucursales,empleado,sueldo])
            print(sucursales,empleado,sueldo)
            codigos_empleados.pop(codigos_empleados.index(empleado)) 

print(f"Se crearon {empleados_agregados}")
with open('archivos/sueldos.txt', 'w', ) as f:
    writer = csv.writer(f)
    for reg in reporte:
        writer.writerow(reg)
