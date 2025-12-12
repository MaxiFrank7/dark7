import fastf1
import matplotlib.pyplot as plt

import fastf1.plotting

import os  # <--- Necesitamos importar esto para manejar carpetas

# Definir el nombre de la carpeta
cache_dir = 'cache'

# Si la carpeta no existe, la creamos
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# Ahora sí habilitamos el caché sin miedo a errores
fastf1.Cache.enable_cache(cache_dir)

print("Descargando datos de la sesión... (esto puede tardar un poco la primera vez)")

# 3. Obtener resultados
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')

# load a session and its telemetry data
session = fastf1.get_session(2024, 'Baku', 'Q')
session.load()

ver_lap = session.laps.pick_drivers('VER').pick_fastest()
col_lap = session.laps.pick_drivers('COL').pick_fastest()

ver_tel = ver_lap.get_car_data().add_distance()
col_tel = col_lap.get_car_data().add_distance()

rbr_color = fastf1.plotting.get_team_color(ver_lap['Team'], session=session)
will_color = fastf1.plotting.get_team_color(col_lap['Team'], session=session)

fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color=rbr_color, label='VER')
ax.plot(col_tel['Distance'], col_tel['Speed'], color=will_color, label='COL')

ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")
plt.show()