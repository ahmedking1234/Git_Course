#home work 1
class Game:
    
    def __init__(self, name,developer,year,price) :
  # Write Class Content
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
        
    def price_in_pounds(self) :
      return f"{self.price * 15.6 }  Egyptian Pounds"  
            

game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")



