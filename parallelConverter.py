#parallelConverter.py
import os
import multiprocessing as mp
# The `ParallelConverter` class takes a `music_converter` object and converts input music files to
# both MP3 and OGG formats in parallel using multiprocessing.

class ParallelConverter:

    def __init__(self, music_converter):
        self.music_converter = music_converter

    def convert(self, input_files):
        """
        The `convert` function takes a list of input files, extracts their base filenames, generates
        output file paths for both mp3 and ogg formats, and then uses multiprocessing to convert the
        input files to mp3 and ogg formats.
        
        :param input_files: The `convert` method you provided seems to be converting input music files
        to both MP3 and OGG formats using multiprocessing. The `input_files` parameter in this method
        should be a list of input music files that you want to convert
        """
     
        cpuCount = os.cpu_count()
        process = mp.Pool(cpuCount)
       
        output_files = []
        # This part of the code is iterating over each input file in the `input_files` list. For each
        # file, it extracts the filename and extension using `os.path.splitext(file)`. Then, it gets
        # the base filename using `os.path.basename(filename)`.
        for file in input_files:
            filename, ext = os.path.splitext(file)
            base_filename = os.path.basename(filename)
            output_file_mp3 = os.path.join(self.music_converter.output_folder, base_filename + ".mp3")
            output_file_ogg = os.path.join(self.music_converter.output_folder, base_filename + ".ogg")
            output_files.append((file, output_file_mp3))
            output_files.append((file, output_file_ogg))
        

        print("outputs : {}".format(output_files))
 
      
        # `process.starmap(self.music_converter.convert_file, output_files)` is using the `starmap`
        # method of the `Pool` object to apply the `self.music_converter.convert_file` function to
        # each pair of arguments in the `output_files` list.
        process.starmap(self.music_converter.convert_file, output_files)

     
        
        process.close()
        process.join()
