import json
from termcolor import colored
import colorama
from colorama import Fore

class Books:


    def show_best_sellers_name(self,json_name,name_book):
        for i in json_name["results"]:
            if i["title"] == name_book:
                print("Title: {}\n Author: {} \n Resume: {} \n Book Published Date: {} \n, Book Best-Seller Date: {} \n\n".format(i["title"],i["author"],i["description"],i["published_date"],i["bestsellers_date"]))

    
    def show_best_sellers_data(self,json_date):
        for i in json_date["results"]["lists"]:
               print("Title: {}\n Author: {} \n Resume: {} \n Link to buy this book in Amazon, access: \n\n".format(i["title"],i["author"],i["description"],i["amazon_product_url"]))


    def show_best_sellers_name(json_author):
        for i in json_author["results"]:
                print("Title: {}\n Author: {} \n Resume: {} \n Book Published Date: {} \n, Book Best-Seller Date: {} \n\n".format(i["title"],i["author"],i["description"],i["published_date"],i["bestsellers_date"]))
