import datetime
import random

from bs4 import BeautifulSoup
from django.shortcuts import render
from requests import get

# Create your views here.
from suggestions.services.perser_service import ImdbWebParser


def home(request):
    return render(request, 'suggestions/movie_home.html')


def suggestion(request):
    if request.method == 'GET':
        release_date_from = request.GET['release_date_from'] if request.GET['release_date_from'] \
            else (datetime.datetime.now() - datetime.timedelta(days=3*365)).strftime('%Y-%m-%d')

        release_date_to = request.GET['release_date_to'] if request.GET['release_date_to'] \
            else datetime.datetime.now().strftime('%Y-%m-%d')

        user_rating_from = request.GET['user_rating_from'] if request.GET['user_rating_from'] else "5"
        user_rating_to = request.GET['user_rating_to'] if request.GET['user_rating_to'] else "10"
        tv_movie = 'tv_movie'

        genre = request.GET['genre']

        success = False
        retry_count = 0
        while not success and retry_count < 10:
            try:
                movie_container = ImdbWebParser().get_movie(tv_movie, release_date_from, release_date_to,
                                                            user_rating_from,
                                                            user_rating_to, genre)
                suggested_movie = random.choice(movie_container)
                success = True
            except IndexError:
                retry_count += 1
                print(retry_count)

        movie_name = suggested_movie.h3.a.text
        movie_rating = float(suggested_movie.strong.text)
        movie_votes = suggested_movie.find('span', attrs={'name': 'nv'})['data-value']
        about_movie = suggested_movie.find('span', attrs={'class': 'genre'}).text

        main_page = suggested_movie.h3.a['href']
        main_page = "http://www.imdb.com/" + main_page
        main_response = get(main_page)
        main_html = BeautifulSoup(main_response.text, 'html.parser')

        image = main_html.find('img', class_='ipc-image')["src"]
        summary = main_html.find('span', class_='kgphFu').text

        context = [
            movie_name,
            movie_rating,
            movie_votes,
            about_movie,
            image,
            summary
        ]

        # print(len(movie_container))
        # # print(image)
        # # print(img_trailer)
        # # print(release_date_from)
        # # print(release_date_to)
        # # print(genre)
        # # print(main_page)

        # print(user_rating_from)
        # print(user_rating_to)
        # print(genre)
        # print(release_date_from)
        # print(release_date_to)
        # print(video)

        return render(request, 'suggestions/movie_home.html', {'context': context})

# url = 'https://www.imdb.com/search/title?title_type=tv_movie&release_date='\
# +release_date_from+','\
# +release_date_to+\
# '&user_rating='+user_rating_from+','\
# +user_rating_to+\
# '&genres='+genre+\
# '&sort=num_votes,desc&page='+str(1)
