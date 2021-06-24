
import wave
import pyaudio
import time
import os
from core.json__ import *
from tqdm import tqdm as progess_bar
from core.path__ import *
from pynput.keyboard import Listener, Key, KeyCode
import threading
from core.aesthetics import *
from core.system import *

def play_wav_with_progress(wav_file, self):
    wf = wave.open(wav_file, "rb")
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    try:
        chunk = 1024
        data = wf.readframes(chunk)
        wav_frames = []
        while data:
            wav_frames.append(data)
            data = wf.readframes(chunk)

        _sep = get_path_sep(wav_file)
        _items = wav_file.split(_sep)
        destination_folder = _sep.join(_items[:-1])
        filename = _items[-1]

        cancel_music = False
        is_playing = True
        index = 0
        skip_limit = 30

        for frame in progess_bar(
            iterable=wav_frames,
            desc=green(filename),
            total=len(wav_frames),
            unit="frame",
            ncols=130,
            bar_format="{l_bar}%s{bar}%s{r_bar}" % (AnsiCodes.yellow, AnsiCodes.endc)
        ):
            stream.write(frame)

        # keys = set()
        # def key_press(key):
        #     nonlocal is_playing, index, keys, cancel_music

        #     keys.add(key)
        #     ctrl_r = KeyCode(char='\x12')
        #     if ctrl_r in keys:
        #         keys.clear()
        #         index = 0
        #         music_progress_bar.n = 0
        #         music_progress_bar.refresh()


        #     if key == Key.right:
        #         if index + skip_limit < len(wav_frames):
        #             index += skip_limit
        #             music_progress_bar.n = index
        #         music_progress_bar.refresh()

        #     elif key == Key.left:
        #         if index - skip_limit >= 0:
        #             index -= 30
        #             music_progress_bar.n = index
        #         music_progress_bar.refresh()

        #     elif key == Key.backspace:
        #         cancel_music = True


        # def key_release(key):
        #     nonlocal is_playing, index
        #     # stopping music
        #     if key == Key.space:
        #         if stream.is_stopped():
        #             music_progress_bar.refresh()

        #             clearscreen()
        #             print(f"Song: {self.full_name}")
        #             print(f"From: {self.path}\n")

        #             stream.start_stream()
        #             is_playing = True
        #         elif stream.is_active():
        #             music_progress_bar.refresh()
        #             stream.stop_stream()
        #             is_playing = False
        #             print(f"\n{blue('music')} paused from [ {red_bold('space ( _ )')} ]")


        # key_listener = Listener(on_press=key_press, on_release=key_release)
        # key_listener.start()

        # music_progress_bar = progess_bar(
        #     iterable=range(len(wav_frames)),
        #     desc=green(filename),
        #     total=len(wav_frames),
        #     unit="frame",
        #     ncols=130,
        #     bar_format="{l_bar}%s{bar}%s{r_bar}" % (AnsiCodes.yellow, AnsiCodes.endc)
        # )
        # while index < len(wav_frames):
        #     if is_playing:
        #         if cancel_music:
        #             break
        #         # music_progress_bar.refresh()
        #         stream.write(wav_frames[index])
        #         music_progress_bar.update(1)
        #         index += 1
        #         if cancel_music:
        #             break

        #     else:
        #         if cancel_music:
        #             break
        #         sleep(0.01)
        #         if cancel_music:
        #             break

        # music_progress_bar.close()

        # if cancel_music:
        #     print(f"\n{blue('music')} stopped from [ {red_bold('backspace (<-)')} ]")
        #     return "stopped from backspace"

    except KeyboardInterrupt:
        stream.close()
        wf.close()
        p.terminate()

        print(f"\n{blue('music')} stopped from [ {red_bold('KeyboardInterrupt')} ]")
        return "stopped from keyboard_interrupt"

    stream.close()
    wf.close()
    p.terminate()


