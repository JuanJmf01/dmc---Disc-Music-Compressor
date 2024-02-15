#parallelConverter.py
import os
import multiprocessing as mp

class ParallelConverter:

    def __init__(self, music_converter):
        self.music_converter = music_converter

    def convert(self, input_files):

        """
        A process pool object which controls a pool of worker processes to which jobs can be submitted. 
        It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.
        library link : https://docs.python.org/3/library/multiprocessing.html
        Find the amount of cores the cpu has and then we use the multiprocessing.Pool this allows us to create a pool of processes.
        """
        #The cpu count and the pool method are instanciated here.
        cpuCount = os.cpu_count()
        process = mp.Pool(cpuCount)
        #Tuples
        mp3Output = []
        aacOutput = []
        '''Create the tuples for each file in files(The files that are found in the directory thats passed by the user) so that we can then
            pass this tuple to the convertAac and convertmp3 in the musicConverter and encode each file in parallel using the pool function and the starmap from multiprocessing
            allowing us to send the tuples as arguments to the function.
        '''
        #MP3 ITERATOR and #AAC ITERATOR used to make the output tuples which contain the output folder and the file extension for each file of the input files.
        for files in input_files:
            mp3Output.append((files, os.path.join(self.music_converter.output_folder, os.path.splitext(os.path.basename(files))[0] + ".mp3"))) #Mp3 conversion
            aacOutput.append((files, os.path.join(self.music_converter.output_folder, os.path.splitext(os.path.basename(files))[0] + ".aac"))) #AAC conversion 
 
        '''
        Arguments to be passed to the convertmp3 and convertAcc functions in musicConverter.
        The starmap method from multiprocessing is used to execute the functions convertMp3 and convertAAC like the mp.Process and mp.start but it also allows
        for each method to run in parallel across multiple processes with each handling a different conversion task so for each starmap we pass the tuple containing all the input files and all the output files 
        '''
        process.starmap(self.music_converter.convertmp3, mp3Output)
        process.starmap(self.music_converter.convertAcc, aacOutput)
        '''
        this methods are used by pool, close is used to not allow anymore workers into the pool and join is used to wait for any worker process in the pool
        to have completed their task and end
        '''
        process.close()
        process.join()
