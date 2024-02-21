#musicConverter.py
import os
import subprocess as sub

# The `MusicConverter` class in Python is designed to convert music files using FFmpeg.
class MusicConverter:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def convert_file(self, input_file, output_file):
        """
        The function `convert_file` takes an input file, an output file, and uses ffmpeg to convert the
        input file to the specified output file.
        
        :param input_file: Thank you for providing the code snippet. It looks like you are trying to
        convert a file using FFmpeg. To complete the print statement with the input file parameter, you
        can simply concatenate the input file variable to the print statement. Here's how you can do it:
        :param output_file: The `output_file` parameter is the file path where the converted file will be
        saved after the conversion process is completed
        """
    

        print("input_file: {}".format(input_file))
        print("output_file: {}".format(output_file))

        command = ['ffmpeg', '-i', input_file, output_file]
        sub.run(command)
