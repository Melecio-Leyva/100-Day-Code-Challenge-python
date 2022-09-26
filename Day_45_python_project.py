from bs4 import BeautifulSoup
import requests
# grab url for scraping
URL = ""

# request it via request module
response = requests.get(URL)
# save the website in text format
website_html = response.text
# create a BeautifulSoup instance for the website
soup = BeautifulSoup(website_html, "html.parser")
# grab all the h3 with the class title
all_movie = soup.find_all(name="h3", class_="title")
# make a list comprehension of all the movies
movie_titles = [movie.getText() for movie in all_movie]

# Reverse the list
movies = movie_titles[::-1]
# put the movies in a file.
with open("movies.txt", "w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
