import json
from termcolor import colored
import colorama
from colorama import Fore

class Movies:


    def show_reviews_movies(self,json_movies):
        for i in json_movies["results"]:
            print("Film Name: {}\n Review Name: {}\n Resume: {} \n For more information about this review, acess:\n\n".format(i["display_title"],i["headline"],i["summary_short"],i["link"]["url"]))
