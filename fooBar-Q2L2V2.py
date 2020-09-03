def countLooping(history):
  cycle = []
  c = 0
  for item in history:
    c = history.count(item)
    if c > 1 and item not in cycle:
      cycle.append(item)
  return len(cycle)

def borrow(minuend, r, s, base):
  if r - s >= 0:
    if minuend[r - s] - 1 < 0:
      if s<len(minuend) and r>s:
        minuend[r - s] = base - 1
        s += 1
        return borrow(minuend, r, s, base)
    else:
      minuend[r - s] -= 1
      return minuend

def solution(n, base):
  global subtrahend, minuend, history, cycle, subtraction, sortList
  subtrahend = minuend = history = cycle = []

  subtraction = lambda minuend, subtrahend: minuend-subtrahend
  sortList = lambda arr, order: sorted(arr, reverse=order)
  return(prepareVariable(n, base))

def prepareVariable(n, base):
  k = len(n)
  arr = []
  for q in n:
    arr.append(q)
  subtrahend = ''.join(sortList(arr, False))# ascending
  minuend = ''.join(sortList(arr, True))# descending
  Subtractor(minuend, subtrahend, base, k)
  if cycleChecking() == True:
    return countLooping(history)

def itemToInt(list):
  newArr = []
  for item in list:
    newArr.append(int(item))
  return newArr

def cycleChecking():
  c = 1
  isLooping = False
  for item in history:
    c = history.count(item)
    if c > 2:
      isLooping = True
  return isLooping

def Subtractor(minuend, subtrahend, base, k):
  minuend = itemToInt(minuend)
  subtrahend = itemToInt(subtrahend)
  rawResult = []
  for i in range(k):
    d = 0
    r = k - i - 1

    if minuend[r] >= subtrahend[r]:
      d = minuend[r] - subtrahend[r]
    elif minuend[r] < subtrahend[r]:
      d = base - subtrahend[r] + minuend[r]
      minuend[r] = d
      #minuend[r - 1] = base - 1
      minuend = borrow(minuend, r, 1, base)

    rawResult.append(d)
  rawResult.reverse()

  newN = ''.join([str(elem) for elem in rawResult]) 
  history.append(newN)
  if cycleChecking() == False:
    prepareVariable(newN, base)
