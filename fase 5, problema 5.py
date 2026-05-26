recursos = [
    ["Carlos Pérez", 8, 9, 8, 10, 9],
    ["Ana Gómez", 7, 8, 7, 8, 7],
    ["Luis García", 9, 10, 9, 8, 10],
    ["María López", 6, 7, 8, 7, 6]
]
def calcular_jornada(recursos):
    nombre = recursos[0]
    horas = recursos[1:]
    
    total_horas = sum(horas)
    
    if total_horas >= 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
    
    return nombre, total_horas, clasificacion
reporte_semanal = []

for recurso in recursos:
    nombre, total_horas, clasificacion = calcular_jornada(recurso)
    reporte_semanal.append({
        "nombre": nombre,
        "total_horas": total_horas,
        "clasificacion": clasificacion
    })
print(f"{'RECURSO':<18} | {'HORAS TOTALES':<15} | {'ESTADO DE JORNADA'}")
print("-" * 55)
for registro in reporte_semanal:
 print(f"{registro['nombre']:<18} | {registro['total_horas']:<15} | {registro['clasificacion']}")