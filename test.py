import json 
from Person import Person


object = Person()
object.set_data("/home/abdelbadea/jupy/others/Person.json")
print(object.get_Name())
