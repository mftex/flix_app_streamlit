from actors.service import ActorService
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
    birthday = st.date_input('Data de nascimento')
    nationality = st.selectbox('Nacionalidade', options=['USA', 'BR'])
    
    if st.button('Cadastrar'):
        result = actor_service.create_actor(name, birthday, nationality)

        if result['status'] == 'success':
            st.rerun()
        if result['status'] == 'unauthorized':
            st.warning('Você não tem permissão para cadastrar um novo ator. Caso necessário, solicite ao administrador do sistema.')
        else:
            st.warning('Erro ao cadastrar o ator.')