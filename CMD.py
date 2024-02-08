import os
import multiprocessing as Pool
import subprocess as sub

#def convert_to_acc(input_file, output_file):
    #command to encode to acc.


def convert_to_mp3(input_file, output_file):
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
        
        convert_to_mp3(input_file, output_file)

