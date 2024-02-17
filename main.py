# main.py
import os
import time
from tkinter import filedialog, Tk
from musicConverter import MusicConverter
from parallelConverter import ParallelConverter


def select_folder(prompt):
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    folder_path = filedialog.askdirectory(title=prompt)  # Permitir seleccionar una carpeta
    root.destroy()
    return folder_path

def select_file(prompt):
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(title=prompt)  # Permitir seleccionar un archivo
    root.destroy()
    return file_path

if __name__ == "__main__":
    while True:
        user_choice = input("Seleccione una opción:\n  1. Seleccionar un archivo\n  2. Seleccionar una carpeta\nOpción: ")
        if user_choice in ['1', '2']:
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
    
    dir_list = []
    if user_choice == '1':
        selected_path = select_file("Seleccione un archivo") #D:/EAFIT/S7/SO/P1/Music/segundo.wav
        if selected_path:
            print("Seleccionó el archivo:", selected_path) 
            output_folder = os.path.join(os.path.dirname(selected_path), "output") #D:/EAFIT/S7/SO/P1/Music/output
            dir_list = dir_list + [selected_path] #['D:/EAFIT/S7/SO/P1/Music/segundo.mp3']
    elif user_choice == '2':
        selected_path = select_folder("Seleccione una carpeta") #D:/EAFIT/S7/SO/P1/Music
        if selected_path:
            print("Seleccionó la carpeta:", selected_path)
            output_folder = os.path.join(selected_path, "output") #D:/EAFIT/S7/SO/P1/Music/output
            nameMusic_list = os.listdir(selected_path)            # ['mus1.wav', 'mus2.wav']

            dir_list = [os.path.join(selected_path, filename) for filename in nameMusic_list] # ['D:/EAFIT/S7/SO/P1/Music/mus1.wav', D:/EAFIT/S7/SO/P1/Music/mus2.wav',]
        


    # Crear la carpeta "output" en la misma dirección que la ruta seleccionada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("Se creó la carpeta 'output' en:", output_folder)
    else:
        print("La carpeta 'output' ya existe en la ruta seleccionada.")

    music_converter = MusicConverter(output_folder)
    parallel_converter = ParallelConverter(music_converter)

    core_count = os.cpu_count()

    if 'output' in dir_list:
        dir_list.remove('output')

    start_time = time.time()


    parallel_converter.convert(dir_list)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("La tarea tardó {} segundos en completarse y la cantidad de cores encontrada fue de {}".format(elapsed_time, core_count))