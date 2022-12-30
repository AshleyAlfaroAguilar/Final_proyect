from datetime import datetime
from dateutil.relativedelta import relativedelta

def Age(birth_date):
    birthdate= datetime.strptime(birth_date,'%Y-%m-%d')
    age = relativedelta(datetime.now(), birthdate)
    return age
    