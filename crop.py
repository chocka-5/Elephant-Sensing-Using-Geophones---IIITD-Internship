from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("cycle_14.wav" , "wav") 
chunk_length_ms = 10000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of ten seconds

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "cycle{0}.wav".format(i+323)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")