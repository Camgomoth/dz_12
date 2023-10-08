from collections import UserDict
from datetime import datetime
import pickle
import copy 


class Iterable:
    n_data = list()
    keys = list()
    def __init__(self, N, data):
       self.N = N
       for k,v in data.items():
            self.n_data.append([k,v])
            self.keys.append(k)
       for i in self.keys:
           if i in data.keys():
               data.pop(i)       
    

    def __next__(self):
        if len(self.n_data):
            
            old_data = self.n_data[:self.N]
            for i in old_data:
                for j in self.n_data:
                    if i == j:
                        self.n_data.remove(j)
                
                print(f"{str(i[1])}")
       
    

        
        return f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
    


            
      
        raise StopIteration


class CustomIterator(Iterable):

    def __iter__(self):
        copy_data = copy.copy(book.data)
        return Iterable(self.N, copy_data)


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    

        

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value
    
    @Field.value.setter
    def value(self,value): 
        if value[0].isupper() and value.isalpha():
            self._value = value
        else:
            if not value.isalpha():
                raise ValueError("It's not a name")

            if not value[0].isupper():
                raise ValueError("Name must start with a capital letter")
        

class Phone(Field):     
    def __init__(self,value):
            self.value = value
    
    @Field.value.setter
    def value(self,value):
        if len(value) < 10 or len(value) > 10 or not value.isdigit():
            if not value.isdigit():
              raise ValueError("It's not a phone number")  

            if len(value) < 10 or len(value) > 10:
              raise ValueError("Phone number must be 10 digits long") 
        else:
            self._value = value 
           


 #За моєю умовою, День народження має надходити у форматі "DD.MM" 
class Birthday(Field):
    def __init__(self, value: str):
        self.value = value  
    

    @Field.value.setter
    def value(self,value):
        if value:
            
            if len(str(value)) < 5:
                raise ValueError("Birthday date must be written in format DD.MM") 
            if not str(value)[2] == '.':
                raise ValueError("Birthday date must be written in format DD.MM") 
            if not str(value)[:2].isdigit() and not str(value)[3:].isdigit():
                raise ValueError("Birthday date must contain digits only") 
            
            self._value = value
            



    

class Record:
    def __init__(self, name, birthday=None): 
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)
    
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
            
        return f'Phone has been added succesfully {self.phones}' 
    
    def remove_phone(self,phone):
        for i in self.phones:
            if str(phone) == str(i):
                self.phones.remove(i)
                return f'Phone has been removed succesfully {self.phones}'

       
        
        return f"It is impossible to remove a non-existing phone number, try command 'add_phone'"  

    def edit_phone(self, phone, new_phone):
        for i in self.phones:
            if str(phone) == str(i):
                 indx = self.phones.index(i)
                 self.phones.remove(i)
                 self.phones.insert(indx, Phone(new_phone))
     
                 return f'Phone has been edited succesfully {self.phones}'
        raise ValueError

    def find_phone(self, phone):
        for i in self.phones:
            if str(phone) == str(i):
                    return Phone(phone)
        return 
    
    def days_to_birthday(self):
           
           today = datetime.today().date()
           if self.birthday:
             bd_date = datetime(year = today.year, 
                                month=int(str(self.birthday)[3:]), 
                                day=int(str(Birthday(self.birthday))[0:2]))
            
             
             result = bd_date.date() - today
             if result.days < 0:
                  bd_date = datetime(today.year+1, 
                                    month=int(str(self.birthday)[3:]), 
                                    day=int(str(self.birthday)[0:2]))
                  result = bd_date.date() - today
                 

    
             return f"{result.days} days left\n"
           if not self.birthday:
               return f'No birthday was entered\n'
            


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):

        
    def add_record(self, record):
    
        self.data[record.name.value] = record

        return f'{self.data}'

    
    def find(self, name):
    
        return self.data.get(name)
    


    def iterator(self, N):  
        copy_data = copy.copy(self.data)
        c = CustomIterator(N,copy_data)
    

        for i in c:
            return i
     
      
    
    def delete(self, name):
        for i in self.data.keys():
            if str(i) == name:
                self.data.pop(i)
                return f'Contact has been removed succesfully {self.data}'

        return f"Something went wrong"
    
    
    def serialize(self):
        file_name = 'adress_book.bin'
        with open(file_name, 'wb') as file:
                pickle.dump(self.data, file)
                return 'Session has been successful\n'
     
        
        
    
    def deserialize(self):
        file_name = 'adress_book.bin'
        with open(file_name, 'rb') as file:
                print(pickle.load(file))
                return 'Session has been successful\n'
        
        



    def search(self, string):
        list = []
        for k,v in self.data.items():
            if string in str(k).lower() or string in str(v):
                list.append([f'{(v)}'])
        return list



    


book = AddressBook()

jane_record = Record("Jane", "11.06 ")
jane_record.add_phone("9876543210")
print(jane_record.days_to_birthday())
jane_record.add_phone("1234567890")
book.add_record(jane_record)

john_record = Record("John")
john_record.add_phone("1231231231")
john_record.add_phone("5555555555")   

book.add_record(john_record)

sue_record = Record("Sue")
sue_record.add_phone("0000000000")
sue_record.add_phone("8888888888")   
book.add_record(sue_record)

helen_record = Record("Helen")
helen_record.add_phone("3839308563")
helen_record.add_phone("1111811111")   
book.add_record(helen_record)


print(book.serialize())
print(book.deserialize())

print(book.search('j'))
print(book.search('8'))




