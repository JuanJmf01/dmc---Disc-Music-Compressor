# main.py
# ffmpeg
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
        user_choice = input("Seleccione una opcion:\n  1. Seleccionar un archivo\n  2. Seleccionar una carpeta\nOpcion: ")
        if user_choice in ['1', '2']:
            break
        else:
            print("Opcion no válida. Por favor, seleccione 1 o 2.")
    
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
    print("\nLa tarea tardó {} segundos en completarse".format(round(elapsed_time)))
    print("la cantidad de cores encontrada fue de {}".format(core_count))

    # Información sobre los archivos convertidos
    fileQuantity = len(os.listdir(output_folder))
    print("\nLa cantidad total de archivos convertidos es:", fileQuantity)

    # Contadores para archivos MP3 y OGG
    mp3Quantity = 0
    oggQuantity = 0
    mp3TotalSize = 0
    oggTotalSize = 0

    # Calcular la cantidad y tamaño total de archivos MP3 y OGG
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path) / (1024 * 1024) # Convertir bytes a MB
            file_extension = os.path.splitext(file)[1]
            if file_extension == '.mp3':
                mp3Quantity += 1
                mp3TotalSize += file_size
            elif file_extension == '.ogg':
                oggQuantity += 1
                oggTotalSize += file_size
            else:
                print("Archivo no reconocido:", file)

    # Imprimir información sobre archivos MP3
    print("\nArchivos MP3:")
    print("Cantidad de archivos MP3:", mp3Quantity)
    print("Tamaño total de archivos MP3:", round(mp3TotalSize, 2), "MB")

    # Imprimir información sobre archivos OGG
    print("\nArchivos OGG:")
    print("Cantidad de archivos OGG:", oggQuantity)
    print("Tamaño total de archivos OGG:", round(oggTotalSize, 2), "MB")


    # Preguntar al usuario si desea mantener archivos MP3 y OGG
    keep_mp3 = input("\n¿Desea mantener los archivos MP3? (yes/no): ").lower().strip() == 'yes'
    keep_ogg = input("¿Desea mantener los archivos OGG? (yes/no): ").lower().strip() == 'yes'

    # Eliminar archivos según la selección del usuario
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        file_extension = os.path.splitext(file)[1]
        if file_extension == '.mp3' and not keep_mp3:
            os.remove(file_path)
        elif file_extension == '.ogg' and not keep_ogg:
            os.remove(file_path)

    print("\nOperación completada.")
