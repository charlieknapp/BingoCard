import random

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint(Bingo):
  for row in Bingo:
    print(f"{row[0]}  |  {row[1]}  |  {row[2]}")
    print("-------------------")

def createCard():
  bingo = [[],[],[]]
  index = 0
  nums = []
  for i in range(9):
    num = ran()
    while num in nums:
      num = ran()
    nums.append(num)
    nums.sort()
  for n in nums:
    bingo[index].append(n)
    if len(bingo[index]) > 2:
      index += 1
  bingo[1][1] = "BINGO"
  return bingo

card = createCard()
prettyPrint(card)

while True:
  num = int(input("What number was called? "))
  for row in card:
    if num in row:
      row[row.index(num)] = "X"
  xs = 0
  for row in card:
    for item in row:
      if item == "X":
        xs += 1
  if xs == 8:
    print("You have won!")
    break
  prettyPrint(card)