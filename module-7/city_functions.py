# Alisa Steensen
# Module 7.2

# Function that takes 2 parameters initially, then is changed to display language and population as options

def city_country(city_name, country, language=None, population=None):
    """ Returns a string in the format 'City, Country, Language and Population is optional. """

    # For optional population and language
    if population is not None and language is not None:
        return f"{city_name.title()}, {country.title()} - population {population}, {language.title()}"
    # Optionaal population
    elif population is not None:
        return f"{city_name.title()}, {country.title()} - population {population}"
    # Optional language
    elif language is not None:
        return f"{city_name.title()}, {country.title()}, language {language.title()}"
    else:
        return f"{city_name.title()}, {country.title()}"

# Output
print(city_country("santiago", "chile", "Spanish", 5000000))  # Output: Santiago, Chile, 5000000, Spanish
print(city_country("paris", "france", population=6000000))    # Output: Paris, France, 6000000
print(city_country("tokyo", "japan"))     # Output: Tokyo, Japan