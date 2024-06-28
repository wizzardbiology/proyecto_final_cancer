from collections import Counter

# Lista de mutaciones
mutations = [
    "G->A", "A->T", "T->G", "G->C", "G->A", "A->G", "T->A", "T->C",
    "G->C", "G->C", "G->A", "G->C", "T->A", "T->G", "T->C", "C->G",
    "C->A", "C->G", "T->C", "C->T", "C->A", "A->C", "T->C", "G->A",
    "G->C", "C->G", "T->A", "A->C", "A->C", "G->C", "A->C", "G->C",
    "G->T", "C->A", "G->A", "C->G", "T->C", "A->C", "A->G", "A->G",
    "G->A", "T->G", "T->A", "T->C", "T->A", "G->T", "A->T", "G->T",
    "C->T", "T->C", "T->C", "C->G", "T->A", "C->A", "A->C", "A->T",
    "A->G"
]

# Contar las frecuencias de cada tipo de mutación
mutation_frequencies = Counter(mutations)

# Imprimir las frecuencias
for mutation, frequency in mutation_frequencies.items():
    print(f"{mutation}: {frequency}")
