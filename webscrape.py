# Scrapes property.com.au for rental property listings

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd


class PropertySearch:

    def __init__(self, city, num_rooms, min_price=50, max_price=5000, min_car=0, min_bathroom=1, surrounding_suburbs=False):
        self.city = city
        self.num_rooms = num_rooms
        self.min_price = min_price
        self.max_price = max_price
        self.min_car = min_car
        self.min_bathroom = min_bathroom
        self.surrounding_suburbs = surrounding_suburbs

    def search_url(self, page_num):

        # url component for selection of studio (i.e. no room) is null
        num_rooms_url = ''
        if self.num_rooms > 0:
            num_rooms_url = f'with-{self.num_rooms}-bedrooms'

        # construct URL based on user parameters
        url = f'https://www.property.com.au/rent/' \
              f'{num_rooms_url}-between-' \
              f'{self.min_price}-{self.max_price}-in-' \
              f'{self.city},+' \
              f'/list-{page_num}?' \
              f'numParkingSpaces={self.min_car}&' \
              f'numBaths={self.min_bathroom}&' \
              f'includeSurrounding={str(self.surrounding_suburbs).lower()}'

        return url

    def results_page(self, page_num):

        response = requests.get(self.search_url(page_num))

        html_soup = BeautifulSoup(response.text)

        address_list = []
        price_list = []
        url_list = []

        if len(html_soup.find_all('div', {'id': 'noresults'})) == 0:

            result_elements = html_soup.find_all('div', {'class': 'resultBody'})

            for result_element in result_elements:

                # store address of individual listing
                address = result_element.find('div', {'class': 'vcard'}).find('a', {'rel': 'listingName'}).getText()
                address_list.append(address)

                # store price of individual listing
                price = result_element.find('div', {'class': 'propertyStats'}).find('span', {'class': 'hidden'}).getText()
                price_list.append(price)

                # store URL of individual listing
                url = result_element.find('div', {'class': 'vcard'}).find('a').get('href')
                url_list.append(url)

        df = pd.DataFrame({'Address': address_list, 'Price': price_list, 'URL': url_list})

        return df

    def results(self):

        # scraps up to page 20
        df = []
        for page_num in range(1, 21):
            df_page_num = self.results_page(page_num)

            df.append(df_page_num)

        df = pd.concat(df).reset_index(drop=True)

        return df

    def results_save(self):
        df = self.results()

        if len(df) > 0:
            df.to_csv(f'rental-listings_{datetime.datetime.now().date()}.csv', index=False)
        else:
            print('No rental listings found that match search preferences. Please adjust preference selections.')

