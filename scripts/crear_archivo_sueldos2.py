# • Código de sucursal (cod_suc:entero)
# • Código de departamento  (cod_dpto:entero)
# • Código de empleado  (cod_emp:entero)
# • Sueldo mensual (sueldo:real)

from random import sample , randrange
import csv
empleados_agregados = 0 
sucursales = 40
departamentos_sucursales = 10
empleados_x_suxcursal = 20
 
codigos_empleados = [a for a in range(10,empleados_x_suxcursal*sucursales*departamentos_sucursales)]
reporte = []
for sucursales in range(1,sucursales+1):
    for dpto in range(1,randrange(1,departamentos_sucursales)):
        if len(codigos_empleados ) >0 :
            seleccion_empleados =  sample(codigos_empleados,k=randrange(2,empleados_x_suxcursal))
            for empleado in seleccion_empleados:
                empleados_agregados +=1
                sueldo = float(randrange(50,350) * 1000)
                reporte.append([sucursales,100+dpto,empleado,sueldo])
                print(sucursales,100+dpto,empleado,sueldo)
                codigos_empleados.pop(codigos_empleados.index(empleado)) 

print(f"Se crearon {empleados_agregados}")
with open('archivos/sueldos2.txt', 'w', ) as f:
    writer = csv.writer(f)
    for reg in reporte:
        writer.writerow(reg)
