# webscrape-property.com.au
Python script that webscrapes https://property.com.au for rental property listings.

## How it works
* `city`: String. Specifies the city to search for rental listings. Note that if your city name is common and you wish to be more specific, you can also specify state and postcode e.g. `city='Chatswood, NSW, 2067'`.
* `num_rooms`: Integer. Specifies the number of bedrooms. If you wish to search for studio apartments, specify `num_rooms=0`.
* `min_price`: Integer. Minimum weekly price of rental listings. Lowest permissible value is 50.
* `max_price`: Integer. Maximum weekly price of rental listings. Highest permissible value is 5000.
* `min_car`: Integer,.. Minimum number of car space(s) at rental property.
* `min_bathroom`: Integer. Minimum number of bathroom(s) at rental property.
* `surrounding_suburbs`: Boolean. `surrounding_suburbs=True` if you wish to extend search to surrounding suburbs of search location.

View Jupyter notebook `webscrape.ipynb` for example usage.
