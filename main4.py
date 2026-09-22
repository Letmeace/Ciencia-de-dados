import pandas as pd 

Empresa =  {
    'Funcionarios': ['Bernardo', 'Mayron', 'eduarda', 'Maria'],
    'Nota': [10, 8.7, 9.7, 9.75],
    'Salario': [5000, 6000, 7000, 8000],
    'Escala': ['Manha', 'Tarde', 'Noite', 'Manha'],
    'Departamento': ['RH', 'TI', 'Financeiro', 'Marketing'],
    'Horas_extra': [500, 600, 700, 800]
}

Empresa_df = pd.DataFrame(Empresa)

print(Empresa_df.head(3))

print(Empresa_df.tail(2))

Empresa_df.info()

print(Empresa_df[['Salario', 'Nota']].describe())



