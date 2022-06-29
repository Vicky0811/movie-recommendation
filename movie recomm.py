#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import difflib 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[3]:


#Data collection from kegal


# In[4]:


#loading the data from the  csv file to apandas dataframe
movies_data = pd.read_csv('movies.csv')


# movies_data.head()

# In[5]:


movies_data.head()


# In[6]:


#number of rows and columns
movies_data.shape


# In[7]:


selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)


# In[8]:


#replacing the null values with null string
for feature in selected_features:
    movies_data[feature]=  movies_data[feature].fillna('') 


# In[9]:


#combining all the 5 selected features
combined_features =   movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+" "+  movies_data['director']


# In[10]:


print(combined_features)


# In[11]:


#converting the text data to feature vectors
vectorizer = TfidfVectorizer()


# In[12]:


feature_vectors = vectorizer.fit_transform(combined_features)


# In[13]:


print(feature_vectors)


# In[14]:


#Cosine similarity 
#getting the similarity

similarity = cosine_similarity(feature_vectors)


# In[15]:


print(similarity)


# In[16]:


print(similarity.shape)


# In[17]:


movie_name = input('Enter your favorite movie name: ')


# In[18]:


#Creating a list with all the movie name frome the user
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)


# In[19]:


find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)
print(find_close_match)


# In[ ]:


close_match = find_close_match[0]
print(close_match)


# In[ ]:


#finding the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)


# In[22]:


#getting a list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)


# In[ ]:


len(similarity_score)


# In[ ]:


#sorting the movie based  on their similarity score
sorted_similar_movies = sorted(similarity_score,key = lambda x:x[1],reverse = True)
print(sorted_similar_movies)


# In[ ]:


print('movies suggested for you :  ')
i=1
for  movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if(i<=30):
        print(i,'.',title_from_index)
        i+=1


# In[ ]:


#Movie recommendation system

movie_name = input('Enter your favorite movie name: ')
find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score,key = lambda x:x[1],reverse = True)
print('movies suggested for you :  ')
i=1
for  movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if(i<=90):
        print(i,'.',title_from_index)
        i+=1


# In[ ]:


# movie recommendation system

selected_features = ['genres','keywords','tagline','cast','director']
for feature in selected_features:
    movies_data[feature]=  movies_data[feature].fillna('') 
combined_features =   movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+" "+  movies_data['director']
vectorizer = TfidfVectorizer()
#converting the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)
movie_name = input('Enter your favorite movie name: ')
find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score,key = lambda x:x[1],reverse = True)
print('movies suggested for you :  ')
i=1
for  movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if(i<=30):
        print(i,'.',title_from_index)
        i+=1


# In[ ]:




