""""Vamos a crear tu primer DataFrame y extraer información.

Crea un DataFrame manualmente (usando un diccionario) con datos de 4 empleados:
Columnas: Nombre, Salario, Departamento.

Inventa los datos.
Aumenta el sueldo de todos un 10% (Pandas permite operaciones vectorizadas igual que NumPy: df['columna'] * 1.10).
Imprime solo la columna Nombre y la columna Salario (ya actualizado).

Usa .describe() para mostrarme las estadísticas rápidas del nuevo salario."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

empleados_columnas = {
    "Nombre": ["Ana García", "Carlos Ruiz", "Elena Torres", "David Menta"],
    "Salario": [3500, 2800, 4200, 3100],
    "Departamento": ["IT", "Recursos Humanos", "Gerencia", "Marketing"]
}

datos_empleados=pd.DataFrame(empleados_columnas)
print(datos_empleados)

datos_empleados['Salario']=datos_empleados['Salario']*1.1
print(datos_empleados)

subset = datos_empleados[['Nombre', 'Salario']]
print(subset)

print(datos_empleados['Salario'].describe())

"""Filtro: Crea un nuevo DataFrame llamado seniors que contenga solo a los empleados con más de 5 años de experiencia. Imprímelo.
Agrupación: Calcula el Salario Promedio por Departamento. (Deberías ver que IT gana más).
Ordenamiento (Bonus): Muestra los empleados ordenados por Salario de mayor a menor.
Pista: Busca sort_values en Google o la documentación, o intenta adivinar la sintaxis (es muy intuitiva)."""
data = {
    'Nombre': ['Ana', 'Luis', 'Juan', 'Maria', 'Pedro', 'Laura'],
    'Departamento': ['Ventas', 'IT', 'Ventas', 'IT', 'Marketing', 'Ventas'],
    'Salario': [2500, 4500, 2700, 4800, 3200, 2600],
    'Años_Experiencia': [2, 8, 3, 9, 4, 2]
}
df_empresa = pd.DataFrame(data)

seniors=df_empresa[df_empresa['Años_Experiencia']>=5]
print(seniors)
promedios=df_empresa.groupby('Departamento')['Salario'].mean()
print(promedios)
print(df_empresa.sort_values('Salario',ascending=False))

"""Crea un Gráfico de Barras que muestre:

Eje X: Los Nombres de los empleados.
Eje Y: Sus Salarios.
Pista: Usa plt.bar(x, y).

Añade un título al gráfico: "Salarios del Equipo".
Añade etiquetas a los ejes X e Y ("Empleado" y "Euros")."""
plt.bar(df_empresa['Nombre'],df_empresa['Salario'])
plt.title('Salarios del Equipo')
plt.xlabel('Empleado')
plt.ylabel('Dolares')
plt.show()

