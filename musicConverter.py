#musicConverter.py
import os
import subprocess as sub
# The `MusicConverter` class provides methods to convert audio files to AAC and MP3 formats using
# FFmpeg. FFmpeg docs about video and audio conversion "https://ffmpeg.org/ffmpeg.html#toc-Video-and-Audio-file-format-conversion"

class MusicConverter:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def convert_file(self, input_file, output_file):
        """
        The function converts an audio file to either AAC or MP3 format based on the file extension.

        :param input_file: The input file is the file that you want to convert.
        :param output_file: The name or path of the file where you want to save the converted audio file.
        """

        print("input_file: {}".format(input_file))
        print("output_file: {}".format(output_file))



        command = ['ffmpeg', '-i', input_file, output_file]
        sub.run(command)



        # Determine the file extension
        # file_extension = os.path.splitext(input_file)[1].lower()
        # print("TUPLA: {}".format(file_extension))

        # # Check the file extension and call the appropriate conversion method
        # if file_extension == '.aac':
        #     self.convertAcc(input_file, output_file)
        # elif file_extension in ('.mp3', '.wav', '.flac'):
        #     self.convertmp3(input_file, output_file)
        # else:
        #     print(f"Unsupported file format: {file_extension}")










    def convertAcc(self, input_file, output_file):
        
        """
        The function converts an audio file to AAC format using FFmpeg.
        
        :param input_file: The input file is the file that you want to convert. It can be any audio file
        format that is supported by ffmpeg, such as MP3, WAV, FLAC, etc
        :param output_file: The `output_file` parameter is the name or path of the file where you want
        to save the converted audio file
        """
        command = ['ffmpeg', '-i', input_file, '-codec:a', 'aac', output_file]
        sub.run(command)

        print("EJEMPLO OUTPUT FOLDER: {}".format(input_file))

        
    def convertmp3(self, input_file, output_file):

        """
        The function converts an input audio file to MP3 format using the ffmpeg library.
        
        :param input_file: The input file is the path to the audio file that you want to convert to MP3
        format
        :param output_file: The output_file parameter is the name or path of the file where you want to
        save the converted MP3 file
        """
        command = ['ffmpeg', '-i', input_file, '-codec:a', 'libmp3lame', '-qscale:a', '2', output_file]
        sub.run(command)
        
        