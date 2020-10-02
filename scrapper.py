import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://www.imdb.com/list/ls021078225/"

content = requests.get(url).text

soup = BeautifulSoup(content,'html.parser')

name = []
year = []
rating = []
genre = []
run_time = []

movies = soup.find_all('div',attrs={'class':'lister-item mode-detail'})

for movie in movies:
	name.append(movie.h3.a.text)
	year.append(movie.find('span', attrs={'class':'lister-item-year text-muted unbold'}).text)
	rating.append(movie.find('span', attrs={'class':'ipl-rating-star__rating'}).text)
	genre.append(movie.find('span', attrs={'class':'genre'}).text)
	run_time.append(movie.find('span',attrs={'class':'runtime'}).text)


top_movies = pd.DataFrame({
	'movie':name,
	'year':year,
	'rating':rating,
	'genre':genre,
	'runtime':run_time
	})
top_movies.to_csv("Top_100_Movies_2010_2019", index=False, header=False)

