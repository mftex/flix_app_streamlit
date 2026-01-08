import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Tom Ford',
    },
    {
        'id': 2,
        'name': 'Tom Hanks',
    },
    {
        'id': 3,
        'name': 'Marcelo',
    }

]


def show_actors():
    st.write("Lista de Ators:")
    
    AgGrid(pd.DataFrame(actors),
           reload_data=True,
           key='actors_grid',
           show_toolbar=True,)

    st.title('Cadastrar novo ator')
    name = st.text_input('Nome do ator')
    if st.button('Cadastrar'):
        st.success(f'Ator "{name}" cadastrado com sucesso!')