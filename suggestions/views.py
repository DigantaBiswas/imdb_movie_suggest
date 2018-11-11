import random

from bs4 import BeautifulSoup
from time import time, sleep
from random import randint
from requests import get
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 

# Create your views here.
def home(request):
	return render(request,'suggestions/movie_home.html')


def suggestion(request):

	if request.method ==  'GET':
		release_date_from = request.GET['release_date_from']
		release_date_to = request.GET['release_date_to']

		user_rating_from = request.GET['user_rating_from']
		user_rating_to = request.GET['user_rating_to']

		genre = request.GET['genre']

		url = 'https://www.imdb.com/search/title?/title_type=tv_movie&release_date='+release_date_from+','+release_date_to+'&user_rating='+user_rating_from+','+user_rating_to+'&genres='+genre+'&sort=num_votes,desc'+'&page='+str(randint(1,5))
		response = get(url)

		page_html = BeautifulSoup(response.text, 'html.parser')
		movie_container = page_html.find_all('div', class_='lister-item mode-advanced')

		suggested_movie = random.choice(movie_container)
		movie_name = suggested_movie.h3.a.text
		movie_rating = float(suggested_movie.strong.text)
		movie_votes = suggested_movie.find('span', attrs = {'name':'nv'})['data-value']
		about_movie = suggested_movie.find('span', attrs = {'class':'genre'}).text

		main_page = suggested_movie.h3.a['href']
		main_page = "http://www.imdb.com/"+main_page
		main_response = get(main_page)
		main_html = BeautifulSoup(main_response.text, 'html.parser')

		img_trailer = main_html.find('div', class_='poster')
		image = img_trailer.find('a')
		image = image.img['src']

		# image = suggested_movie.find('img')
		# image = image['src']
		summary = main_html.find('div', class_='summary_text')
		summary =summary.text


		context = [
		movie_name,
		movie_rating,
		movie_votes,
		about_movie,
		image,
		summary
		]

		
		print(len(movie_container))
		# print(image)
		# print(img_trailer)
		# print(release_date_from)
		# print(release_date_to)
		# print(genre)
		# print(main_page)

		print(user_rating_from)
		print(user_rating_to)
		print(genre)
		print(release_date_from)
		print(release_date_to)


		return render(request, 'suggestions/movie_home.html', {'context':context})







# url = 'https://www.imdb.com/search/title?title_type=tv_movie&release_date='\
# +release_date_from+','\
# +release_date_to+\
# '&user_rating='+user_rating_from+','\
# +user_rating_to+\
# '&genres='+genre+\
# '&sort=num_votes,desc&page='+str(1)