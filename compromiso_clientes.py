# ============================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN
# FASE 5 – EVALUACIÓN FINAL POA
#
# PROGRAMA:
# Sistema de clasificación del nivel de compromiso
# de sesiones de clientes mediante análisis de datos
# utilizando programación estructurada en Python



# MATRIZ DE DATOS
sesiones = [

    ["C001", 250, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 4]

]


# FUNCIÓN PARA CLASIFICAR EL COMPROMISO
def clasificar_compromiso(duracion, clics):

    # Clasificación ALTA
    if duracion > 180 and clics > 8:
        return "ALTO"

    # Clasificación BAJA
    elif duracion < 60 or clics < 3:
        return "BAJO"

    # Clasificación MEDIA
    else:
        return "MEDIO"


# ENCABEZADO
print("========================================================")
print("   SISTEMA DE CLASIFICACIÓN DE COMPROMISO DE CLIENTES")
print("========================================================")


# RECORRER MATRIZ
for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("\nCliente:", id_cliente)
    print("Duración de la sesión:", duracion, "segundos")
    print("Cantidad de clics:", clics)
    print("Nivel de compromiso:", clasificacion)
    print("---------------------------------------------------")


# FINAL DEL PROGRAMA
print("\nProceso finalizado correctamente.")