#!/bin/bash

# Directorio de entrada y salida
INPUT_DIR="./fasta_files"
OUTPUT_DIR="./results"
REFERENCE_SEQ="./reference/tp53_reference.fasta"

# Crear directorio de salida si no existe
mkdir -p $OUTPUT_DIR

# Función para comparar secuencias
compare_sequences() {
    local file=$1
    local output_file=$2
    local reference=$REFERENCE_SEQ
    
    # Leer la secuencia de referencia
    ref_seq=$(grep -v '^>' $reference | tr -d '\n')

    # Leer la secuencia de entrada
    seq=$(grep -v '^>' $file | tr -d '\n')
    
    # Comparar secuencias y encontrar diferencias
    diff_pos=""
    for ((i=0; i<${#ref_seq}; i++)); do
        if [ "${seq:$i:1}" != "${ref_seq:$i:1}" ]; then
            diff_pos+="$i: ${ref_seq:$i:1}->${seq:$i:1}\n"
        fi
    done

    # Guardar las diferencias en el archivo de salida
    echo -e $diff_pos > $output_file
}

# Procesar cada archivo FASTA en el directorio de entrada
for fasta_file in $INPUT_DIR/*.fasta; do
    filename=$(basename -- "$fasta_file")
    output_file="$OUTPUT_DIR/${filename%.fasta}_mutations.txt"
    compare_sequences $fasta_file $output_file
done

echo "Análisis completado. Los resultados están en el directorio $OUTPUT_DIR."
