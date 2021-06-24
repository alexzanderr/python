

import wave
import pyaudio
from threading import Thread
from pathlib import Path


class AudioRecorder:
    def __init__(
        self,
        save_destination,
        remote_save_destination,
        stop_flag,
        stop_all
    ):
        if isinstance(save_destination, Path):
            self.save_destination = save_destination.as_posix()
        else:
            self.save_destination = save_destination

        if isinstance(remote_save_destination, Path):
            self.remote_save_destination = save_destination.as_posix()
        else:
            self.remote_save_destination = save_destination

        self.stop_flag = stop_flag
        self.stop_all = stop_all

        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100  # Record at 44 samples per second
        # self.p = pyaudio.PyAudio()
        # self.stream = self.p.open(format=self.sample_format,
        #                 channels=self.channels,
        #                 rate=self.fs,
        #                 frames_per_buffer=self.chunk,
        #                 input=True)
        self.record = True
        self.audio_thread = Thread(target=self.record_audio)
        self.frames = []


    def record_audio(self):
        self.p = pyaudio.PyAudio()


        # the stream needs to be opened before starting nrecording
        # in order to synchronize
        # the audio and the video
        self.stream = self.p.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.fs,
            frames_per_buffer=self.chunk,
            input=True
        )

        while self.record and not self.stop_all[0]:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.save()

        self.stop_flag[0] = True


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



    pass


