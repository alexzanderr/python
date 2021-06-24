
from dataset_generator import *

# print(customers[0])


"""
INSERT INTO Address
    ("Country", "Zipcode", "StreetName", "StreetNumber")
VALUES
    ('test', 'test', 'test', 'test'),
    ('test', 'test', 'test', 'test'),
    ('test', 'test', 'test', 'test'),
"""

"""
INSERT INTO Customer 
    ("FirstName", "LastName", "Email", "Type", "CompanyName", "Phone", "AddressID")
VALUES
    ('sadf', 'asdf', 'asdf', 'asdf', 'asdf', 'asdf', 1),
    ('sadf', 'asdf', 'asdf', 'asdf', 'asdf', 'asdf', 2),
    ('sadf', 'asdf', 'asdf', 'asdf', 'asdf', 'asdf', 3)
"""

# here we create the commands
insert_customer = 'INSERT INTO Customer\n'
insert_customer += '\t("FirstName", "LastName", "Email", "Type", "CompanyName", "Phone", "AddressID")\n'
insert_customer += 'VALUES\n'

insert_address = 'INSERT INTO Address\n'
insert_address += '\t("Country", "Zipcode", "StreetName", "StreetNumber")\n'
insert_address += 'VALUES\n'

# after here we insert the lines

from copy import deepcopy
usable_insert_customer = deepcopy(insert_customer)
usable_insert_address = deepcopy(insert_address)

insert_address_commands = []
insert_customer_commands = []

AddressIDCounter = 1
counter = 0
for i in range(len(customers)):
    
    AddressObject = customers[i].AddressID
    CustomerObject = customers[i]

    if counter == 99:
        insert_address_line = f"\t('{AddressObject.country}', '{AddressObject.zipcode}', '{AddressObject.street_name}', {AddressObject.street_number})\n"
        insert_customer_line = f"\t('{CustomerObject.first_name}', '{CustomerObject.last_name}', '{CustomerObject.email}', '{CustomerObject.customer_type}', '{CustomerObject.company_name}', '{CustomerObject.phone_number}', {AddressIDCounter})\n"
    else:
        insert_address_line = f"\t('{AddressObject.country}', '{AddressObject.zipcode}', '{AddressObject.street_name}', {AddressObject.street_number}),\n"
        insert_customer_line = f"\t('{CustomerObject.first_name}', '{CustomerObject.last_name}', '{CustomerObject.email}', '{CustomerObject.customer_type}', '{CustomerObject.company_name}', '{CustomerObject.phone_number}', {AddressIDCounter}),\n"

    usable_insert_address += insert_address_line
    usable_insert_customer += insert_customer_line

    counter += 1
    if counter == 100:
        insert_address_commands.append(usable_insert_address)
        insert_customer_commands.append(usable_insert_customer)

        usable_insert_customer = deepcopy(insert_customer)
        usable_insert_address = deepcopy(insert_address)

        counter = 0

    AddressIDCounter += 1

# if the counter didnt got all the remaining commands
if counter < 100:
    item = usable_insert_address[: len(usable_insert_address) - 2] + "\n"
    insert_address_commands.append(item)
    item = usable_insert_customer[: len(usable_insert_customer) - 2] + "\n"
    insert_customer_commands.append(item)

# pentru primele 17 sunt 100 de linii pentru values
# pentru a 18-a sunt 63 de linii pentru values

def DisplayCommands():
    for i in range(len(insert_address_commands)):
        print('=' * 100)
        print(insert_address_commands[i])
        print('=' * 100)

    print("\n\n\n")

    for i in range(len(insert_customer_commands)):
        print('=' * 100)
        print(insert_customer_commands[i])
        print('=' * 100)


print(len(insert_address_commands))
print(len(insert_customer_commands))

def WriteInSQLScript(path, commands):
    with open(path, 'w+', encoding='utf-8') as file:
        file.truncate(0)
        for command in commands:
            file.write(command + "\n")


sql_addresses_path = r'D:\__Alexzander_files__\__computer_science__\pentru_dragosi\sql_script_generator\insert_addresses.sql'
sql_customers_path = r'D:\__Alexzander_files__\__computer_science__\pentru_dragosi\sql_script_generator\insert_customers.sql'

WriteInSQLScript(sql_addresses_path, insert_address_commands)
WriteInSQLScript(sql_customers_path, insert_customer_commands)
