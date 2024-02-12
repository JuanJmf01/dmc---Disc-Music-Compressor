# musicConverter.py

import subprocess as sub

# The `MusicConverter` class provides methods to convert audio files to AAC and MP3 formats using
# FFmpeg.
class MusicConverter:
    def __init__(self, output_folder):
        self.output_folder = output_folder

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
