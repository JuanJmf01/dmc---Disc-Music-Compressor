import os
import multiprocessing as Pool
import subprocess as sub


def convert_to_mp3(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, '-codec:a', 'libmp3lame', '-qscale:a', '2', output_file]
    sub.run(command)

if __name__ == "__main__":
    path_folder = input("Enter the path folder:")
    output_folder = input("Enter the output folder: ")
    for filename in os.listdir(path_folder):
        if not os.path.exists(path_folder):
            print("input file doesn't exist")
        else:
            input_file = os.path.join(path_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + "." + "mp3")
        
        convert_to_mp3(input_file, output_file)

   # if not os.path.exists(input_file):
      #  print("Input file does not exist.")
 #  else:
     #   convert_to_mp3(input_file, output_file)
    #    print("Conversion completed successfully.")





'''
path_folder1 = input("Ingresa el directorio: ")
path_folder2 = input("Ingresa la carpeta de destino: ")

sub.call(['ffmpeg', '-i', path_folder1, path_folder2])
'''


'''
ext = input("Ingresa la extensión que quieres cambiar: ")
newExt = input("Ingresa el nuevo formato: ")

for filename in os.listdir(path_folder):
    if filename.endswith("." + ext):
        old_path = os.path.join(path_folder, filename)
        new_path = os.path.join(path_folder, os.path.splitext(filename)[0] + "." + newExt)
        print(old_path)
        print(new_path)

        os.rename(old_path, new_path)
print(f"Se cambiaron los archivos con la extension '{ext}' a '{newExt}' en la carpeta {path_folder}.")
'''