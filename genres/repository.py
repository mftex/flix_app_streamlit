from login.service import logout
import requests
import streamlit as st


class GenreRepository:

    def __init__(self):
        self.__base_url = 'https://mftex.pythonanywhere.com/api/v1'
        self.__genres_url = f"{self.__base_url}/genres/"
        self.__headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers,
            verify=False
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        if response.status_code == 403:
            return Exception("Sem permissões")
        raise Exception(f"Erro ao obter dados da API. Status code: {response.status_code}")

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            json=genre,
            headers=self.__headers,
            verify=False
        )
        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao criar gênero na API. Status code: {response.status_code}")
