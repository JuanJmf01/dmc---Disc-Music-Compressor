# main.py
import os
import time
from musicConverter import MusicConverter
from parallelConverter import ParallelConverter
import time
def WorkInFile(path_folder,output_folder):
    coreCount = os.cpu_count()
    music_converter = MusicConverter(output_folder)
    parallel_converter = ParallelConverter(music_converter)
    input_files = []
    if os.path.isdir(path_folder):
        inicio = time.time()
        dir_list = os.listdir(path_folder)# es un directorio. 
        for filename in dir_list:
            input_files.append(os.path.join(path_folder, filename))
     # Pass the list of input files to the convert method
    elif os.path.isfile(path_folder): # Es un
        inicio = time.time()
        input_files.append(path_folder)
        # es un archivo.
    
    #Simple list 
    parallel_converter.convert(input_files)

    fin = time.time() # El tiempo ha finalizado
    tiempo_transcurrido = fin - inicio # Calculo de tiempo transcurrido
    print("La tarea tardó {} segundos en completarse y la cantidad de cores encontrada fue de {}".format(tiempo_transcurrido, coreCount))

def ReadFile(path_folder):
    print("Archivos encontrado(s):")

    if os.path.isdir(path_folder):
        print(f"{path_folder}") # es un directorio.
        dir_list = os.listdir(path_folder)
        input_files = [os.path.join(path_folder, filename) for filename in dir_list]
        for file_path in input_files:
            print((file_path)+"\n")
    elif os.path.isfile(path_folder):
        print(path_folder+"\n") # es un archivo.

    
        

if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Trabajar con ruta de  carpeta")
        print("2. Trabajar con ruta de archivo")
        print("3. Salir del menú")

        choice = input("Ingrese su opción (1, 2, o 3): ")

        if choice == '1':
            path_folder = input("Ingrese la ruta de la carpeta: ")
            output_folder = input("Ingrese la carpeta de salida: ")
            ReadFile(path_folder)
            WorkInFile(path_folder,output_folder)
            input("Presiona Enter para salir...") 

        elif choice == '2':
            path_folder = input("Ingrese la ruta del archivo(s): ")
            output_folder = input("Ingrese la carpeta de salida: ")
            ReadFile(path_folder)
            WorkInFile(path_folder,output_folder)
            input("Presiona Enter para salir...")

        elif choice == '3':
            print("Saliendo del menú.")
            print("El siguiente proyecto fue realizado por: \nAlberto Andres Diaz Mejia <-> aadiazm@eafit.edu.co \nNicolas Betancur Ochoa <-> nbetancur1@eafit.edu.co \nJuan Jose Muñoz Florez <-> jjmunozf@eafit.edu.co")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
