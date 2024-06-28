import matplotlib.pyplot as plt

# Datos de frecuencia de tipos de cambio
mutation_frequencies = {
    'G->A': 6,
    'A->T': 3,
    'T->G': 3,
    'G->C': 7,
    'A->G': 4,
    'T->A': 6,
    'T->C': 8,
    'C->G': 5,
    'C->A': 4,
    'C->T': 2,
    'A->C': 6,
    'G->T': 3,
}

# Extraer datos para el gráfico
mutation_types = list(mutation_frequencies.keys())
frequencies = list(mutation_frequencies.values())

# Crear un gráfico de barras
plt.figure(figsize=(12, 6))
plt.barh(mutation_types, frequencies, color='skyblue', edgecolor='black')
plt.xlabel('Frecuencia')
plt.ylabel('Tipo de Cambio')
plt.title('Frecuencia de Tipos de Cambio en el Gen TP53 (Humano vs. Glotón)')
plt.tight_layout()
plt.show()
