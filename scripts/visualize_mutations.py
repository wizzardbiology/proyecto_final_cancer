import matplotlib.pyplot as plt

# Leer las mutaciones del archivo
with open('results/gloton_tp53_mutations.txt', 'r') as file:
    mutations = file.readlines()

# Extraer posiciones
positions = []
for mutation in mutations:
    if mutation.strip():
        pos, _ = mutation.split(':')
        positions.append(int(pos.strip()))

# Crear un histograma de las mutaciones
plt.figure(figsize=(14, 7))
plt.hist(positions, bins=50, color='skyblue', edgecolor='black')
plt.xlabel('Position in Gene')
plt.ylabel('Number of Mutations')
plt.title('Distribution of Mutations in TP53 Gene (Human vs. Gloton)')
plt.grid(True)
plt.tight_layout()
plt.show()

