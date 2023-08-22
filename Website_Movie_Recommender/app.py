import streamlit as st
import pickle
import requests
import pandas as pd
from PIL import Image


def get_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=79a849d31e9b9dc4cffd9af2e2e9eada&language=en-US'.format(
            movie_id))
    data = response.json()
    try:
        if (len(data['poster_path']) != 0):
            # st.text(data['poster_path'])
            return "https://image.tmdb.org/t/p/w185" + data['poster_path']
    except:
        return "Poster unavailable"


def recommend(movie):
    movie_ind = movies_list[movies_list['title'].apply(lambda x: x.lower()) == movie.lower()].index[0]
    dist = similar_movies[movie_ind]
    recommend_movies = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:13]

    recommend_list = []
    recommend_list_poster = []
    recommend_movie_id = []
    for i in recommend_movies:
        movie_id = movies_list.iloc[i[0]].id
        # st.write(movies_list['title'][i[0]])
        recommend_list.append(movies_list.iloc[i[0]].title)
        recommend_movie_id.append(movie_id)
        recommend_list_poster.append(get_poster(movie_id))

    return recommend_list, recommend_list_poster, recommend_movie_id


movies_list = pd.read_pickle('movies.pkl')
# pickle.load(open('movies.pkl', 'rb'))

similar_movies = pd.read_pickle('similar.pkl')
# pickle.load(open('similar.pkl', 'rb'))

st.title('Movie Recommendation')

option = st.selectbox(
    'Enter a movie title you like : ',
    movies_list['title'].values)

if st.button('Recommend'):
    st.write('Recommending movies similar to : ' + option )
    titles, posters, ids = recommend(option)
    # st.text(len(titles))
    # st.text(len(posters))
    col1, col2, col3 = st.columns(3, gap="large")
    cols = [col1, col2, col3]

    k = 0
    for j in range(4):
        for i in cols:
            with i:
                st.subheader(titles[k])
                # st.write("[{}]({})".format(titles[k], link1))
                link = "https://www.themoviedb.org/movie/{}-{}".format(ids[k], "-".join(titles[k].lower().split()))
                if posters[k] != "Poster unavailable":
                    # st.image(posters[k], use_column_width="auto")
                    st.markdown("[![Foo]({})]({})".format(posters[k], link))
                else:
                    # image = Image.open('Poster_Unavailable.jpg')
                    # st.image(image, use_column_width="auto")
                    st.markdown("[![Foo](https://i.imgur.com/7c0ZFea.jpg)]({})".format(link))
            k += 1

    # for i in cols:
    #     with i:
    #         st.subheader(titles[k])
    #         st.image(posters[k], use_column_width="auto")
    #     k += 1

    # with col1:
    #     st.text(titles[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(titles[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(titles[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(titles[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(titles[4])
    #     st.image(posters[4])
    # with col6:
    #     st.text(titles[5])
    #     st.image(posters[5])
    # with col7:
    #     st.text(titles[6])
    #     st.image(posters[6])
    # with col8:
    #     st.text(titles[7])
    #     st.image(posters[7])
    # with col9:
    #     st.text(titles[8])
    #     st.image(posters[8])
    # with col10:
    #     st.text(titles[9])
    #     st.image(posters[9])
