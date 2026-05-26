def calcular_y_clasificar_jornada(matriz_horas, umbral=40):
    """
    Módulo que calcula la suma total de horas semanales por recurso
    y clasifica su jornada según el umbral establecido.
    """
    resultados = []
    
    for fila in matriz_horas:
        nombre = fila[0]
        # Sumamos solo los valores numéricos (desde la posición 1 a la 5, Lunes a Viernes)
        total_horas = sum(fila[1:])
        
        # Lógica de negocio para la clasificación
        if total_horas > umbral:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        resultados.append({
            "nombre": nombre,
            "total_horas": total_horas,
            "clasificacion": clasificacion
        })
        
    return resultados

# --- REQUISITOS DE DESARROLLO ---

# 1. Creación de la matriz con 4 recursos y sus horas diarias (Lu, Ma, Mi, Ju, Vi)
matriz_recursos = [
    ["Ana Gómez", 8, 8, 9, 8, 8],       # Total: 41 horas (Sobretiempo)
    ["Carlos Pérez", 8, 7, 8, 6, 8],     # Total: 37 horas (Horario Estándar)
    ["María López", 9, 10, 8, 9, 9],    # Total: 45 horas (Sobretiempo)
    ["Luis Rodríguez", 8, 8, 8, 8, 8]   # Total: 40 horas (Horario Estándar)
]

# 2. Llamada al módulo de cálculo
reporte_semanal = calcular_y_clasificar_jornada(matriz_recursos)

# 3. Salida de datos formateada
print(f"{'RECURSO':<18} | {'HORAS TOTALES':<15} | {'ESTADO DE JORNADA'}")
print("-" * 55)
for registro in reporte_semanal:
    print(f"{registro['nombre']:<18} | {registro['total_horas']:<15} | {registro['clasificacion']}")