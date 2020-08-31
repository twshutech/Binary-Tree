subtrahend = []
minuend = []
history = []
cycle = []

def solution(n, base):
  k = len(n)
  arr = []
  for q in n:
    arr.append(q)
  arr.sort() # ascending
  subtrahend = ''.join(arr)
  arr.sort(reverse=True) # descending
  minuend = ''.join(arr)
  print(n, base, k)
  Subtractor(minuend, subtrahend, base, k)

def itemToInt(n):
  print(n)
  newArr = []
  for item in n:
    newArr.append(int(item))
  return newArr

def cycleChecking():
  c = 1
  isLooping = False
  for item in history:
    c = history.count(item)
    if c > 3:
      isLooping = True
      if c not in cycle:
        cycle.append(c)
  # if len(cycle) != 0:
  #   for cycleItem in cycle:
  #     cycleIndex.append(history.index(cycleItem))
  # print(cycleIndex)
  return isLooping

def Subtractor(minuend, subtrahend, base, k):
  minuend = itemToInt(minuend)
  subtrahend = itemToInt(subtrahend)
  result = []
  for i in range(k):
    d = 0
    r = k - i - 1

    if minuend[r] > subtrahend[r]:
      d = minuend[r] - subtrahend[r]
    elif minuend[r] < subtrahend[r]:
      d = base - subtrahend[r] + minuend[r]
      if r - 1 != -1:
        minuend[r - 1] = minuend[r - 1] - 1
      print('base',base, subtrahend[r], minuend[r])
    result.append(d)
  result.sort(reverse=False)

  newN = ''.join([str(elem) for elem in result]) 
  newN = newN.zfill(k)
  history.append(newN)
  if cycleChecking() == False:
    solution(newN, k)
  else:
    print(cycle)

solution('1211', 10)
#solution('210022', 3)