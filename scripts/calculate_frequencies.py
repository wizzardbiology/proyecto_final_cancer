from collections import Counter

# Leer las mutaciones del archivo
with open('results/gloton_tp53_mutations.txt', 'r') as file:
    mutations = file.readlines()

# Extraer los cambios
changes = []
for mutation in mutations:
    if mutation.strip():
        _, change = mutation.split(':')
        changes.append(change.strip())

# Contar la frecuencia de cada tipo de cambio
change_counts = Counter(changes)

# Mostrar la frecuencia de cada tipo de cambio
print("Frecuencia de tipos de cambio:")
for change, count in change_counts.items():
    print(f"{change}: {count} veces")
