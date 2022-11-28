text = input("Enter text: ")
for index in range(len(text)):
  print(text[index], end=" ")
print()
numwords = 0
for letter in text:  # for-each loop
  if letter == " ":
    numwords += 1
  print(letter)
print("The number of words is", numwords + 1)

def main():
  text = "cool beans"
  print("In main: " + text)

main()
print("After main: " + text)