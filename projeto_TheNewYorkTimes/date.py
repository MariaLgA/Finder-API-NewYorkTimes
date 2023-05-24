from datetime import date

class Date:

    def __init__(self,day,month,year):
        self.day = day
        self.month = month 
        self.year = year

    def format_date_actual(self):
        return "{}/{}/{}".format(date.today().day,date.today().month,date.today().year)

    def format_date(self):
        return "{}-{}-{}".format(self.year,self.month,self.day)
    
    def split_date(self):
        return "{}".format(date.today().month),"{}".format(date.today().year)
