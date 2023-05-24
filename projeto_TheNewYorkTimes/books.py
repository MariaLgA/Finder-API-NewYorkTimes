import json
from termcolor import colored
import colorama
from colorama import Fore

class Books:


    def show_best_sellers_name(self,json_name,name_book):
        for i in json_name["results"]:
                print("Title: {}\n Author: {} \n Resume: {} \n\n".format(i["title"],i["author"],i["description"]))

    


    def show_best_sellers_author(self,json_author):
        for i in json_author["results"]:
                print("Title: {}\n Author: {} \n Resume: {} \n\n".format(i["title"], i["author"], i["description"]))
