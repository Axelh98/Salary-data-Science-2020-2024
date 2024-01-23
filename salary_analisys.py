import pandas as pd
import numpy as np

archivo = 'data_science_salaries.csv'

salario = pd.read_csv(archivo)


### Analisis por nivel de Experiencia.
print('--- ANALISIS POR NIVEL DE EXPERIENCIA --- ')
experience_lvl_data = salario.groupby('experience_level')['salary'].agg(['max', 'mean', 'count'])
print(experience_lvl_data)

print(" --- ANALISIS GEOGRAFICO ---")
analisis_geografico = salario.groupby('company_location')['salary'].agg(['max', 'mean', 'count', np.std])
print(analisis_geografico)

print(" --- ANALISIS POR TAMAÑO DE EMPRESA ---")
analisis_tamaño_empresa = salario.groupby('company_size')['salary'].agg(['max', 'mean', 'count', np.std])
print(analisis_tamaño_empresa)

print(" --- ANALISIS POR TIPO DE MODALIDAD ---")
tipo_modalidad = salario.groupby('work_models')['salary'].agg(['max', 'mean', 'count', np.std])
print(tipo_modalidad)






