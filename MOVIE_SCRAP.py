from bs4 import BeautifulSoup
import requests
import html


response = requests.get('https://www.empireonline.com/movies/features/best-movies-2020/')
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
html_movie = soup.find_all(name="h3", class_="title")
movie_data = [tag.getText() for tag in html_movie[::-1]]

with open('abc.txt', mode='w') as file:
    for movie in movie_data:
        print(movie)
        try:
            file.write(html.unescape(movie))
        except UnicodeEncodeError:
            for i in movie:
                try:
                    file.write(html.unescape(i))
                except UnicodeEncodeError:
                    pass
        finally:
            file.write("\n")
