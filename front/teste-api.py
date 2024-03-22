import requests

def buscar_dados_receita(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)

    # Verifica se a resposta foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Retorna os dados em formato JSON
        return response.json()
    else:
        # Se a resposta não foi bem-sucedida, imprime o código de status e retorna None
        print(f'Erro na requisição: {response.status_code}')
        return None

# Exemplo de uso
cnpj = '83891283000136'
dados_receita = buscar_dados_receita(cnpj)
if dados_receita:
    print(dados_receita['tipo'])
else:
    print('Falha ao buscar dados da Receita Federal.')
