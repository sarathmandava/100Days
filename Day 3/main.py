print("\nWelcome To Treasure Island!\n\nLet's see if you can win it all!\n\nAnswer the following questions, depending on the answer you will advance forward and win the treasure\n\nGOOD LUCK!")

def direction_left_or_right(direction):
  if direction == "left":
    return(direction)
  else:
    print("\nError: You picked wrong direction")
    exit()

def swim_or_wait(sw_answer):
  if sw_answer == "wait":
    return(sw_answer)
  else:
    print("\nError: Wrong choice")
    exit()

def choose_color_door(choose_color):
  if choose_color =="yellow":
    print("\nYOU WIN")
  else:
    print("\nError: Better luck next time")
    exit()

direction = input("\nDo you want to turn left/right?\t")
direction_left_or_right(direction)

sw_answer = input("\nWould you like to swim/wait?\t")
swim_or_wait(sw_answer)

choose_color = input("\nWhich color would you choose between red/blue/yellow colored doors?\t")
choose_color_door(choose_color)