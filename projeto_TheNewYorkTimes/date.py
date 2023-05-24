from datetime import date

class Date:

    def format_date_actual(self):
        return "{}/{}/{}".format(date.today().day,date.today().month,date.today().year)
    
    def format_date(self,year,month,day):
        return "{}-{}-{}".format(year,month,day)

    def format_actual_2_date(self):
        return "{}-{}-{}".format(date.today().year,date.today().month,date.today().day)

    def split_date(self):
        return "{}".format(date.today().month),"{}".format(date.today().year)
