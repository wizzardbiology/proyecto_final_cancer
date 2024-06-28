import matplotlib.pyplot as plt

# Datos de frecuencia de tipos de cambio
changes = {
    'G->A': 81,
    'A->T': 101,
    'T->G': 151,
    'G->C': 195,
    'A->G': 134,
    'T->A': 118,
    'T->C': 173,
    'C->G': 171,
    'C->A': 95,
    'C->T': 139,
    'A->C': 174,
    'G->T': 96,
    'N->C': 355,
    'N->G': 347,
    'N->T': 226,
    'N->A': 172,
    'C->': 126,
    'T->': 123,
    'G->': 98,
    'A->': 74,
}

# Crear listas de tipos de cambio y frecuencias
change_types = list(changes.keys())
frequencies = list(changes.values())

# Crear el gráfico
plt.figure(figsize=(14, 8))
plt.barh(change_types, frequencies, color='skyblue')
plt.xlabel('Frecuencia')
plt.ylabel('Tipo de Cambio')
plt.title('Frecuencia de Tipos de Cambio en el Gen TP53 (Humano vs. Glotón)')
plt.tight_layout()
plt.show()
