#home work 2


class User:
    
    
    
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        
    def price_in_pounds(self) :
      return f"{40 - self.age}"     
    def say_hello(self) :
        if self.gender == 'Male':
            return f"Hello Mr {self.fname} {self.lname[0]}."
        
        elif self.gender == 'Female':
            return f"Hello Mrs {self.fname} {self.lname[0]}."       
    def full_details(self):
       return f"{self.say_hello()} {self.price_in_pounds()} Years To Reach 40" 
    
  # Write Class Content

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40