### Overview
This project aims to develop a book recommendation system using collaborative filtering and content-based filtering techniques. The recommendation system suggests books to users based on their preferences and behavior.

#### Dataset
The dataset used in this project contains information about books and user ratings. It includes attributes such as ISBN, book title, author, year of publication, and user ratings. The dataset is preprocessed to filter out users with fewer than 200 ratings and books with fewer than 50 ratings.


### Model Building Concept

***Collaborative Filtering with Singular Value Decomposition (SVD)***

The collaborative filtering approach uses Singular Value Decomposition (SVD) to factorize the user-item rating matrix. Truncated SVD is employed to reduce dimensionality and capture latent features. The resulting matrix provides a low-dimensional representation of users and items, enabling the recommendation of similar items to users based on their preferences.

***Content-Based Filtering***

The content-based filtering approach utilizes the textual features of books, such as author, year of publication, and publisher. A TF-IDF vectorizer is employed to transform the textual features into numerical vectors. Cosine similarity is then computed between books based on their textual features, allowing the system to recommend books that are similar in content to those liked by the user.

***Hybrid Approach***

The hybrid approach combines collaborative filtering with content-based filtering to leverage the strengths of both techniques. In this approach, recommendations from collaborative filtering and content-based filtering are merged to provide more diverse and personalized recommendations to users.

### Built With
Streamlit

Machine learning techniques

scikit-learn

### How to Run
***Prerequisites***

Anaconda or Miniconda installed

***Steps***
1. Clone the repository 
```git clone https://github.com/entbappy/ML-Based-Book-Recommender-System.git```
2. Navigate to the cloned repository:
```cd ML-Based-Book-Recommender-System```
3. Create a conda environment:
```conda create -n venv python=3.7.10 -y```
4. Activate the conda environment:
```conda activate venv```
5. Install the required packages:
```pip install -r requirements.txt```
6. Run the Streamlit app:
```streamlit run application.py```




