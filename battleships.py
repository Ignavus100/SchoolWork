import random

def CheckSunk(board, row, column, ships, points):
  for i in range(len(points)):
    if [row, column] in list(points.values())[i]:
      ships[i][1] -= 1
      if ships[i][1] == 0:
        print("you have sunk the "+ ships[i][0])
        del ships[i]
  return ships
      

def GetName():
  name = input("Enter your name: ")
  return name

def GetRowColumn():
  print()
  Column = 10
  Row = 10
  while Column not in range(0, 10):
    Column = int(input("Please enter column: "))
  while Row not in range(0, 10):  
    Row = int(input("Please enter row: "))
  print()
  return Row, Column
            
def MakePlayerMove(Board, Ships, moves, points):
  Row, Column = GetRowColumn()
  if Board[Row][Column] == "m" or Board[Row][Column] == "h":
    print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
  elif Board[Row][Column] == "-":
    print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
    Board[Row][Column] = "m"
    moves += 2
  else:
    print("Hit at (" + str(Column) + "," + str(Row) + ").")
    Board[Row][Column] = "h"
    moves += 1
    Ships = CheckSunk(Board, Row, Column, Ships, points)
  return moves, Ships
        
def SetUpBoard():
  Board = []
  for Row in range(10):
    BoardRow = []
    for Column in range(10):
      BoardRow.append("-")
    Board.append(BoardRow)
  return Board

def LoadGame(Filename, Board):
  BoardFile = open(Filename, "r")
  for Row in range(10):
    Line = BoardFile.readline()
    for Column in range(10):
      Board[Row][Column] = Line[Column]
  BoardFile.close()
    
def PlaceRandomShips(Board, Ships):
  points = {}
  for Ship in Ships:
    Valid = False
    while not Valid:
      Row = random.randint(0, 9) 
      Column = random.randint(0, 9) 
      HorV = random.randint(0, 1)
      if HorV == 0:
        Orientation = "v" 
      else:
        Orientation = "h" 
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
    print("Computer placing the " + Ship[0])
    points[Ship[0]] = PlaceShip(Board, Ship, Row, Column, Orientation)
  return points

def PlaceShip(Board, Ship, Row, Column, Orientation):
  points = []
  if Orientation == "v":
    for Scan in range(Ship[1]):
      Board[Row + Scan][Column] = Ship[0][0]
      points.append([(Row + Scan), Column])
  elif Orientation == "h":
    for Scan in range(Ship[1]):
      Board[Row][Column + Scan] = Ship[0][0]
      points.append([Row, (Column + Scan)])
  return points

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
  if Orientation == "v" and Row + Ship[1] > 10:
    return False
  elif Orientation == "h" and Column + Ship[1] > 10:
    return False
  else:
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-":
          return False
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-":
          return False
  return True

def CheckWin(Board):
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True
 
def PrintBoard(Board, moves):
  print()
  print("The board looks like this: ")  
  print()
  print("You have made " + str(moves) + " moves.")
  print()
  print (" ", end="")
  for Column in range(10):
    print(" " + str(Column) + "  ", end="")
  print()
  for Row in range(10):
    print (str(Row) + " ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print(" ", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print(" ", end="")                
      else:
        print(Board[Row][Column], end="")
      if Column != 9:
        print(" | ", end="")
    print()
  return moves
       
def DisplayMenu(name):
  
  print("MAIN MENU")
  print("")
  print(str(name))
  print("")
  print("1. Start new game")
  print("2. Load training game")
  print("9. Quit")
  print("")
    
def GetMainMenuChoice():
  new = False
  while new == False:
    print("Please enter your choice: ", end="")
    try:
      Choice = int(input())
      new = True
    except:
      print()
      print("Invalid input")
    print()
  return Choice

def PlayGame(Board, Ships, points, highScore):
  GameWon = False
  moves = 0
  while not GameWon:
    PrintBoard(Board, moves)
    moves, Ships = MakePlayerMove(Board, Ships, moves, points)
    GameWon = CheckWin(Board)
    if GameWon:
      print("All ships sunk!")
      print()
      print("You win in " + str(moves) + " moves!")
      if highScore > moves:
        highScore = moves
      print("highscore is " + str(highScore))
    elif moves > 50:
      print("You have run out of moves! Game over.")

if __name__ == "__main__":
  TRAININGGAME = "Training.txt"
  MenuOption = 0
  highScore = 999
  while not MenuOption == 9:
    name = GetName()
    Board = SetUpBoard()
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
    DisplayMenu(name)
    MenuOption = GetMainMenuChoice()
    if MenuOption == 1:
      points = PlaceRandomShips(Board, Ships)
      print(points)
      PlayGame(Board,Ships, points, highScore)
    if MenuOption == 2:
      LoadGame(TRAININGGAME, Board)
      PlayGame(Board, Ships, points, highScore) 
