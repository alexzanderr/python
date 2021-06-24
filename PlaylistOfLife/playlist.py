
import json
from core.system import *
import webbrowser, os
from core.aesthetix import *
from core.json_module import *

playlist_path = "PlaylistOfLife.json"

# create the json playlist if not existent 
if not os.path.exists(playlist_path):
    PlaylistOfLifeFromYT = read_json_from_file(playlist_path)

    base_url = "https://www.youtube.com/watch?v={}__pathaylistID = "PLYArvM4aLBU0moPhQSP2KaHPZAH6k6dCd"

    PlaylistOfLife = []
    for index, song in enumerate(PlaylistOfLifeFromYT, start=1):
        songID = song["contentDetails"]["videoId"]
        songNAME = song["snippet"]["title"]
        songURL = base_url.format(songID)
        indexURL = songURL + "&list={}".format(playlistID) + "&index={}".format(index)
        new_song = {
            "id": songID,
            "name": songNAME,
            "song_url": songURL,
            "index_url": indexURL
        }
        PlaylistOfLife.append(new_song)

    write_json_to_file(PlaylistOfLife, playlist_path)
else:
    # navigating through playlist
    PlaylistOfLife = read_json_from_file(playlist_path)
    
    def PrintPlaylist(playlist):
        for index, song in enumerate(playlist, start=1):
            i = ConsoleColoredBold(str(index), "yellow", underlined=1)
            name = ConsoleColoredBold(song["name"], "yellow")
            print("[ {} ]. {}".format(i, name))
        print()
        
    playlist_dimension = len(PlaylistOfLife)
    current_index = None
    exit_option = ConsoleColored("__EXIT__", "red", bold=1)
    
    while 1:
        clearscreen()
        PrintPlaylist(PlaylistOfLife)
        print("[ {} ]. {}".format(playlist_dimension + 1, exit_option))
        
        print("\n\tCurrent Index >>> [ {} ]".format(ConsoleColored(str(current_index), "green", bold=1, underlined=1)))
        if current_index:
            song_name = ConsoleColored(PlaylistOfLife[current_index - 1]["name"], "green", bold=1)
            print("\tCurrently Playing >>> [ {} ]".format(song_name))
            del song_name
        else:
            print("\tno song is playing. :(")
        
        message = ConsoleColored("\n>>> choose", "green", bold=1) + " your action:\n\t"
        action = input(message)
        
        try:
            index = int(action)
            if 1 <= index <= playlist_dimension:
                webbrowser.open(PlaylistOfLife[index - 1]["song_url"])
                current_index = index
            else:
                break
        except ValueError:
            if action == "exit":
                break