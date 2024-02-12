# main.py

import os
import time

from musicConverter import MusicConverter
from parallelConverter import ParallelConverter


if __name__ == "__main__":
    path_folder = input("Enter the path folder:")
    output_folder = input("Enter the output folder: ")

    music_converter = MusicConverter(output_folder)
    parallel_converter = ParallelConverter(music_converter)

    inicio = time.time()
    
    for filename in os.listdir(path_folder):
        if not os.path.exists(path_folder):
            print("input file doesn't exist")
        else:
            input_file = os.path.join(path_folder, filename)
            parallel_converter.convert(input_file)
    
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("La tarea tardó {} segundos en completarse.".format(tiempo_transcurrido))
