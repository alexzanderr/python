
from random import choice, uniform
import pandas as pd
from urllib.request import urlopen

def Random2DigitNumber():
    digits = list("0123456789")
    shallow = digits.copy()
    shallow.remove('0')
    first = choice(shallow)
    second = choice(digits)
    return first + second

first_names = []
with open("sql_script_generator\\first_names.txt", 'r', encoding='utf-8') as first_names_file:
    line = first_names_file.readline()
    while line != "__EOF__":
        first_names.append(line[:len(line) - 1])
        line = first_names_file.readline()

last_names = []
with open("sql_script_generator\\last_names.txt", 'r', encoding='utf-8') as last_names_file:
    line = last_names_file.readline()
    while line != "__EOF__":
        last_names.append(line[:len(line) - 1])
        line = last_names_file.readline()

emails = []
names_combination = []

for lastName in last_names:
    for firstName in first_names:
        names_combination.append((lastName, firstName))

#for nc in names_combination:
#   print(nc)
#print(len(names_combination))

for comb in names_combination:
    emails.append(comb[0] + "." + comb[1] + Random2DigitNumber() + "@gmail.com")

customer_types = ["Old_Customer", "New_Customer", "Special_Customer"]

company_names = []
companies_path = r'D:\__Alexzander_files__\__computer_science__\pentru_dragosi\sql_script_generator\us_companies.csv'
dataset = pd.read_csv(companies_path)
for i in range(len(dataset['company_name'])):
    company_names.append(dataset['company_name'][i])


for elem in list(company_names):
    if 'Inc' in elem or \
        str(elem).__contains__(',') or \
        str(elem).__contains__('.') or \
        str(elem).__contains__('\'') or \
        elem == "How's My Offer?":
        company_names.remove(elem)

#for cn in company_names:
    #print(cn)



def RandomPhoneNumber():
    calling_code = [
        '+40',
        '+45',
        '+48',
        '+55',
        '+10',
        '+82', 
        '+86',
        '+91',
        '+61',
        '+34' 
    ]
    digits = list("0123456789")
    phone_number = choice(calling_code)
    while len(phone_number) <= 11:
        phone_number += choice(digits)
    return phone_number

phone_numbers = []
for i in range(len(names_combination)):
    phone_numbers.append(RandomPhoneNumber())

#for ph in phone_numbers:
    #print(ph)

# print(len(names_combination))

# this url is forbidden
url = 'https://pkgstore.datahub.io/core/country-list/data_csv/data/d7c9d7cfb42cb69f4422dec222dbbaa8/data_csv.csv'
path = r'D:\__Alexzander_files__\__computer_science__\pentru_dragosi\sql_script_generator\countries.csv'

dataset = pd.read_csv(path)

countries = []
for i in range(len(dataset['Name'])):
    countries.append(dataset['Name'][i])

countries.pop(1)


for c in countries:
    if "'" in c:
        countries.remove(c)

def RandomZipCode():
    digits = list("0123456789")
    zipcode = choice(digits)
    while len(zipcode) < 6:
        zipcode += choice(digits)
    return zipcode

#for c in countries:
#    print(c)


zipcodes = []
for _ in range(len(names_combination)):
    zipcodes.append(RandomZipCode())

#for z in zipcodes:
    #print(z)

street_names = []

with open("sql_script_generator\\street_names.txt", 'r', encoding='utf-8') as file:
    line = file.readline()
    while line != '__EOF__':
        street_names.append(line[line.index('.') + 2 : len(line) - 1])
        line = file.readline()

for street in street_names:
    if "'" in street:
        street_names.remove(street)

#for s in street_names:
    #print(s)

print(len(emails))

department_names = ["DYI Department", "Turnkey Department", "Wholesaler Department"]

street_numbers = []

def RandomStreetNumber():
    return int(uniform(1, 100))

for _ in range(len(names_combination)):
    street_numbers.append(RandomStreetNumber())

#for s in street_numbers:
    #print(s)

"""
    names_combinations => 1764
    emails => 1764
    zipcodes => 1764
    phone => 1764
    street_numbers => 1764

    randomes: 
        customer type => 3 => choice(type)
        company_names => 529 => choice(company_names)
        countries => 248 => choice(countries)
        street_names => 100 => choice(street_names)
        depart_names => 3 => choice(depart_names)
"""
def GenerateCustomersAndDeparts():
    from Objects import Customer, Address, Department

    customers = []
    departments = []

    for i in range(len(names_combination)):
        AddressObject = Address(
            choice(countries), 
            zipcodes[i], 
            choice(street_names),
            street_numbers[i]
        )

        customer = Customer(
            names_combination[i][0],
            names_combination[i][1],
            emails[i],
            choice(customer_types),
            choice(company_names),
            phone_numbers[i],
            AddressObject
        )

        customers.append(customer)

        dep = Department(choice(department_names))
        departments.append(dep)

    return customers, departments

customers, _ = GenerateCustomersAndDeparts()

dataset_path = r"sql_script_generator\customers.csv"
header = 'Counter,InfoAboutCustomer,FirstName,LastName,Email,Type,Company,Phone,InfoAboutAddress,Country,Zipcode,StreetName,StreetNumber\n'

def CreateCSVFile(path):
    with open(path, 'w+', encoding='utf-8') as file:
        # format_ = '0,"CustomerObject =>","Andrew","Alexzander","alexxander18360@gmail.com","Old_Customer","Google","+40770924018","AddressObject =>","Romania","077160","Strada Bateriei","Nr. 49A"'
        file.write(header)
        for i in range(len(customers)):
            # dont forget about departments
            item = f'{i},{customers[i]}\n'
            file.write(item)


def RecreateDataset(path):
    with open(path, 'w+', encoding='utf-8') as file:
        file.truncate(0)
        file.write(header)
        for i in range(len(customers)):
            # dont forget about departments
            item = f'{i},{customers[i]}\n'
            file.write(item)


#for i in range(len(customers)):
    #print(customers[i].phone_number)

customers_csv_path = r'D:\__Alexzander_files__\__computer_science__\pentru_dragosi\sql_script_generator\customers.csv'

def GetDatasetPandas(path):
    dataset = pd.read_csv(customers_csv_path)
    return dataset


#print('=====')
#for c in company_names:
    #print(c)
#print('=====')

#RecreateDataset(customers_csv_path)


# dataset = GetDatasetPandas(customers_csv_path)
# dataset.head(10)