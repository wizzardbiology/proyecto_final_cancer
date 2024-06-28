
# Proyecto Final de Bioinformática: Análisis del Gen TP53

Este proyecto analiza las mutaciones en el gen TP53 comparando secuencias de Homo sapiens y Gulo gulo (glotón). 

## Estructura del Proyecto

1. **scripts/**: Contiene los scripts utilizados para analizar los datos.
2. **data/**: Contiene los archivos de secuencia utilizados en el análisis.
3. **results/**: Contiene los resultados de los análisis, incluyendo gráficos y tablas de mutaciones.

## Scripts

- `analyze_tp53.sh`: Script principal para analizar las secuencias.
- `calculate_frequencies.py`: Calcula las frecuencias de las mutaciones.
- `clean_sequence.py`: Limpia las secuencias de entrada.
- `count_mutation_frequencies.py`: Cuenta las frecuencias de las mutaciones.
- `visualize_frequencies.py`: Genera gráficos de las frecuencias de las mutaciones.
- `visualize_mutation_frequencies.py`: Genera gráficos de la distribución de mutaciones.
- `visualize_mutations.py`: Visualiza las mutaciones en las secuencias.

## Datos

- `tp53_reference.fasta`: Secuencia de referencia del gen TP53 de Homo sapiens.
- `gloton_tp53.fasta`: Secuencia del gen TP53 de Gulo gulo.

## Resultados

- `Frecuencia de Tipos de Cambio en el Gen TP53 (Humano vs. Glotón).png`: Gráfico de las frecuencias de tipos de cambio en las mutaciones.
- `Distribución de Mutaciones en el Gen TP53 (Humano vs. Glotón).png`: Gráfico de la distribución de mutaciones a lo largo del gen TP53.
- `Alineación de Secuencias del Gen TP53 (Humano vs. Glotón).png`: Alineación de las secuencias del gen TP53 entre humano y glotón.

## Conclusiones

El análisis muestra una mayor frecuencia de ciertas mutaciones en el gen TP53 cuando se compara entre Homo sapiens y Gulo gulo. Estas diferencias pueden proporcionar información sobre la evolución y las funciones específicas del gen en diferentes especies.

## Introducción

El gen TP53, conocido como el "guardián del genoma", es fundamental en la regulación del ciclo celular y en la preservación de la estabilidad genética. Este gen codifica una proteína que actúa como un supresor de tumores al prevenir la proliferación de células dañadas. Las mutaciones en TP53 son comúnmente observadas en una amplia variedad de cánceres y están asociadas con la progresión de la enfermedad y la resistencia a la terapia.

## Importancia del Gen TP53

El TP53 desempeña un papel crucial en la respuesta celular a los daños en el ADN. Cuando una célula sufre daño genético, TP53 puede detener el ciclo celular para permitir la reparación del ADN, o bien, inducir la apoptosis si el daño es irreparable. De este modo, TP53 evita la acumulación de mutaciones que podrían conducir a la formación de tumores. Las mutaciones en TP53 pueden inactivar esta función protectora, lo que facilita la supervivencia y proliferación de células malignas.

## Objetivo del Estudio

El objetivo de este estudio es analizar las mutaciones en el gen TP53 comparando las secuencias de referencia humana y de glotón. Comparar estas secuencias nos permite entender mejor las diferencias evolutivas y funcionales entre especies, y cómo estas diferencias pueden influir en la susceptibilidad al cáncer y otras enfermedades.

## Metodología

### Recopilación de Secuencias

Las secuencias del gen TP53 fueron obtenidas de bases de datos genómicas. La secuencia de referencia humana fue descargada de [NCBI](https://www.ncbi.nlm.nih.gov/), mientras que la secuencia del glotón fue obtenida a través de BLAST.

### Análisis de Mutaciones

Se identificaron y anotaron las mutaciones presentes en el gen TP53 comparando la secuencia de referencia humana con la del glotón. Las mutaciones fueron categorizadas por tipo de cambio nucleotídico (por ejemplo, `G->A`, `A->T`).

## Resultados del Análisis de Mutaciones

Este análisis identificó múltiples mutaciones entre la secuencia de referencia humana y la secuencia del glotón en el gen TP53. A continuación se presentan algunos ejemplos de las mutaciones encontradas:

- `0: G->A`
- `1: A->T`
- `2: T->G`
- `3: G->C`
- `4: G->A`
- `6: A->G`
- `7: T->A`
- `8: T->C`
- ...

## Visualización de las Mutaciones

### Distribución de Mutaciones en el Gen TP53

![Distribución de Mutaciones en el Gen TP53](results/Distribuci%C3%B3n%20de%20Mutaciones%20en%20el%20Gen%20TP53%20(Humano%20vs.%20Glot%C3%B3n).png)

#### Análisis del Gráfico

Este gráfico muestra la distribución de las mutaciones a lo largo de la secuencia del gen TP53. Cada barra representa un intervalo de posiciones en el gen y la altura de la barra indica el número de mutaciones en ese intervalo. Las regiones con barras más altas indican una mayor cantidad de mutaciones, lo que sugiere que estas áreas son más propensas a cambios genéticos.

#### Observaciones Clave

- **Regiones con Alta Frecuencia de Mutaciones**: Las posiciones con barras significativamente más altas pueden corresponder a zonas críticas del gen donde las mutaciones son más frecuentes.
- **Regiones Conservadas**: Las áreas con barras más bajas sugieren regiones más conservadas del gen que pueden ser esenciales para su función y, por tanto, menos propensas a mutaciones.

### Frecuencia de Tipos de Cambio en el Gen TP53

![Frecuencia de Tipos de Cambio en el Gen TP53](results/Frecuencia%20de%20Tipos%20de%20Cambio%20en%20el%20Gen%20TP53%20(Humano%20vs.%20Glot%C3%B3n).png)

#### Análisis del Gráfico

Este gráfico muestra la frecuencia de los diferentes tipos de cambios nucleotídicos (por ejemplo, `G->A`, `A->T`) en el gen TP53. Cada barra representa un tipo de cambio y su altura indica la cantidad de veces que se observa ese cambio en las secuencias comparadas.

#### Observaciones Clave

- **Cambios Comunes**: `T->C` es el cambio más frecuente con 8 ocurrencias, seguido por `G->C` con 7 ocurrencias. Estos tipos de cambios pueden estar relacionados con mecanismos específicos de mutación o con características estructurales del gen.
- **Cambios Menos Comunes**: Cambios como `C->T` y `G->T` son menos frecuentes, lo que puede indicar una menor susceptibilidad a estos tipos de mutaciones en las regiones estudiadas del gen TP53.

## Resultados de BLAST

### Alineación de Secuencias

Se realizó una alineación de secuencias entre el gen TP53 humano y el gen TP53 del glotón utilizando BLAST. Los resultados indican una alta similitud entre las dos secuencias.

#### Descripción de la Alineación

- **Gen Alineado**: Gen Gulo gulo luscus TP53 (TP53), cds completo
- **Puntuación Máxima**: 152
- **Puntuación Total**: 152
- **Cubierta de Consulta**: 5%
- **Valor E**: 9E-40
- **Identificación**: 90.43%

### Detalle de la Alineación

![Detalle de la Alineación](results/Alineaci%C3%B3n%20de%20Secuencias%20del%20Gen%20TP53%20(Humano%20vs.%20Glot%C3%B3n).png)

### Análisis del Resultado

La alineación muestra una alta similitud entre las dos secuencias, con un 90.43% de nucleótidos idénticos. Sin embargo, solo el 5% de la secuencia de consulta está cubierta en la alineación, lo que sugiere que podría haber diferencias significativas en otras regiones del gen no incluidas en esta alineación.

### Interpretación del Alineamiento
- **Similitudes**:
  - La mayoría de los nucleótidos en esta región son idénticos, lo que indica que estas secuencias han conservado su estructura a lo largo de la evolución.
  - Las posiciones alineadas muestran una alta similitud (90%), reflejando la conservación de secuencias críticas para la función del gen TP53.

- **Diferencias**:
  - Las diferencias nucleotídicas (10%) pueden representar variaciones evolutivas entre las dos especies.
  - Estas variaciones pueden tener implicaciones funcionales o ser neutrales, dependiendo de la región específica del gen y su impacto en la proteína codificada.

## Conclusión Comparativa de las Imágenes

Comparar la distribución de mutaciones y la frecuencia de tipos de cambios nucleotídicos en el gen TP53 proporciona una visión más completa de la naturaleza de estas mutaciones:

1. **Susceptibilidad a Mutaciones**:
   - Las regiones del gen TP53 con una alta frecuencia de mutaciones son áreas críticas que pueden ser más susceptibles a cambios debido a su estructura o exposición a factores mutagénicos.
   - La alta frecuencia de ciertos tipos de cambios nucleotídicos, como `T->C` y `G->C`, sugiere que estos tipos de mutaciones son más comunes en el gen TP53 y pueden estar impulsados por mecanismos específicos de mutación.

2. **Regiones Conservadas vs. Regiones Variables**:
   - Las regiones conservadas del gen, que muestran menos mutaciones, son probablemente esenciales para la función del gen TP53 y están bajo una fuerte presión selectiva para mantener su integridad.
   - Las regiones con más mutaciones pueden ser áreas de menor importancia funcional o pueden estar más expuestas a factores que inducen mutaciones.

3. **Impacto Biológico**:
   - Las mutaciones frecuentes en el gen TP53 pueden tener un impacto significativo en su función como supresor de tumores. Las áreas con mutaciones frecuentes pueden ser puntos críticos para la investigación sobre cómo las mutaciones en TP53 contribuyen al desarrollo y progresión del cáncer.
   - Comprender los tipos de cambios nucleotídicos más comunes puede ayudar a dirigir estudios futuros sobre los mecanismos de mutación y la prevención del cáncer.

Este análisis proporciona una base para investigar más a fondo las mutaciones en el gen TP53 y su impacto en la biología del cáncer.

## Bibliografía

1. Vousden, K. H., & Lane, D. P. (2007). p53 in health and disease. *Nature Reviews Molecular Cell Biology*, 8(4), 275-283. https://doi.org/10.1038/nrm2147
2. Levine, A. J., & Oren, M. (2009). The first 30 years of p53: growing ever more complex. *Nature Reviews Cancer*, 9(10), 749-758. https://doi.org/10.1038/nrc2723
3. Kandoth, C., et al. (2013). Mutational landscape and significance across 12 major cancer types. *Nature*, 502(7471), 333-339. https://doi.org/10.1038/nature12634
4. Vousden, K. H. (2000). p53: death star. *Cell*, 103(5), 691-694. https://doi.org/10.1016/S0092-8674(00)00170-0
5. Petitjean, A., et al. (2007). Impact of mutant p53 functional properties on TP53 mutation patterns and tumor phenotype: lessons from recent developments in the IARC TP53 database. *Human Mutation*, 28(6), 622-629. https://doi.org/10.1002/humu.20495


