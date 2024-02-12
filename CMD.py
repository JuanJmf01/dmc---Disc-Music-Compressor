import os
import multiprocessing as mp
import subprocess as sub

def convertAcc(input_file, output_file):
    command2 = ['ffmpeg', '-i', input_file, '-codec:a', 'aac', output_file]
    sub.run(command2)


def convertmp3(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, '-codec:a', 'libmp3lame', '-qscale:a', '2', output_file]
    sub.run(command)
    #change codec and bitrate.


if __name__ == "__main__":
    path_folder = input("Enter the path folder:")
    output_folder = input("Enter the output folder: ")
    for filename in os.listdir(path_folder):
        if not os.path.exists(path_folder):
            print("input file doesn't exist")
        else:
            input_file = os.path.join(path_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + "." + "mp3")
        
        convertmp3(input_file,output_file)

    for filename in os.listdir(path_folder):
        if not os.path.exists(path_folder):
            print("input file doesn't exist")
        else:
            input_file = os.path.join(path_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + "." + "aac")

        convertAcc(input_file, output_file)
    
    
#usar multiprocessing!