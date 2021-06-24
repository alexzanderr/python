



import warnings

import wave
import pyaudio
from threading import Thread
from pathlib import Path
from time import sleep

warnings.simplefilter('ignore', category=pyaudio)

class AudioRecorder:
    def __init__(
        self,
        save_destination,
    ):
        if isinstance(save_destination, Path):
            self.save_destination = save_destination.as_posix()
        else:
            self.save_destination = save_destination


        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100  # Record at 44 samples per second
        self.record = True
        self.audio_thread = Thread(target=self.record_audio)
        self.frames = []


    def record_audio(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format,
        channels=self.channels,
        rate=self.fs,
        frames_per_buffer=self.chunk,
        input=True)
        while self.record:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.save()


    def start_thread(self):
        self.audio_thread.start()


    def stop_audio_thread(self):
        self.record = False


    def save(self):
        wf = wave.open(self.save_destination, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b"".join(self.frames))
        wf.close()





if __name__ == "__main__":

    save_path = Path("testing.wav")
    audio_recorder = AudioRecorder(save_path)

    print("\nspeak:\n")
    audio_recorder.start_thread()

    sleep(5)

    audio_recorder.stop_audio_thread()
    print("done")



    pass


