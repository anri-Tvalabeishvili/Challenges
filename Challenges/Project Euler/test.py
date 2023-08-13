import numpy as np 

grid = [
[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0]
]

def possible(y,x,n):
  for i in range(0,9):
    if grid[y][i] == n or grid[i][x] == n:
      return False

    Y_corn = (y//3)*3
    X_corn = (x//3)*3

    for i in range(3):
      for k in range(3):
        if grid[Y_corn + i][X_corn + k] == n:
          return False

  return True



def solver():

  for y in range(9):
    for x in range(9):
      if grid[y][x] == 0:
        for n in range(1,10):
          if possible(y,x,n):
            grid[y][x] = n
            print(grid[0])
            solver()
            grid[y][x] = 0
        return
  
  print(np.matrix(grid))     



solver()