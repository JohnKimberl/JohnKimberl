from tinker import
import random
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE= 50
BODY_PARTS= 3
SNAKE_COLOR= "00F#00"
FOOD_COLOR= "#FF0000"
BACKGROUND_COLOR= "000000"


Class Snake:
  def __init__(self, food, game, property):
    self.food=food
    self.game=game
    self.property=property
my_snake = Snake(food="apple", game="arcade", property="green")

Class Food:
def next_turn():


def change_direction(new_direction):

def check_collisions():



def gameover():
window= TK()
window.title("Snake Game")
score = 0
direction= 'down'
label= Label(window, text= f"Score:{}", font=('consolas', 40))
label.pack()
canvas= Canvas(window, bg=BACKGROUND_COLOR, height= "GAME_HEIGHT", width= GAME_WIDTH)
canvas.pack()
window.update()
window_width= window.window.winfo.width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height= window.winfo_screenheight()
x= (screen_width/2) - (window_width/2)
y= (screen_height/2) - (window_height/2)
window.geometry(f"{window_height}x{window_height}")

window.mainloop()


  
