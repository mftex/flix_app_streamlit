import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService




def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres and 'Sem permissões' not in str(genres):
        st.write("Lista de Gêneros:")
        genres_df = pd.json_normalize(genres)
        AgGrid(genres_df,
            reload_data=True,
            key='genres_grid',
            show_toolbar=True,)
    elif 'Sem permissões' in str(genres):
        st.warning('Você não tem permissão para visualizar os gêneros.')
    else:
        st.warning('Nenhum gênero encontrado.')

    st.divider()

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(name)
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero.')
   