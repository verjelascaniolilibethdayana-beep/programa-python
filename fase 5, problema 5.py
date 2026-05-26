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
        clasificacion = "Horas normales"
    
    return nombre, total_horas, clasificacion

for recurso in recursos:
    nombre, total_horas, clasificacion = calcular_jornada(recurso)
    
    print(f"Recursos: {nombre}")
    print(f"Total de horas: {total_horas}")
    print(f"Clasificación: {clasificacion}")
    print("---------------------------------")