import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic',
    },
    {
        'id': 2,
        'name': 'Mercenários',
    },
    {
        'id': 3,
        'name': 'De volta para o futuro',
    }

]


def show_movies():
    st.write("Lista de Filmes:")
    
    AgGrid(pd.DataFrame(movies),
           reload_data=True,
           key='movies_grid',
           show_toolbar=True,)
