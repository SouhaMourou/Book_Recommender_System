import pickle 
import streamlit as st 
import numpy as np
import pandas as pd

st.header('Book Recommender System')

# Load pickled objects
model = pickle.load(open('artifacts/SVD/svd_model.pkl', 'rb'))
book_name = pickle.load(open('artifacts/SVD/book_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/SVD/final_rating.pkl', 'rb'))
book_svd = pickle.load(open('artifacts/SVD/book_svd.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/SVD/book_pivot.pkl', 'rb'))  

# Function to fetch poster URLs and return recommendations
def recommend_book_svd(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    similarities = np.dot(book_svd, book_svd[book_id])
    closest = np.argsort(similarities)[-8:-1]
    recommended_books = [book_pivot.index[i] for i in closest]
    
    # Fetch poster URLs
    poster_url = []
    for name in recommended_books:
        idx = np.where(final_rating['Title'] == name)[0][0]
        url = final_rating.iloc[idx]['Image_url']
        poster_url.append(url)
    
    return recommended_books, poster_url

# Streamlit UI
selected_books = st.selectbox('Select a book', book_name)

if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_book_svd(selected_books)
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    for i, (book, url) in enumerate(zip(recommendation_books, poster_url)):
        with locals()[f'col{i+1}']:
            st.write(book)
            st.image(url)


# Search functionality
search_query = st.text_input('Search for a book', placeholder='Enter book title')
filtered_books = [book for book in book_name if search_query.lower() in book.lower()]

if filtered_books:
    st.write("Search Results:")
    for book in filtered_books:
        st.write(book)
else:
    st.write("No results found.")

