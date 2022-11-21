def main():

  LetterFits = 0
  BadWords = [""]
  words = str(input("Enter your list of words, with the first word being the word that the other words will fit inside: "))
  wordlist = (words.split(' '))
  FirstWord = wordlist[0]
  print(FirstWord)
  FirstWordLetters = list(FirstWord)
  for num in range(2, len(wordlist) + 1):
    WordInspect = wordlist[num - 1]
    WordInspectLetters = list(WordInspect)
    for num2 in range(1, len(WordInspectLetters) + 1):
      LetterInspect = WordInspectLetters[num2 - 1]
      for num3 in range(1, len(FirstWordLetters) + 1):
        if LetterInspect == FirstWordLetters[num3 - 1]:
          LetterFits = 1
      if LetterFits == 1:
        LetterFits = 0
      else:
        BadWords.append(WordInspect)
        break
          
  print("The words that do not fit are: " + str(BadWords[1:len(BadWords)]))
  pass


if __name__ == "__main__":
  main()