from actors.service import ActorService
from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid



def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors and 'Sem permissões' not in str(actors):
        st.write("Lista de Atores:")
        actors_df = pd.json_normalize(actors)
        AgGrid(actors_df,
            reload_data=True,
            key='actors_grid',
            show_toolbar=True,)
    elif 'Sem permissões' in str(actors):
        st.warning('Você não tem permissão para visualizar os atores.')
    else:
        st.warning('Nenhum ator encontrado.')

    st.divider()

    st.title('Cadastrar novo ator')
    name = st.text_input('Nome do ator')
    birthday = st.date_input(
        label='Data de nascimento',
        value = datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = ['USA', 'BR']
    nationality = st.selectbox(
        label='Nacionalidade', 
        options=nationality_dropdown
    )
    
    if st.button('Cadastrar'):
        result = actor_service.create_actor(name, birthday, nationality)

        if 'name' in result:
            st.rerun()
        if result['status'] == 'unauthorized':
            st.warning('Você não tem permissão para cadastrar um novo ator. Caso necessário, solicite ao administrador do sistema.')
        else:
            st.warning('Erro ao cadastrar o ator.')