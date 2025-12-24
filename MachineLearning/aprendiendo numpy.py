import numpy as np
"""Crea un array que contenga los números del 0 al 19 (inclusive)."""
array=np.arange(0,20,1)
print(array)
"""Cámbiale la forma (reshape) para que sea una matriz de 4 filas y 5 columnas."""
array2=array.reshape(4,5)
print(f"Matriz:\n{array2}")
"""Calcula el promedio de cada columna (deberías obtener 5 números como resultado)."""
for i in range(0,5):
    promedio=array2[:,i].mean()
    print(f'Promedio de la columna {i+1} es {promedio}')
#3. Promedio (La forma correcta)
# axis=0 significa: "Aplasta las filas y opera hacia abajo (por columna). axis=1 opera por filas"
promedios = array2.mean(axis=0)

print(f"Promedios por columna: {promedios}\n")
#🏋️‍♂️ Micro-Desafío Nivel 2: "Limpieza de Sensores"
"""Genera un array llamado temperaturas con 15 números enteros aleatorios entre -10 y 50.
Pista: Usa np.random.randint(min, max, cantidad)."""
temperaturas=np.random.randint(-10,50,15)
print(f'\nTempertauras: \n {temperaturas}')
"""Extrae e imprime en un nuevo array las "Alertas de Calor": temperaturas mayores a 30."""
alertas_de_calor=temperaturas[temperaturas>30]
print(f'\nAlertas de calor: \n{alertas_de_calor}')
"""En el array original temperaturas, reemplaza cualquier valor negativo (menor a 0) con el valor 0."""
temperaturas[temperaturas<0]=0
print(f'\nTempertauras sin bajo cero: \n{temperaturas}')
#🥊 Desafío Final NumPy: "El Normalizador"
"""Genera la matriz datos con notas aleatorias (0-100) de forma (3, 4)."""
datos=np.random.randint(0,100,12).reshape(3,4)
print(f'\nNotas: \n{datos}')
"""Calcula el promedio de cada materia (tendrás un vector de 4 promedios). Recuerda usar axis."""
prom=datos.mean(axis=0)
print(f'\nPromedio x columna: \n{prom}')
"""Broadcasting: Resta el promedio a la matriz original para "centrar" los datos. 
(Esto nos dice cuánto se desvía cada alumno del promedio). Llama a esto datos_centrados."""
datos_centrados=datos - prom
print(f'\n Datos centrados: \n{datos_centrados}')

"""Argmax: Encuentra en qué materia obtuvo la nota más alta el Estudiante 2 (índice 1)."""
mejor_promedio=np.argmax(datos[1]) #aisla la fila del estudiante 2, osea la fila index 1
print(f"La mejor materia del Estudiante 2 es la índice: {mejor_promedio}")