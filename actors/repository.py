from login.service import logout
import requests
import streamlit as st


class ActorRepository:

    def __init__(self):
        self.__base_url = 'https://mftex.pythonanywhere.com/api/v1'
        self.__actors_url = f"{self.__base_url}/actors/"
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url, 
            headers=self.__headers,
            verify=False
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        if response.status_code == 403:
            raise Exception("Sem permissões")
        raise Exception(f"Erro ao obter dados da API. Status code: {response.status_code}")
    
    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            json=actor,
            headers=self.__headers,
            verify=False
        )
        if response.status_code == 201:
            print(response.json())
            return response.json()
            
        if response.status_code == 401:
            logout()
            return None
        
        if response.status_code == 403:
            return {'status': 'unauthorized'}

        raise Exception(f"Erro ao criar ator na API. Status code: {response.status_code}")