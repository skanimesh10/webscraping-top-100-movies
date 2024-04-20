import requests
from bs4 import BeautifulSoup

URl = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URl)
webpage_data = response.text
soup = BeautifulSoup(webpage_data, "html.parser")
get_movies = soup.find_all(name='h3', class_="listicleItem_listicle-item__title__BfenH")
all_movies = []
for movies in get_movies:
    all_movies.append(movies.text)

movie_list = all_movies[::-1]

for i in movie_list:
    with open("movie.txt", 'a') as file:
        file.write(f"{i}\n")
