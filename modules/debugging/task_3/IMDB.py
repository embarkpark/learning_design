from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Setting up session
s = requests.session()  

# List containing all the films for which data has to be scraped from IMDB
films = ['The Godfather', 'Pulp Fiction', 'Scarface', 'Inception', 'Shutter Island', 'Goodwill Hunting' 'Catch me if you Can']

# Lists containing web scraped data


for line in films:
    names = []
    ratings = []
    genres = []

    title = line.lower()

    query = "+".join(title.split()) 
    URL = "https://www.imdb.com/search/title/?title=" + "query"
    
    # print(URL)
    # print(release)
    try: 
        response = s.get(URL)

        #getting content from IMDB Website
        content = response.content


        soup = BeautifulSoup(response.content, features="html.parser") 
        #searching all films containers found
        containers = soup.find_all("div", class_="lister-item-content")
        rating_bar = containers[0].find_all("div", class_="ratings-bar")
        genre = containers[0].find_all("p", class_="text-muted")
        score = rating_bar[0].find_all("div", class_="inline-block ratings-imdb-rating")

        rating = score[0]['data-value']
        genre = genre[0].find_all("span", class_="genre_").text

        names.append(line)
        ratings.append(rating_bar)
        genres.append(genre)


    except Exception:
        print("Try again with valid combination of tile and release year")

#storing in pandas dataframe
df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres}) 

#making csv using pandas
df.to_csv('film_ratings.csv', index=False, encoding='utf-8')
