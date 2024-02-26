import requests
import streamlit as st

def getresponse(uid):
    payload = {'api_key': '2233b77a536cee35ec5b6a78411717ec',
               'url': f'https://api.themoviedb.org/3/movie/{uid}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US' }
    response = requests.get('https://api.scraperapi.com/', params=payload)
    data = response.json()
    return 'https:image.tmdb.org/t/p/w500/' + data['poster_path']

l = []
k = getresponse(3100)
l.append(k)
print(l[0])

st.image('https:image.tmdb.org/t/p/w500//jCyJN1vj8jqJJ0vNw4hDH2KlySO.jpg')

