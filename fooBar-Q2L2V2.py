subtrahend = []
minuend = []
history = []
cycle = []

greater = lambda a,b: a>b
subtraction = lambda a, b: a - b
borrowedSubtraction = lambda a, b, c:  c - b + a
sortList = lambda a, b : sorted(a, reverse=b)
appendInt = lambda a, b : b.append(int(a))
appendStr = lambda a, b : b.append(str(a))

def solution(n, base):
  k = len(n)
  arr = []
  for q in n:
    appendStr(q, arr)

  subtrahend = ''.join(sortList(arr, False))# ascending
  minuend = ''.join(sortList(arr, True))# descending

  Subtractor(minuend, subtrahend, base, k)

def itemToInt(listN):
  newArr = []
  for item in listN:
    appendInt(item, newArr)
  return newArr

def cycleChecking():
  c = 1
  isLooping = False
  for item in history:
    c = history.count(item)
    if c > 10:
      isLooping = True
      if int(item) not in cycle:
        appendInt(item, cycle)
      #if len(cycle) != 0:
      #  print(cycle)
  return isLooping

def borrow(i, r, minuend, s):
  if minuend[r - s] < 1:
    minuend -= 1
    return minuend
  else:
    s += 1
    borrow(i, r, minuend, s)

def Subtractor(minuend, subtrahend, base, k):
  minuend = itemToInt(minuend)
  subtrahend = itemToInt(subtrahend)
  result = []
  for i in range(k):
    d = 0
    r = k - i - 1

    print(r,i)
    if greater(minuend[r], subtrahend[r]): 
      d = subtraction(minuend[r], subtrahend[r])
    elif greater(subtrahend[r], minuend[r]):
      d = borrowedSubtraction(minuend[r], subtrahend[r], base)
      if r > 1:
        minuend[r - 1] = minuend[r - 1] - 1

    appendInt(d, result)
  result = sortList(result, False)

  newN = ''.join([str(elem) for elem in result]) 
  history.append(newN)
  if cycleChecking() == False:
    solution(newN, 3)
  else:
    print(history)

#solution('1211', 10)
solution('210022', 3)
