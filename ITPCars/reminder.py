
from core.system import *
from core.aesthetix import *
from time import sleep
import json, pprint
from datetime import datetime
from datedelta import datedelta
from emails.functionality import *


automation_account_path = r"emails\AutomationAccount.json"
database_path = r"ITPCars\CarsDatabase.json"
datetime_format = "%d.%m.%Y"

expired_cars_path = r"ITPCars\CarsWillExpire.txt"
remaining_time = 15
#TODO lista cu masini care urmeaza sa expire pe data X pe email
# "din masinile facute la data {data_ITP} urmeaza sa expire: {lista masini} in X zile"

# auto refresh la 1 zi
while True:
    # dict
    automation_account = json.loads(open(automation_account_path).read())
    
    print("loading information from database...")
    # dict
    CarsDatabase = json.loads(open(database_path).read())
    CarsWillExpire = []
    
    for car in CarsDatabase:
        nr_masina = car["numar_masina"]
        data_expirarii_ITP = car["data_ITP"]
        data_expirarii_ITP = datetime.strptime(data_expirarii_ITP, datetime_format) + datedelta(months=car["durata_ITP"])
        
        data_expirarii_ITP_str = data_expirarii_ITP.strftime(datetime_format)
        # print(f"data expirarii pentru ITP-ul masinii cu nr. {nr_masina} expira pe: {data_expirarii_ITP_str}.")
        
        diferenta_zile = (data_expirarii_ITP - datetime.now()).days + 1
        # print("diferenta zile: {}".format(diferenta_zile))
        if diferenta_zile == 15:
            new_car = car.copy()
            new_car.update({"data_expirare_ITP": data_expirarii_ITP_str})
            CarsWillExpire.append(new_car)
            
    if len(CarsWillExpire) != 0:
        subject = "reminder"
        message = "lista cu maisini ale caror ITP urmeaza sa expire in {} zile.\n".format(remaining_time)
        message += "=" * 50
        
        for c in CarsWillExpire:
            message += "\t nr. masina: {}. telefon: {}. data ITP: {}. data expirare ITP: {}.\n".format(c["numar_masina"], c["telefon_detinator"], c["data_ITP"], c["data_expirare_ITP"])
        
        with open(expired_cars_path, "w+", encoding="utf-8") as file:
            file.truncate(0)
            file.write(message)
        
        SendEmail(automation_account["email"], automation_account["password"], "just.python.mail.test@gmail.com", subject, "Aveti atasat un fisier text cu lista masinilor ale caror ITP expira in 15 zile.", files_paths=[expired_cars_path])
        
        SendEmail(automation_account["email"], automation_account["password"], "plesa.carmen@ymail.com", subject, "Aveti atasat un fisier text cu lista masinilor ale caror ITP expira in 15 zile.", files_paths=[expired_cars_path])
    
    print("24 hours pause...")
    sleep(60 * 60 * 24) # 24 hour refresh

print()