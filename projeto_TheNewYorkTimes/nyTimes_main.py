import requests
import json
from date import Data
from artigos import Articles
from livros import Books
from film import Movies


def request(url):
    
    req = requests.get(url)
    json_text = json.loads(req.text)
    return json_text

def prints_questions_date():
    day = str(input("type the day: \n"))
    month = str(input("type the month: \n"))
    year = str(input("type the year: \n"))

    if len(month)<2:month
         return day, "0"+month, year
    else:
        return day,month,year

while(1):

    d = Data(0,0,0)
    #menu
    print("Welcome to The New York Times Emulator!!\n")
    print("1 - View Today's Published Articles" +d.format_date_actual() + ":\n")
    print("2 - View Articles from a particular day:\n")
    print("3 - See the New York Times books Best Sellers:\n")
    print("4 - See Movie Reviews by The New York Times:\n") 

    choice = str(input("Choose the desired option and enjoy! :"))
    
    if choice == "1":
        
        m,y = d.split_date()
        if m[0] == "0": m = m[1]

        request_articles = request(f"https://api.nytimes.com/svc/archive/v1/{y}/{m}.json?api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd")

        articles_actual_date = Articles().show_date(request_articles,d.format_date_actual())

    elif choice == "2":
         
        d,m,y = prints_question_date()
        
        date_formated = Data(d,m,y).format_date()

        request_articles_particular = requisicoes(f"https://api.nytimes.com/svc/archive/v1/{y}/{m}.json?api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd")
        
        article_particular = Articles().show_date(request_api_articles,formated)

    elif choice == "3":
        
        print("1 - Search Best Sellers by book name:\n") 
        print("2 - Search the Best Sellers by author of the book:\n")
        print("3 - Search for Best Sellers according to a certain publication date:\n")
        
        book_choice = str(input("Choose the desired option and have a good reading! :\n"))
        
        if book_choice == "1":

            request_name_book = request(f"https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd")

            name_book = str(input("What's is the name of the book ? "))
            books_name = Books().show_best_sellers_name(request_name_book,name_book)
            
        elif book_choice = "2":
            
            author = str(input("What's is the name of the author ?"))

            request_author_book = request(f"https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?title={author}&api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd")

            books_author = Books().show_best_sellers_name(request_author_book)

        elif book_choice == "3":

            y,m,d = prints_question_date()
            
            d = Data()
            dt = d.format_date(y,m,d)


            request_date_book = request(f"https://api.nytimes.com/svc/books/v3/lists/full-overview.json?published_date={dt}&api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd")

            books_date = Books().show_best_sellers_date(request_date_book)
        else:
            print("Opcao Invalida, saindo ...")
            break

    elif escolha == "4":

        name_movie = str(input("What's is name of the film ? "))
        name_movie = name_movie.replace(" ","%20")
        
        req_movie = request(f"https://api.nytimes.com/svc/movies/v2/reviews/search.json?query={name_movie}&api-key=DgKDLqwPwTbdmJ5DXFPVdgVpMWLsboyd")

        movie = Movies().show_reviews_movies(req_movie)
    else:
        print("Somente numeros sao aceitaveis como escolha")
        break