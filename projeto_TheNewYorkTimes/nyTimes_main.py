import requests
import json
from date import Data
from artigos import Articles
from livros import Books
from film import Film

def requisicao_api_articles(mes,ano):
    if mes[0] == "0": mes = mes[1]
    url = f"https://api.nytimes.com/svc/archive/v1/{ano}/{mes}.json?api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd"
    req = requests.get(url)
    #json_text = json.dumps(req.json(),indent=2)
    json_text = json.loads(req.text)
    return json_text

def requisicao_api_books_data(ano,mes,dia):

    d = ano+"-"+mes+"-"+dia
    url = f"https://api.nytimes.com/svc/books/v3/lists/full-overview.json?published_date={d}&api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd"
    req = requests.get(url)
    #json_text = json.dumps(req.json(),indent=2)
    json_text = json.loads(req.text)
    return json_text

def requisicao_api_books_name():

    url = f"https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd"
    req = requests.get(url)
    #json_text = json.dumps(req.json(),indent=2)
    json_text = json.loads(req.text)
    return json_text

def requisicao_api_filmes(name_filme):

    url = f"https://api.nytimes.com/svc/movies/v2/reviews/search.json?query={name_filme}&api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd"
    req = requests.get(url)
    #json_text = json.dumps(req.json(),indent=2)
    json_text = json.loads(req.text)
    return json_text

def prints_pergunta_data():
    dia = str(input("Digite o dia: \n"))
    mes = str(input("Digite o mes: \n"))
    ano = str(input("Digite o ano: \n"))

    if len(mes)<2:
         return dia, "0"+mes, ano
    else:
        return dia,mes, ano

while(1):

    d = Data(0,0,0)
    #menu
    print("Welcome ao to The New York Times Emulator!!\n")
    print("1 - Ver Artigos de hoje " +d.formatar_data_atual() + ":\n") 
    print("2 - Ver Artigos de um determinado dia:\n")
    print("3 - Ver os Livros considerados Best Sellers pelo New York Times:\n")
    print("4 - Ver os Reviews de Filmes pelo The New York Times:\n")

    escolha = str(input("Escolha a opção desejada e aproveite! : "))

    if escolha == "1":
        
        m,a = d.split_data()
        requisicao = requisicao_api_articles(m,a)

        artigos_data_atual = Artigos()
        artigos_data_atual.mostrar_dados(requisicao,d.formatar_data_atual)


    elif escolha == "2":

        d,m,a = prints_pergunta_data()

        data_determinado_dia = Data(d,m,a)
        dt = data_determinado_dia.formatar_data()

        requisicao = requisicao_api_articles(m,a)
        
        artigos = Artigos()
        artigos.mostrar_dados(requisicao,dt)

    elif escolha == "3":
        
        #print("1 - Ver a Listagem completa até a data de hoje de todos os livros considerados Best Sellers:\n")
        print("1 - Pesquisar os Best Sellers de acordo com o nome do livro:\n")\
        print("2 - Pesquisar os Best Sellers de acordo com o nome do livro:\n")
        print("3 - Pesquisar os Best Sellers de acordo com uma determinada data de publicacao:\n")
        
        escolha_livro = str(input("Escolha a opção desejada e aproveite! : \n"))
        
        if escolha_livro == "1":

            requisicao_name_book = requisicao_api_books_name()
            print(requisicao_name_book)
            nome_book = str(input("What's is name of book ? "))
            books_name = Books()
            books_name.mostrar_best_sellers_nome(requisicao_name_book,nome_book)
            
        elif escolha_livro = "2":

        elif escolha_livro == "3":

            a,m,d = prints_pergunta_data()
            requisicao_data_book = requisicao_api_books_data(a,m,d)

            books_data = Books()
            books_data.mostrar_best_sellers_data(requisicao_data_book)

        else:
            print("Opcao Invalida, saindo ...")
            break

    elif escolha == "4":
        name_filme = str(input("What's is name of the film ? "))
        name_filme = name_filme.replace(" ","%20")
        
        req_filme = requisicao_api_filmes(name_filme)

        filme = Film()
        filme.mostrar_reviews_filmes(req_filme)
    else:
        print("Somente numeros sao aceitaveis como escolha")
        break