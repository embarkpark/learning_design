### Task

Make sure you install the requirements for this task by running:

```
pip install -r requirements.txt
```

Your task is to fix the bugs in this webscraping project. Do not change the variable 'films' and you should expect a solution where
all 5 movies are written to a film_ratings.csv file in the folder. 


There are 6 errors and this is a difficult project to debug. This will take time and some experience with web scraping will be required. 


### This is a modified version of [utkarshbajaj](https://github.com/utkarshbajaj) code made to introduce bugs.
> Original code from [utkarshbajaj's GitHub](https://github.com/utkarshbajaj/Find-IMDB-Ratings)

### Solution

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Setting up session
s = requests.session()  

# List contaiting all the films for which data has to be scraped from IMDB
films = ['The Godfather', 'Pulp Fiction', 'Scarface', 'Inception', 'Shutter Island', 'Goodwill Hunting', 'Catch me if you Can']

# Lists contaiting web scraped data
names = []
ratings = []
genres = []

for line in films:
    title = line.lower()

    query = "+".join(title.split()) 
    URL = "https://www.imdb.com/search/title/?title=" + query
    # print(URL)
    try: 
        response = s.get(URL)

        #getting contect from IMDB Website
        content = response.content


        soup = BeautifulSoup(response.content, features="html.parser") 
        #searching all films containers found
        containers = soup.find_all("div", class_="lister-item-content")
        rating_bar = containers[0].find_all("div", class_="ratings-bar")
        genre = containers[0].find_all("p", class_="text-muted")
        score = rating_bar[0].find_all("div", class_="inline-block ratings-imdb-rating")

        rating = score[0]['data-value']
        genre = genre[0].find_all("span", class_="genre")[0].text

        names.append(line)
        ratings.append(rating)
        genres.append(genre)


    except Exception:
        print("Try again with valid combination of tile and release year")

#storing in pandas dataframe
df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres}) 

#making csv using pandas
df.to_csv('film_ratings.csv', index=False, encoding='utf-8')