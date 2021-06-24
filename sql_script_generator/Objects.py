

class Address:
    def __init__(self, country, zipcode, street_name, street_number):
        self.country = country
        self.zipcode = zipcode
        self.street_name = street_name
        self.street_number = street_number

    def __str__(self):
        aobj = "\"AddressObject =>\""   
        content = ",".join([
            aobj,
            f'"{self.country}"',
            f'"{self.zipcode}"',
            f'"{self.street_name}"',
            str(self.street_number)
        ])
        return content
        
        
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        
class Customer:
    def __init__(self, first_name, last_name, email, 
                 customer_type, company_name, phone_number,
                 addressID: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.customer_type = customer_type
        self.company_name = company_name
        self.phone_number = phone_number
        self.AddressID = addressID

    def __str__(self):
        cobj = "\"CustomerObject =>\""
        content = ",".join([
            cobj, 
            self.first_name, 
            self.last_name, 
            f'"{self.email}"', 
            self.customer_type, 
            f'"{self.company_name}"',
            str(self.phone_number),
            str(self.AddressID)
        ])
        return content