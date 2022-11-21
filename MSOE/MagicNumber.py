def main():
  
  LastInput = ""
  WinLossList = []
  HighestWins = 0
  WinningTeam = 0
  WinningTeamCheck = 0
  TeamMagicNumber = 0
  MagicNumbers = []
  while not LastInput == "0 0":
    LastInput = str(input("Input a new team's wins and losses (input '0 0' to end inputs): "))
    WinLossList.append(LastInput)
  WinLossList = WinLossList[0:len(WinLossList) - 1]
  for teams in range(1, len(WinLossList) + 1):
    TeamInspect = WinLossList[teams - 1]
    TeamInspectNums = TeamInspect.split(' ')
    TeamWins = int(TeamInspectNums[0])
    WinningTeamCheck += 1
    if TeamWins > HighestWins:
      HighestWins = TeamWins
# The above code finds the team with the most wins
  for teams in range(1, len(WinLossList) + 1):
    TeamInspect = WinLossList[teams - 1]
    TeamInspectNums = TeamInspect.split(' ')
    TeamWins = int(TeamInspectNums[0])
    TeamLosses = int(TeamInspectNums[1])
    if not TeamWins == HighestWins:
      TeamMagicNumber = 162 - HighestWins - TeamLosses + 1
      if TeamMagicNumber <= 0:
        MagicNumbers.append("Eliminated from playoff contention")
      else:
        MagicNumbers.append(TeamMagicNumber)
    else:
      pass

  print(MagicNumbers)


if __name__ == "__main__":
  main()