from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests


def get_api_key(line_num):
    try:
        with open('day-046/project-046_spotify_playlist/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    user_year = input(
        "Which year do you want to travel to? "
        "Type the data in this format YYYY-MM-DD:")
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_year}/")

    soup = BeautifulSoup(response.text, 'html.parser')
    song_name_lines = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_name_lines]

    sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=get_api_key(0),
        client_secret=get_api_key(1),
        show_dialog=True,
        cache_path="token.txt",
        username=get_api_key(2), 
    )
)
    user_id = sp.current_user()["id"]


if __name__ == "__main__":
    main()
