import json
from termcolor import colored
import colorama
from colorama import Fore

class Articles:


    def split_date_json(self,date):
        split_date = data.split("T")
        return split_date[0]

    def show_datas(self,json_articles,date):
        for i in json_articles["response"]["docs"]:
            if self.split_data_json(i["pub_date"]) == date:
                print("Article Title: {}\n Article Resume: {} \n Article Author: {} \n Article Published Date: {} \n, Article Type: {} \n, For more information about the Article, access: {} \n\n".format(i["abstract"],i["lead_paragraph"],i["byline"]["original"],i["pub_date"],i["type_of_material"],i["web_url"]))