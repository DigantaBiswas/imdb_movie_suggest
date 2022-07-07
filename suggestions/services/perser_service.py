from random import randint

from bs4 import BeautifulSoup
from requests import get


class ImdbWebParser:
    def generate_random_page_number(self):
        initial = 1
        interval = 50
        x = randint(0, 10)
        random_page = interval * x + initial
        return str(random_page)

    def generate_url(self, tv_movie, release_date_from, release_date_to, user_rating_from, user_rating_to, genre):
        url = 'https://www.imdb.com/search/title/?title_type=' + tv_movie + '&release_date=' + release_date_from + \
              ',' + release_date_to + '&user_rating=' + user_rating_from + ',' + user_rating_to + '&genres=' + genre + \
              '&sort=num_votes,desc' + '&page=' + '&start=' + self.generate_random_page_number() + '&ref_=adv_nxt'
        return url

    def get_movie(self,  tv_movie, release_date_from, release_date_to, user_rating_from, user_rating_to, genre):
        url = self.generate_url(tv_movie, release_date_from, release_date_to, user_rating_from,
                                           user_rating_to, genre)

        response = get(url)

        page_html = BeautifulSoup(response.text, 'html.parser')
        movie_container = page_html.find_all('div', class_='lister-item mode-advanced')
        return movie_container
