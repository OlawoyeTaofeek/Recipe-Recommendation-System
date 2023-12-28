# Import the required libraries 
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

# Extracting the Data from the JAMIE OLIVER RECIPE Webiste

url = "https://www.jamieoliver.com/recipes/category/course/mains/"
try: 
    source = requests.get(url)
    # print(source.status_code)
    soup = BeautifulSoup(source.text, "html.parser")
except Exception as e:
    print(e)


links = []
# Find the div with a specific class
div_class = soup.find_all('div', class_='recipe-block')
for div in div_class:
    anchor_tag = div.find('a')
    if anchor_tag:
        href_attribute = anchor_tag.get('href')
        links.append(href_attribute)
    else:
        print("No anchor tag found within the div.")

# print(links[:20])

# Since all elements in the links list are links, we will be making them a link by adding "https://www.jamieoliver.com/"

new_links = []
for link in links:
    element_link = "https://www.jamieoliver.com" + link
    new_links.append(element_link)

# print(new_links[:20])


# So now lets extract informations from all the links in the list
# Let's take one of the link as reference then generalize

# url = new_links[0]
# try: 
#    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#    Recipe_name = soup.find("h1").text
#    print(Recipe_name)
# except Exception as e:
#     print(e)

# recipe_names = []
# for link in new_links[:10]:
#     try: 
#         soup = BeautifulSoup(requests.get(link).content, 'html.parser')
#         Recipe_name = soup.find("h1").text
#         recipe_names.append(Recipe_name)
#     except Exception as e:
#             print(e)
# print(recipe_names)

ingredients_extract = soup.find_all("ul", class_="ingred-list")
# print(ingredients)


ingredients = []
for list in ingredients_extract:
    li_tags = list.find_all("li")
    for li in li_tags:
        # print(li.text)
        ingr = " ".join(li.text.split())
        ingredients.append(ingr)
# print(ingredients)



class JamieOliverScraper:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        self.recipe_links = []

    def extract_recipe_links(self):
        """Extract recipe links from the main page."""
        recipe_blocks = self.soup.find_all('div', class_='recipe-block')
        for block in recipe_blocks:
            anchor_tag = block.find('a')
            if anchor_tag:
                href_attribute = anchor_tag.get('href')
                self.recipe_links.append("https://www.jamieoliver.com" + href_attribute)
        return self.recipe_links

    def extract_ingredients(self, recipe_url):
        """Extract ingredients from a recipe page."""
        try:
            soup = BeautifulSoup(requests.get(recipe_url).content, 'html.parser')
            ingredients_extract = soup.find_all("ul", class_="ingred-list")
            ingredients = []
            for ingred_list in ingredients_extract:
                li_tags = ingred_list.find_all("li")
                for li in li_tags:
                    ingr = " ".join(li.text.split())
                    ingredients.append(ingr)
            return ingredients
        except Exception as e:
            print(f"Error extracting ingredients from {recipe_url}: {e}")
            return np.nan
    
    def extract_recipe_name(self, recipe_url):
        """Extrac recipe name from a recipe page."""
        try:
            soup = BeautifulSoup(requests.get(recipe_url).content, 'html.parser')
            Recipe_extract = soup.find("h1").text
            recipe_names = []
            recipe_names.append(Recipe_extract)
            return recipe_names
        except Exception as e:
            print(f"Error extracting ingredients from {recipe_url}: {e}")
            return np.nan
        
    def extract_cooking_time(self):
        pass

    def extract_difficulty_level(self):
        pass

    def extract_people_served(self):
        pass
        

    def dump_into_json_and_csv(self):
        """Extract all the above data and convert them into json so as to be load into DataFrame 
        and then converted into CSV file
        """
        pass

# Example usage:TR
jamie_scraper = JamieOliverScraper("https://www.jamieoliver.com/recipes/category/course/mains/")
jamie_scraper.extract_recipe_links()


for recipe_link in jamie_scraper.recipe_links:
    ingredients = jamie_scraper.extract_ingredients(recipe_link)
    recipe_names = jamie_scraper.extract_recipe_name(recipe_link)
    print(f"Ingredients for {recipe_link}:\n{ingredients}\n")
    # print(f"The recipe_name for {recipe_link}:\n{recipe_names}")


































































































































































