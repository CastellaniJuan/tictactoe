"""
Author: Juan Ignacio Castellani
Assignment: W02 Prove - Developer Solo Code Submission

Purpose: Tic-tac-toe game in python.

"""
def builder(map):
  for i in range(len(map)):
    if i==2 or i==5 or i==8:
      print(f"{map[i]}")
    else:
      print(f"{map[i]}|", end="")

def game_manager(map, turn):

  while True:
    try:  
      print(f"{turn}'s turn to choose a square(1-9): ", end="")
      square=int(input(""))-1
      break
    except ValueError:
      print("Please input a valid number")
  while True:
    if map[square]=="x" or map[square]=="o":
      print("Square not available, please choose another.")
      print(f"{turn}'s turn to choose a square(1-9): ", end="")
      square=int(input(""))-1
    elif square>8 or square<0:
      print("Please choose a valid square(1-9)")
      print(f"{turn}'s turn to choose a square(1-9): ", end="")
      square=int(input(""))-1
    else:
      map[square]=turn
      if turn=="x":
        turn="o"
      else:
        turn="x"
      return turn
      break
    
def game_validator(map):
  def checker(map, player):
    winner=""
    if map[0]==player and map[1]==player and map[2]==player:
      winner=player  
    elif map[3]==player and map[4]==player and map[5]==player:
      winner=player
    elif map[6]==player and map[7]==player and map[8]==player:
      winner=player
    elif map[0]==player and map[4]==player and map[8]==player:
      winner=player
    elif map[2]==player and map[4]==player and map[6]==player:
      winner=player
    elif map[0]==player and map[3]==player and map[6]==player:
      winner=player
    elif map[1]==player and map[4]==player and map[7]==player:
      winner=player
    elif map[2]==player and map[5]==player and map[8]==player:
      winner=player
      
    return winner
  
  winner=checker(map,"x")
  if winner=="":
    winner=checker(map,"o")

  if winner != "":
    return True, winner
  else:
    return False, ""
    
def main():
  map=["1","2","3","4","5","6","7","8","9"]
  turn="x"
  
  while True:
    print(map)
    builder(map)
    checker, winner=game_validator(map)
    if checker==True:
      print(f"{winner} won the match")
      break
    turn_counter=0
    for i in range(len(map)):
      if map[i]=="x" or map[i]=="o":
        turn_counter+=1
    if turn_counter==9:
      print("Draw")
      break
    turn=game_manager(map, turn)
  
  
if __name__ == "__main__":
  main()
  