class Song(object):

    def __init__(self, path, name):
        self.name = name
        self.path = path
        self.full_name = get_filename_plus_extension(path)

    @staticmethod
    def play_song(self, repeat_forever=False):
        clearscreen()
        print(f"Song: {self.full_name}")
        print(f"From: {self.path}\n")
        result = play_wav_with_progress(self.path, self)
        if result == "stopped from keyboard_interrupt":
            return
        else:
            if repeat_forever:
                self.play_song(repeat_forever=True)
            else:
                choice = input("\n[ repeat song ? ]\n[y(es) or <enter> / n(o)]:\n{} ".format(left_arrow_3_green_bold))
                if choice == "y" or choice == "":
                    choice = input("\n[ repeat forever ? ]\n[y(es) or <enter> / n(o)]:\n{} ".format(left_arrow_3_green_bold))
                    if choice == "y" or choice == "":
                        self.play_song(repeat_forever=True)
                    else:
                        self.play_song()


class Playlist(object):

    def __init__(self, database_path):
        self.songs_database = read_json_from_file(database_path)
        if self.songs_database == [] or self.songs_database == {}:
            raise InterruptedError("empty json: {}".format(self.songs_database))

        self.playlist = [Song(song_path, get_file_name(song_path)) for song_path in self.songs_database]


    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.playlist):
                return self.playlist[index]


    def __len__(self):
        return len(self.playlist)


    def __str__(self):
        Playlist_string = "[ Playlist ]:\n"
        for index, song in enumerate(self.playlist, start=1):
            # print(f"\tName: {yellow(song.full_name)}")
            # print(f"\tPath: {blue_underlined(song.path)}")
            Playlist_string += f"[ {index} ]\tName: { yellow(song.full_name)}\n"
            Playlist_string += f"{' ' * len(f'[ {index} ]')}\tPath: {blue_underlined(song.path)}\n\n"
        return Playlist_string



def SongsPlaylist():
    database_path = "songs.json"
    playlist = Playlist(database_path)
    while True:
        try:
            clearscreen()
            print(playlist)
            choice = input("choose your song:\n{} ".format(left_arrow_3_green_bold))
            try:
                choice = int(choice)
            except ValueError:
                continue
            else:
                if 1 <= choice <= len(playlist):
                    playlist[choice - 1].play_song()

        except (KeyboardInterrupt, EOFError):
            try:
                print(f"\n{yellow_bold('Songs Playlist')}\napplication {red_bold('closed')} from [ {red_bold(KeyboardInterrupt.__name__)} ]")
                break
            except KeyboardInterrupt:
                print(f"\n{yellow_bold('Songs Playlist')}\napplication {red_bold('closed')} from [ {red_bold(KeyboardInterrupt.__name__)} ]")
                break

        except BaseException as error:
            print(error)
            print(type(error))
            pauseprogram()


if __name__ == '__main__':
    # generating for the first time from this path
    # songs_folder = "D:/Alexzander__/audio/best-songs-wav"
    #
    # songs = os.listdir(songs_folder)
    # songs = [songs_folder + "/" + song for song in songs]
    # print(songs)
    # write_json_to_file(songs, "songs.json")
    SongsPlaylist()


    r"""
        answer: https://stackoverflow.com/questions/63681770/getting-error-when-using-pynput-with-pyinstaller

        fallback to: pip install pynput==1.6.8

        # we cant make this exe because
        PS C:\Users\dragonfire\Applications\SongsPlaylist> .\SongsPlaylist.exe
        Traceback (most recent call last):
        File "SongsPlaylist.py", line 10, in <module>
            from pynput.keyboard import Listener, Key, KeyCode
        File "c:\applications__\python372\lib\site-packages\PyInstaller\loader\pyimod03_importers.py", line 493, in exec_module
            exec(bytecode, module.__dict__)
        File "pynput\__init__.py", line 40, in <module>
        File "c:\applications__\python372\lib\site-packages\PyInstaller\loader\pyimod03_importers.py", line 493, in exec_module
            exec(bytecode, module.__dict__)
        File "pynput\keyboard\__init__.py", line 31, in <module>
        File "pynput\_util\__init__.py", line 82, in backend
        ImportError
        [18352] Failed to execute script SongsPlaylist
    """
