#oarallelConverter.py

import os
import multiprocessing

# The `ParallelConverter` class allows for parallel conversion of music files to both MP3 and AAC
# formats.
class ParallelConverter:
    def __init__(self, music_converter):
        self.music_converter = music_converter

    def convert(self, input_file):
        """
        The `convert` function takes an input file and converts it to both MP3 and AAC formats using
        multiprocessing.
        
        :param input_file: The input_file parameter is the path to the file that needs to be converted.
        It can be a file in any audio format that is supported by the music_converter object
        """
        mp3_output_file = os.path.join(self.music_converter.output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".mp3")
        acc_output_file = os.path.join(self.music_converter.output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".aac")

        # Crear procesos para la conversión a mp3 y aac
        mp3_process = multiprocessing.Process(target=self.music_converter.convertmp3, args=(input_file, mp3_output_file))
        aac_process = multiprocessing.Process(target=self.music_converter.convertAcc, args=(input_file, acc_output_file))
        
        # Iniciar los procesos
        mp3_process.start()
        aac_process.start()
        
        # Esperar a que los procesos terminen
        mp3_process.join()
        aac_process.join()
