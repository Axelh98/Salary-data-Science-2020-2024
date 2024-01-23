import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

archivo = 'data_science_salaries.csv'

salario = pd.read_csv(archivo)


### Analisis por nivel de Experiencia.
print('--- ANALISIS POR NIVEL DE EXPERIENCIA --- ')
experience_lvl_data = salario.groupby('experience_level')['salary'].agg(['max', 'mean', 'count'])
print(experience_lvl_data)

# Ejemplo: Diagrama de barras para el análisis por nivel de experiencia
sns.barplot(x=experience_lvl_data.index, y='mean', data=experience_lvl_data)
plt.title('Salario Promedio por Nivel de Experiencia')
plt.xlabel('Nivel de Experiencia')
plt.ylabel('Salario Promedio')
plt.show()

print(" --- ANALISIS GEOGRAFICO ---")
analisis_geografico = salario.groupby('company_location')['salary'].agg(['max', 'mean', 'count', np.std])
print(analisis_geografico)

print(" --- ANALISIS POR TAMAÑO DE EMPRESA ---")
analisis_tamaño_empresa = salario.groupby('company_size')['salary'].agg(['max', 'mean', 'count', np.std])
print(analisis_tamaño_empresa)

print(" --- ANALISIS POR TIPO DE MODALIDAD ---")
tipo_modalidad = salario.groupby('work_models')['salary'].agg(['max', 'mean', 'count', np.std])
print(tipo_modalidad)

sns.barplot(x=tipo_modalidad.index, y='mean', data=tipo_modalidad)
plt.title('Salario promedio por tipo de modalidad')
plt.xlabel('Modalidad')
plt.ylabel('Salario Promedio')
plt.show()

analisis_temporal = salario.groupby('work_year')['salary'].agg(['max', 'mean', 'count', np.std])
print(" --- ANALISIS DE TENDENCIAS TEMPORALES ---")
print(analisis_temporal)

analisis_titulo_ubicacion = salario.groupby(['job_title', 'company_location'])['salary'].agg(['max', 'mean', 'count', np.std])
print(" --- ANALISIS POR TITULO DE TRABAJO Y UBICACION ---")
print(analisis_titulo_ubicacion)





