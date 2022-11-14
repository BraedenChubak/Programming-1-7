def main():
  weight = float(input("Please input weight in kilograms: "))
  length = int(input("Please input length in centimeters: "))
  width = int(input("Please input width in centimeters: "))
  height = int(input("Please input height in centimeters: "))

  size = length * width * height

  if weight > 27 and size > 100000:
    print("Package is too heavy and too large")
  elif weight > 27:
    print("Package is too heavy")
  elif size > 100000:
    print("Package is too large")
  else:
    print("We are able to ship your package!")
  pass


if __name__ == "__main__":
  main()