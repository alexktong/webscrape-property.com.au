# webscrape-property.com.au

### **PropertySearch(*city='Chatswood'*, *num_rooms=0*, *min_price=300*, *max_price=400*, *min_car=1*, *surrounding_suburbs=False*)**

Python script that webscrapes https://property.com.au for rental property listings.

**Options**

`city` : *string* Name of suburb. If the suburb name is common, state and postcode can also be specified e.g. `city='Chatswood, NSW, 2067'`

`num_rooms` : *integer* Number of bedrooms. For studio apartments, specify (0).

`min_price` : *integer* Minimum weekly price of rental listings. Default (50).

`max_price` : *integer* Maximum weekly price of rental listings. Default (5000).

`min_car` : *integer* Minimum carspace(s) at rental property. Default (0).

`min_bathroom` : *integer* Minimum bathroom(s) at rental property. Default (1).

`surrounding_suburbs` : *boolean* Exclude search to surrounding suburbs. Default False.

## How it works
View Jupyter notebook `webscrape.ipynb` for example usage.