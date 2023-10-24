import numpy as np
import streamlit as st
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import pickle
import pandas as pd
st.title('Hotel Recommendation System')
data=pickle.load(open('hotel_dict.pkl','rb'))
data = pd.DataFrame(data)

def recommend_hotel(location,description):
    description = str(description)
    location = str(location)
    description = description.lower()
    word_tokenize(description)
    stop_words = stopwords.words('english')
    lemm = WordNetLemmatizer()
    filtered = {word for word in description if not word in stop_words}
    filtered_set = set()
    for fs in filtered:
        filtered_set.add(lemm.lemmatize(fs))

    country = data[data['countries']==location.lower()]
    country = country.set_index(np.arange(country.shape[0]))
    list1 = []; list2 = []; cos = [];
    for i in range(country.shape[0]):
        temp_token = word_tokenize(country["Tags"][i])
        temp_set = {word for word in temp_token if not word in stop_words}
        temp2_set = set()
        for n in temp_set:
            temp2_set.add(lemm.lemmatize(n))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    country['similarity']=cos
    country = country.sort_values(by='similarity',ascending=False)
    country.drop_duplicates(subset='Hotel_Name',keep='first', inplace=True)
    country.sort_values('Average_Score',ascending=False, inplace=True)
    country.reset_index(inplace=True)
    return country

datad = pickle.load(open('hotel_dict.pkl','rb'))
datad = pd.DataFrame(datad)
countries_list = datad.countries.unique()

selected_country = st.selectbox('Enter the Country',
                                countries_list)

tags = ['Leisure','Business', 'Couple', 'Solo','Group','Family']
selected_tag = st.selectbox('Enter the purpose of trip',tags)

if st.button('Recommend'):
    n = recommend_hotel(str(selected_country), str(tags))
    n = pd.DataFrame(n)
    n = n.iloc[:5, ]
    n = n[['Hotel_Name','Average_Score','Hotel_Address']]
    st.table(n)

# option = st.selectbox(
#     'Select the country you want to visit',
#     ('UK','Netherlands','France','Italy','spain','Austria')
# )