import fastf1

# 1. Habilitar el caché (creará una carpeta "cache" donde esté tu script)
# Esto es vital para que no tarde años descargando datos cada vez.
fastf1.Cache.enable_cache('cache') 

print("Descargando datos de la sesión... (esto puede tardar un poco la primera vez)")

# 2. Cargar una sesión (Ej: Clasificación de Bahrein 2023)
session = fastf1.get_session(2023, 'Bahrain', 'Q')
session.load()

# 3. Obtener resultados
f1_results = session.results

# 4. MOSTRAR DATOS (El paso que faltaba)
print("\n--- Top 5 Pilotos en la Clasificación ---")
# Mostramos las columnas de Abreviatura, Equipo y Tiempo de vuelta
print(f1_results[['Abbreviation', 'TeamName', 'Q3']].head(5))

print("\n--- Vuelta más rápida ---")
fastest_lap = session.laps.pick_fastest()
print(f"El piloto más rápido fue: {fastest_lap['Driver']}")
print(f"Tiempo: {fastest_lap['LapTime']}")