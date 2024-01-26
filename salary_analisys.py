import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ESTE ES EL DATASET A TRABAJAR
archivo = 'data_science_salaries.csv'
salario = pd.read_csv(archivo)


# ---> Analisis por nivel de Experiencia.
print('--- ANALISIS POR NIVEL DE EXPERIENCIA --- ')
experience_lvl_data = salario.groupby('experience_level')['salary'].agg(['max', 'mean', 'count'])
print(experience_lvl_data)

<<<<<<< HEAD


# ----> GRAFICO DE BARRAS PARA EL ANALISIS POR NIVEL DE EXPERIENCIA
# ----> GRAFICO DE BARRAS PARA EL ANALISIS POR NIVEL DE EXPERIENCIA
# ----> GRAFICO DE BARRAS PARA EL ANALISIS POR NIVEL DE EXPERIENCIA
ax = sns.barplot(x=experience_lvl_data.index, y='mean', data=experience_lvl_data)
plt.title('Salario Promedio por Nivel de Experiencia')
plt.xlabel('Nivel de Experiencia')
plt.ylabel('Salario Promedio')

    # ---> ESTE BUCLE AGREGA ETIQUETAS A LAS BARRAS
for i, v in enumerate(experience_lvl_data['mean']):
    ax.text(i, v + 1000, f'{v:.2f}', ha='center', va='bottom', fontsize=8)

plt.show()

# ---> ANALISIS GEOGRAFICO
=======
# Ejemplo: Diagrama de barras para el análisis por nivel de experiencia
sns.barplot(x=experience_lvl_data.index, y='mean', data=experience_lvl_data)
plt.title('Salario Promedio por Nivel de Experiencia')
plt.xlabel('Nivel de Experiencia')
plt.ylabel('Salario Promedio')
plt.show()

>>>>>>> a3043c07c7547d06ac13da4a13052c404429a263
print(" --- ANALISIS GEOGRAFICO ---")
analisis_geografico = salario.groupby('company_location')['salary'].agg(['max', 'mean', 'count', np.std])
print(analisis_geografico)

# ---> ANALISIS GEOGRAFICO
print(" --- ANALISIS POR TAMAÑO DE EMPRESA ---")
analisis_tamaño_empresa = salario.groupby('company_size')['salary'].agg(['max', 'mean', 'count', np.std])
print(analisis_tamaño_empresa)

# ---> ANALISIS POR TIPO DE MODALIDAD
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

# ----> GRAFICO DE BARRAS PARA EL ANALISIS POR TIPO DE MODALIDAD
# ----> GRAFICO DE BARRAS PARA EL ANALISIS POR TIPO DE MODALIDAD
# ----> GRAFICO DE BARRAS PARA EL ANALISIS POR TIPO DE MODALIDAD
ax = sns.barplot(x=tipo_modalidad.index, y='mean', data=tipo_modalidad)
plt.title('Salario promedio por tipo de modalidad')
plt.xlabel('Modalidad')
plt.ylabel('Salario Promedio')

    # ---> ESTE BUCLE AGREGA ETIQUETAS A LAS BARRAS
for i, v in enumerate(tipo_modalidad['mean']):
    ax.text(i, v + 500, f'{v:.2f}', ha='center', va='bottom', fontsize=8)

plt.show()

analisis_temporal = salario.groupby('work_year')['salary'].agg(['max', 'mean', 'count', np.std])
print(" --- ANALISIS DE TENDENCIAS TEMPORALES ---")
print(analisis_temporal)

analisis_titulo_ubicacion = salario.groupby(['job_title', 'company_location'])['salary'].agg(['max', 'mean', 'count', np.std])
print(" --- ANALISIS POR TITULO DE TRABAJO Y UBICACION ---")
print(analisis_titulo_ubicacion)





