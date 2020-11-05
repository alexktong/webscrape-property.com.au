# Scrapes property.com.au for rental property listings

import requests
from bs4 import BeautifulSoup
import datetime


def main(city, num_rooms, min_price=50, max_price=5000, min_car=0, min_bathroom=1, surrounding_suburbs=False):

    # url component for selection of studio (i.e. no room) is null
    num_rooms_url = ''
    if num_rooms > 0:
        num_rooms_url = f'with-{num_rooms}-bedrooms'

    address_list = []
    price_list = []
    url_list = []

    # scraps up to page 20
    for page_num in range(1, 21):

        # construct URL based on user parameters
        url = f'https://www.property.com.au/rent/' \
              f'{num_rooms_url}-between-' \
              f'{min_price}-{max_price}-in-' \
              f'{city},+' \
              f'/list-{page_num}?' \
              f'numParkingSpaces={min_car}&' \
              f'numBaths={min_bathroom}&' \
              f'includeSurrounding={str(surrounding_suburbs).lower()}'

        response = requests.get(url)

        html_soup = BeautifulSoup(response.text)

        if len(html_soup.find_all('div', {'id': 'noresults'})) == 0:

            result_elements = html_soup.find_all('div', {'class': 'resultBody'})

            for result_element in result_elements:

                # store address of individual listing
                address = result_element.find('div', {'class': 'vcard'}).find('a', {'rel': 'listingName'}).getText()

                # store price of individual listing
                price = result_element.find('div', {'class': 'propertyStats'}).find('span', {'class': 'hidden'}).getText()

                # store URL of individual listing
                url = result_element.find('div', {'class': 'vcard'}).find('a').get('href')

                address_list.append(address)
                price_list.append(price)
                url_list.append(url)

    # store listings in text file with naming convention 'rental-listings_YYYY-MM-DD.txt'
    text_file = open(f'rental-listings_{datetime.datetime.now().date()}.txt', 'w')

    if len(address_list) > 0:

        # rental listing stored in format 'ADDRESS - RENTAL PRICE - URL'
        for ind, result in enumerate(address_list):
            result_full = f'{result} - {price_list[ind]} - {url_list[ind]}'
            text_file.write(result_full + '\n')
    else:
        text_file.write('No rental listings found that match search preferences. Please adjust preference selections.')
    text_file.close()


if __name__ == '__main__':
    main(city='Chatswood', # if irrelevant listings found, try search 'CITY, STATE, POSTCODE' e.g. 'Chatswood, NSW, 2067'.
         num_rooms=1,
         min_price=350,
         max_price=450,
         min_car=0,
         min_bathroom=1,
         surrounding_suburbs=True)