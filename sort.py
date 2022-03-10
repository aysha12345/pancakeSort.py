import sys

def pancake_sort(list):
  """You should implement this function, which takes the pancake stack as a list from bottom to top. I.e., 5 4 3 2 1 is an already sorted stack."""
  start = 0
  counter = ""
  sortedList = sorted(list)
  expectedList = sortedList[::-1]

  while list != expectedList:
    maximumValue = max(list[start:])
    maximumIndex = list.index(maximumValue)

    subList = list[maximumIndex:]
    reversedSubList = subList[::-1]

    if maximumIndex != len(list) - 1 and maximumIndex != start:
      counter += str(maximumIndex + 1) + " "
      
    if maximumIndex != start:
      counter += str(start + 1) + " "

    restOfList = list[:maximumIndex]

    list = restOfList + reversedSubList
  
    if start != 0:
      list = list[:start] + (list[start:][::-1])    
    else:
      list = list[::-1]

    start += 1
  counter += "0"
  return counter

line=sys.stdin.readline().strip()
while line!="0":
  linearray=list(map(int,line.split()))
  print(pancake_sort(linearray))
  line=sys.stdin.readline().strip()
  
print("0")
