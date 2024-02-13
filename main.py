# main.py

import os
import time
from tqdm import tqdm
from musicConverter import MusicConverter
from parallelConverter import ParallelConverter


if __name__ == "__main__":
    path_folder = input("Enter the path folder:")
    output_folder = input("Enter the output folder: ")


    music_converter = MusicConverter(output_folder)
    parallel_converter = ParallelConverter(music_converter)
    dir_list = os.listdir(path_folder)
    inicio = time.time()
    progress_bar = tqdm(dir_list, desc="Converting files", unit="file")

    for filename in progress_bar:
        if not os.path.exists(path_folder):
            print("input file doesn't exist")
        else:
            input_file = os.path.join(path_folder, filename)
            parallel_converter.convert(input_file)
    
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("La tarea tardó {} segundos en completarse.".format(tiempo_transcurrido))

