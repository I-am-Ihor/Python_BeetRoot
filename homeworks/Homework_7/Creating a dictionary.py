"""

Creating a dictionary.
Create a function called make_country, which takes in a country's name and capital as parameters. 
Then create a dictionary from those two, with 'name' as a key and 'capital' as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended.

"""

def make_country(country_name, capital):
    """ function(country_name, capital) -> dict """
    country_and_capital = {country_name: capital}       # created a new dictionary
    print(country_and_capital)                          # dictionary output

make_country('Ukraine', 'Kyiv')                         # a field for entering a key and value into a dictionary from a function