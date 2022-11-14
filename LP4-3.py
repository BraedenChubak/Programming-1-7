def main():
  eggs = int(input("How many eggs would you like?  "))
  dozens = eggs // 12
  extra = eggs % 12
  price = 0.0
  cost = 0.0
  
  if dozens > 0 and dozens < 4:
    price = 0.5
  elif dozens >= 4 and dozens < 6:
    price = 0.45
  elif dozens >= 6 and dozens < 11:
    price = 0.4
  elif dozens >= 11:
    price = 0.35

  cost = price * dozens + price/12 * extra
  print("The cost of your eggs is: $" + str(cost))
  pass


if __name__ == "__main__":
  main()