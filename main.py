# main.py
import os
import time
from musicConverter import MusicConverter
from parallelConverter import ParallelConverter


if __name__ == "__main__":

    #print("Hello-------- welcome to CMD music converter please select if you want to convert files inside of a folder or just one file!")
    path_folder = input("Enter the path folder:")
    output_folder = input("Enter the output folder: ")
    coreCount = os.cpu_count()

    music_converter = MusicConverter(output_folder)
    parallel_converter = ParallelConverter(music_converter)
    dir_list = os.listdir(path_folder)
    inicio = time.time()

    #Simple list 
    input_files = []
    for filename in dir_list:
        input_files.append(os.path.join(path_folder, filename))

    # Pass the list of input files to the convert method
    parallel_converter.convert(input_files)

    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("La tarea tardó {} segundos en completarse y la cantidad de cores encontrada fue de {}".format(tiempo_transcurrido, coreCount))


#C:\Users\usuario\Desktop\testing1
#C:\Users\usuario\Desktop\moveTo
    

    