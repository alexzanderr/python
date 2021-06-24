
from pprint import PrettyPrinter
import json

def EliminateQuotes(string: str):
    return "".join(list(filter(lambda x : (x != "\""), list(string))))

class FamilyMember:
    def __init__(self, family_name, name, birth_date):
        self.family_name = family_name
        self.name = name
        self.fullname = name + " " + family_name
        self.birth_date = birth_date
        self.married = 0
        self.UpdateDetails()
        
    def UpdateDetails(self):
        self.details = {
            "family_name": self.family_name,
            "name": self.name,
            "fullname": self.fullname,
            "birth_date": self.birth_date,
            "married": True if self.married else False
        }
    
    def GetDetails(self):
        return self.details
        
    def __str__(self):
        return "<FamilyMember>\n" + \
               EliminateQuotes(json.dumps(self.details, indent=4)[2:-1]) + \
               "</FamilyMember>\n"
        
def CreateConnection(fm1: FamilyMember, fm2: FamilyMember):
    fm1.married = fm2.married = 1
    fm1.UpdateDetails(); fm2.UpdateDetails()
    
    # pointer to object fm2
    fm1.marriage = fm2
    fm1.connection_details = fm2.GetDetails()
    
    # pointer to object fm1
    fm2.marriage = fm1
    fm2.connection_details = fm1.GetDetails()