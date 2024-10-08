#python -m pip install requests
import requests
import json
import psycopg2
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Optional

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Carrega as variáveis de ambiente do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if not load_dotenv(dotenv_path):
    print("Arquivo .env não foi carregado corretamente.")

# variáveis de ambiente do gateway de pagamento
#TOKEN = os.getenv("TOKEN_KEY")
TOKEN = "test_b025e5770ded38e8daaaf62cb53f8b"
#BASE_URL = os.getenv("BASE_URL")
BASE_URL = "https://api.api-futebol.com.br/v1/"

class FutebolAPIService:
    DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"  # Sem milissegundos e timezone por padrão
    def __init__(self, base_url: str, token: str):
        """
        Inicializa o serviço para enviar pedidos de criação de QRCode de PIX.

        :param base_url: URL base do serviço.
        :param token: Token de autorização.
        """
        self.base_url = self.validate_url(f"{base_url}")
        self.token = token
        self.headers = {
            "accept": "application/json",
            "Authorization": f'Bearer {self.token}',
            "content-Type": "application/json"
        }

    @staticmethod
    def validate_url(uri: str) -> str:
        """Remove barras duplas de uma URI, exceto :// do protocolo."""
        result = []
        i = 0
        while i < len(uri):
            # Verifica se a sequência é '://' e pula para não remover essas barras duplas
            if uri[i:i+3] == "://":
                result.append(uri[i:i+3])
                i += 3
            # Remove barras duplas extras fora do '://'
            elif uri[i:i+2] == "//":
                result.append("/")
                i += 2
            else:
                result.append(uri[i])
                i += 1
        return ''.join(result)
            
    def list_championships(self):
        service_url = self.validate_url(BASE_URL + "campeonatos/")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_championship_by_id(self, championship_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_championship_table_by_id(self, championship_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/tabela")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
    
    def list_championship_artillery_by_id(self, championship_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/artilharia")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
    
    def list_championship_phases_by_id(self, championship_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/fases")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_championship_and_phase_by_id(self, championship_id: str, phase_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/fases/{phase_id}")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
    
    def list_championship_rounds_by_id(self, championship_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/rodadas")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_championship_and_round_by_id(self, championship_id: str, round_id: str):
        #plan_id = SignaturePlan.
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/rodadas/{round_id}")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_live_matches(self):
        service_url = self.validate_url(BASE_URL + "ao-vivo/")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_live_matches_of_championship_by_id(self, championship_id: str):
        service_url = self.validate_url(BASE_URL + f"campeonatos/{championship_id}/partidas")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def return_match_by_id(self, match_id: str):
        service_url = self.validate_url(BASE_URL + f"partidas/{match_id}")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def return_team_by_id(self, team_id: str):
        service_url = self.validate_url(BASE_URL + f"times/{team_id}")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")
        
    def list_next_matches_by_team_id(self, team_id: str):
        service_url = self.validate_url(BASE_URL + f"times/{team_id}/partidas/proximas")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")

    def list_previous_matches_by_team_id(self, team_id: str):
        service_url = self.validate_url(BASE_URL + f"times/{team_id}/partidas/anteriores")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")

    def list_live_matches_by_team_id(self, team_id: str):
        service_url = self.validate_url(BASE_URL + f"times/{team_id}/partidas/ao-vivo")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")

    def return_athlete_by_id(self, athlete_id: str):
        service_url = self.validate_url(BASE_URL + f"atletas/{athlete_id}")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")     

    def return_account_information(self):
        service_url = self.validate_url(BASE_URL + "me/")
        try:
            self.print_request(method="GET", url=service_url, headers=self.headers)

            # Faz a requisição GET (a lógica de requisição continua a mesma)
            response = requests.get(url=service_url, headers=self.headers)
            response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decode error: {e}")  

    @staticmethod
    def print_request(method: str, url: str, headers: dict, json_body: Optional[str] = None):
        """
        Imprime o comando cURL equivalente à requisição HTTP.

        :param method: Método HTTP (POST).
        :param url: URL da requisição.
        :param headers: Cabeçalhos da requisição.
        :param json_body: Corpo da requisição em JSON.
        """
        print("Request")
        print(f"curl --location --request {method} {url} \\")
        for key, value in headers.items():
            print(f"-H '{key}: {value}' \\")
        if(json_body):
            print(f"--data-raw '{json_body}'")
        print()

    @staticmethod
    def print_header(headers: dict, header_name: str, prefix: str = ""):
        """
        Imprime um cabeçalho da requisição.

        :param headers: Cabeçalhos da requisição.
        :param header_name: Nome do cabeçalho a ser impresso.
        :param prefix: Prefixo para o cabeçalho.
        """
        value = headers.get(header_name)
        if value:
            print(f"{prefix}{header_name}: {value}")

    @staticmethod
    def print_response(response: requests.Response):
        """
        Imprime detalhes da resposta HTTP.

        :param response: Resposta da requisição.
        """
        print("Response")
        print(f"Status Code: {response.status_code}")
        print(response.text)
        print()

    # Função fora da Classe para testar a Classe
def exemplo():
    #service = PixOrderService(base_url="https://example.com", token="your_token_here")
    service = FutebolAPIService(base_url=BASE_URL, token=TOKEN)
   
    try:
        # Exemplo de como listar todos os campeonatos
        response_championships = service.list_championships()
        print("Lista de campeonatos: ", response_championships)

        # Exemplo de como buscar informações de um campeonato específico
        championship_id = 14  # ID de exemplo
        response_championship = service.list_championship_by_id(championship_id)
        print(f"Informações do campeonato {championship_id}: ", response_championship)

        # Exemplo de como buscar a tabela de um campeonato específico
        response_table = service.list_championship_table_by_id(championship_id)
        print(f"Tabela do campeonato {championship_id}: ", response_table)

        # Exemplo de como buscar a artilharia de um campeonato específico
        response_artillery = service.list_championship_artillery_by_id(championship_id)
        print(f"Artilharia do campeonato {championship_id}: ", response_artillery)

        # Exemplo de como listar as fases de um campeonato
        response_phases = service.list_championship_phases_by_id(championship_id)
        print(f"Fases do campeonato {championship_id}: ", response_phases)

        # Exemplo de como listar uma fase específica de um campeonato
        phase_id = 32
        response_phase = service.list_championship_and_phase_by_id(championship_id, phase_id)
        print(f"Fase {phase_id} do campeonato {championship_id}: ", response_phase)

        # Exemplo de como listar as rodadas de um campeonato
        response_rounds = service.list_championship_rounds_by_id(championship_id)
        print(f"Rodadas do campeonato {championship_id}: ", response_rounds)

        # Exemplo de como listar uma rodada específica de um campeonato
        round_id = 1
        response_round = service.list_championship_and_round_by_id(championship_id, round_id)
        print(f"Rodada {round_id} do campeonato {championship_id}: ", response_round)

        # Exemplo de como buscar partidas ao vivo
        response_live_matches = service.list_live_matches()
        print("Partidas ao vivo: ", response_live_matches)

        # Exemplo de como listar partidas ao vivo de um campeonato específico
        response_live_matches_by_champ = service.list_live_matches_of_championship_by_id(championship_id)
        print(f"Partidas ao vivo do campeonato {championship_id}: ", response_live_matches_by_champ)

        # Exemplo de como listar uma partida de um campeonato
        match_id = 7034
        response_match = service.return_match_by_id(match_id)
        print(f"Partida do campeonato {championship_id}: ", response_match)

        # Exemplo de como listar um time do campeonato
        team_id = 6
        response_team = service.return_team_by_id(team_id)
        print("Time: ", response_team)

        # Exemplo de como listar as próximas partidas de um time
        response_next_team_matches = service.list_next_matches_by_team_id(team_id)
        print(f"Próximas partidas do time {team_id}: ", response_next_team_matches)

        # Exemplo de como listar as partidas anteriores de um time
        response_previous_team_matches = service.list_previous_matches_by_team_id(team_id)
        print(f"Partidas anteriores do time {team_id}: ", response_previous_team_matches)
        
        # Exemplo de como listar as partidas ao vivo de um time
        response_live_team_matches = service.list_live_matches_by_team_id(team_id)
        print(f"Partidas ao vivo do time {team_id}: ", response_live_team_matches)

        # Exemplo de como retornar um atleta
        athlete_id = 564
        response_athlete = service.return_athlete_by_id(athlete_id)
        print("Atleta: ", response_athlete)
        
        # Exemplo de como retornar informações da sua conta
        response_account = service.return_account_information()
        print(response_account)
        
        #print(response_order)
    except RuntimeError as e:
        print(e)

# Função para calcular a probabilidade de ser campeão ou rebaixado
def calcular_probabilidades(tabela, rodada_atual, total_rodadas=38):
    pontos_por_vitoria = 3
    total_jogos_restantes = total_rodadas - rodada_atual

    # Líder atual
    lider = tabela[0]
    time_lider = lider["time"]["nome_popular"]
    pontos_lider = lider["pontos"]
    
    print(f"Time atual na liderança: {time_lider}, com {pontos_lider} pontos.")
    
    # Zona de rebaixamento (últimos 4 times)
    rebaixados = tabela[-4:]
    print("Times na zona de rebaixamento:")
    for time in rebaixados:
        nome_time = time["time"]["nome_popular"]
        pontos_time = time["pontos"]
        print(f" - {nome_time}: {pontos_time} pontos")

    # Verifica probabilidades para todos os times
    print("\nProbabilidades de ser campeão e rebaixado:")
    for time in tabela:
        nome_time = time["time"]["nome_popular"]
        pontos_time = time["pontos"]
        posicao_time = time["posicao"]
        
        # Pontuação máxima possível deste time nas rodadas restantes (considerando vitórias)
        pontos_maximos_possiveis = pontos_time + (total_jogos_restantes * pontos_por_vitoria)
        
        # Cálculo de probabilidade de ser campeão
        if pontos_maximos_possiveis < pontos_lider:
            prob_campeao = 0.0  # Sem chance de ser campeão
        else:
            prob_campeao = calcular_prob_campeao(total_jogos_restantes, pontos_lider, pontos_time, tabela)

        # Cálculo de probabilidade de ser rebaixado
        ultimo_time_fora_rebaixamento = tabela[-5]  # 16º colocado
        pontos_minimos_para_evitar_rebaixamento = ultimo_time_fora_rebaixamento["pontos"]
        
        if pontos_time >= pontos_minimos_para_evitar_rebaixamento:
            prob_rebaixamento = 0.0  # Sem chance de rebaixamento
        else:
            diferenca_para_rebaixamento = pontos_minimos_para_evitar_rebaixamento - pontos_time
            prob_rebaixamento = calcular_prob_rebaixamento(total_jogos_restantes, diferenca_para_rebaixamento, rebaixados, tabela)

        print(f"{nome_time} (posição {posicao_time}): {prob_campeao:.2f}% de chance de ser campeão, {prob_rebaixamento:.2f}% de chance de ser rebaixado.")

def calcular_prob_campeao(jogos_restantes, pontos_lider, pontos_time, tabela):
    """
    Calcula a probabilidade de um time ser campeão considerando a pontuação máxima.
    """
    max_pontos_time = pontos_time + (jogos_restantes * 3)
    
    # Se o time pode ultrapassar o líder, calcula a probabilidade
    if max_pontos_time >= pontos_lider:
        probabilidade = (max_pontos_time - pontos_lider) / 3 * 50  # 50% de chance ajustada
        return min(probabilidade, 100.0)
    
    return 0.0

def calcular_prob_rebaixamento(jogos_restantes, diferenca_pontos, rebaixados, tabela):
    """
    Calcula a probabilidade de um time ser rebaixado considerando o desempenho dos times abaixo.
    """
    if diferenca_pontos <= 0:
        return 0.0  # Sem chance de rebaixamento

    chance_time_perder = 0.5  # Suposição de 50% de chance de o time perder seus jogos restantes
    probabilidade_rebaixamento = 0.0

    # Verifica quantos times abaixo podem ultrapassar
    for time in rebaixados:
        # Se o time que está na zona de rebaixamento pode ultrapassar
        if time["pontos"] + (jogos_restantes * 3) > tabela[-5]["pontos"]:  # Se ultrapassaria o 16º
            probabilidade_rebaixamento += 25  # Aumento proporcional

    # Aumenta a chance de rebaixamento proporcionalmente à quantidade de pontos necessários
    probabilidade_rebaixamento += (diferenca_pontos / (jogos_restantes * 3)) * 100 * chance_time_perder

    return min(probabilidade_rebaixamento, 100.0)

if __name__ == "__main__":
    #exemplo()

    service = FutebolAPIService(base_url=BASE_URL, token=TOKEN)
    championship_id = 14
    tabela_serie_b = service.list_championship_table_by_id(championship_id)
    campeonato = service.list_championship_by_id(championship_id)
    rodada_atual = campeonato["rodada_atual"]["rodada"]
    #print(rodada_atual["rodada_atual"]["rodada"])
    calcular_probabilidades(tabela=tabela_serie_b, rodada_atual=rodada_atual)