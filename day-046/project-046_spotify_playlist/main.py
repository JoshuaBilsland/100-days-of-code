from bs4 import BeautifulSoup
import requests


def main():
    user_year = input(
        "Which year do you want to travel to? "
        "Type the data in this format YYYY-MM-DD:")
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_year}/")

    soup = BeautifulSoup(response.text, 'html.parser')
    song_name_lines = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_name_lines]


if __name__ == "__main__":
    main()
