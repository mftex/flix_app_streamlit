import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Ação',
    },
    {
        'id': 2,
        'name': 'Comédia',
    },
    {
        'id': 3,
        'name': 'Drama',
    }

]


def show_genres():
    st.write("Lista de Gêneros:")
    
    AgGrid(pd.DataFrame(genres),
           reload_data=True,
           key='genres_grid',
           show_toolbar=True,)

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')