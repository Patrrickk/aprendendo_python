import os

def write(a, b):
  while (b < len(a)-1):
    b += 1
    print(a[:b])
    os.system('cls' if os.name == 'nt' else 'clear')


write('curso em video canal top recomendo     ', -1)

input()