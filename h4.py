class Games:
  # Write Class Content
   def __init__(self, n,price):

    self.name = n
    self.price = price
    
   def show_games(self):

    print(f"I Have One Game Called {self.name}") 



  
    
  

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)
my_game.show_games()
my_games_count.show_games()