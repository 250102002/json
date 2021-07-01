import json 
class Person : 
    def __init__(self,Name="None",Mobile=0,Boolean=False,Pets=[],Address={}) -> None:
        self.__Name = Name
        self.__Mobile = Mobile
        self.__Boolean = Boolean 
        self.__Pets =Pets
        self.__Address = Address
    



    def set_Name(self,name):
        self.__Name = name
    def set_Mobile(self,Mobile):
        self.__Mobile = Mobile
    def set_Boolean(self,bool):
        self.__Boolean=bool 
    def set_Pets(self,pet):
        self.__Pets=pet
    def set_Address(self,address):
        self.__Address = address
    
    def set_data(self,js_file):
        with open(js_file) as file :
            data = json.load(file)
            self.set_Name(data["Name"])
            self.set_Mobile(data["Mobile"])
            self.set_Boolean(data["Boolean "])
            self.set_Pets(data["Pets"])
            self.set_Address(data["Address"])
    

    def get_Name(self):
        return self.__Name 
    def get_Mobile(self):
        return self.__Mobile
    def get_Boolean(self):
        return self.__Boolean
    def get_Pets():
        return self.__Pets
    def get_Address(self):
        return self.__Address
    


