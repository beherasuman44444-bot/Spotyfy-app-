class spotyfyApp:
    def __init__(self):
        self.playlist = []
        self.curret_song = None

    def current_playlist(self,playlist_name):
        self.playlist.append(playlist_name)
        print(f"playlist: {playlist_name} created")
    
    def add_song_to_playlist(self,playlist_name,song):
        if playlist_name in self.playlist:
            print(f"Added {song} to playlist '{playlist_name}'")
        else:
            print(f"playlist {playlist_name} not found")

    def play_song(self,song):
        self.curret_song =song
        print(f"now playing : {song}")

    def show_current_song(self):
        if self.curret_song:
            print(f"currently playing :{self.curret_song}")
        else:
            print("no song is currentlyplaying")

spotyfy = spotyfyApp()

while True:
    print("\nAvailable commands : create playlist,add song,play song,current song,exit")
    command = input("enter a command : ").strip().lower()
    if command == "create playlist":
        playlist_name = input("playlist name: ")
        spotyfy.current_playlist(playlist_name)
    
    elif command == "add song":
        playlist_name = input("playlist name: ")
        song = input("enter a song: ")
        spotyfy.add_song_to_playlist(playlist_name,song)

    elif command == "play song":
        song = input("enter a song: ")
        spotyfy.play_song(song)

    elif command == "current song":
        spotyfy.show_current_song()

    elif command == "exit":
        print("Exiting the spotyfy app. ")

    else:
        print("invalid command , please try again. ")