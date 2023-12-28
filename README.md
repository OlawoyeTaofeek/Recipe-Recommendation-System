# Recipe Recommendation System
## Project Overview

This project aims to develop a Recipe Recommendation System by leveraging Data Science techniques, including web scraping, data extraction, transformation, machine learning, and web deployment. The goal is to provide users with personalized recipe suggestions based on the ingredients they have available.

* Scraped over 4000 recipes from [All Recipes](allrecipes.com) and [Jamie Oliver](jamieoliver.com) using python beautiful soup and scrapy.
* Parsed recipe ingredients and created word embeddings using Word2Vec and TF-IDF.
* Created a recipe recommendation system using cosine similarity to measure Euclidean distance between the word embeddings of recipe ingredients.
* Built a client-facing API using Django, and a user-friendly [app](https://share.streamlit.io/jackmleitch/whatscooking-deployment/streamlit.py) with Streamlit.

## Motivation

As a cooking enthusiast and someone who appreciates the joy that comes from creating delicious meals, I believe that cooking is an art that should be accessible to everyone. Unfortunately, there can be certain stereotypes around men and cooking, and I am motivated to break those barriers.

This project aims to make cooking more approachable for men, providing them with the tools and inspiration needed to step into the kitchen with confidence. By creating a Recipe Recommendation System tailored to individual preferences and ingredient availability, the goal is to make the entire cooking experience enjoyable and hassle-free.

## Why Men in the Kitchen?

> Breaking Stereotypes: Cooking is a universal skill, and everyone should feel empowered to explore it. This project challenges stereotypes and encourages men to embrace their culinary creativity.

> Promoting Independence: Knowing how to cook is not just a life skill; it's a form of self-expression. This project seeks to foster independence by enabling men to create delicious meals independently.

> Community Building: Cooking can be a shared experience. By creating a community around this project, men can exchange recipes, tips, and experiences, fostering a sense of camaraderie in the kitchen.

## Code 
**Python Version:** 3.11.6 
**Packages:** pandas, numpy, sklearn, gensim, matplotlib, seaborn, beautifulsoup, scrapy, Django, streamlit, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**You can run this model yourself using my API:**
```
docker pull jackmleitch/whatscooking:API
docker run -p 5000:5000 -d whatscooking:api
```
## Project Workflow

1. Data Collection: Extract recipes, ingredients, and ratings from Jamie Oliver and Allrecipes websites.
2. Data Processing: Clean and transform the data, store it in CSV format for analysis.
3. Machine Learning: Build and train a recommendation model based on user preferences and ingredient availability.
4. Deployment: Develop a Django web application to host the recommendation system and provide a seamless user experience.

## Web Scraping
Built a **web scraper** using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [scrapy]() to scrape over 4000 food recipes from [All Recipes](allrecipes.com) and [Jamie Oliver](jamieoliver.com). For each recipe, I retrieved the following:

* Recipe name 
* Ingredients
* URL
* Rating

## Data Processing
After scraping the data, we needed to parse the ingredients to remove redundant information that would not help distinguish recipes. The **ingredient parser** does the following:
* Lemmatize words to ensure we remove all versions of words, e.g. both pounds and pound
* Removed stopwords 
* Removed cooking measures, e.g. pounds and lbs
* Removed common household items, such as oil and butter 
* Some standard NLP preprocessing: getting rid of punctuation, removing accents, making everything lowercase, getting rid of Unicode, etc.
 
## Model Building
I fed my collection of individual ingredients into a **continuous bag of words Word2Vec** neural network to produce word embeddings. Word2Vec was used because I wanted the text representations to capture distributional similarities between words. In the context of recipe ingredients, Word2vec allowed me to capture similarities between recipe ingredients that are commonly used together. For example, mozzarella cheese which is commonly used when making pizza is most similar to other cheeses and pizza-related ingredients.

In order to build the recipe recommendation system, I needed to represent each ingredient list as a single embedding as this would then allow me to calculate corresponding similarities. **TF-IDF** was used to aggregate embeddings (as opposed to simple averaging) as it gives us better distinguishing power between recipes by favoring unique ingredients.

The recommendation system was built using a **content-based filtering** approach which enables us to recommend recipes to people based on the ingredients the user provides. To measure the similarity between user-given ingredients and recipes **cosine similarity** was used. Spacy and KNN were also trialed but cosine similarity won in terms of performance (it was also the most simple approach). The recommendation model computes the cosine similarity between the inputted ingredient list and all recipes in the corpus. It then outputs the top-N most similar recipes, along with their ingredients and URLs, for the user to choose from.

## Deployment
In this step, I built a **Django API** endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of ingredients and returns the top 5 recommended recipes (along with URLs to the recipe webpage).

I also created and deployed a more user-freindly app using **Streamlit**, which can be accessed [here](https://share.streamlit.io/jackmleitch/whatscooking-deployment/streamlit.py). 


