while True:
  try:
    numLesm = int(input())
    lesm = input().split()
    nivel = 1

    for i in range(numLesm):
      lesm[i] = int(lesm[i])
      if(lesm[i]>=20):
        nivel = 3
      elif(lesm[i]>=10 and lesm[i]<20 and nivel!=3):
        nivel = 2
    print(nivel)
  except EOFError:
    break