def startFinding(l ,t):
  s = 0
  endPoint = 0
  for index, n in enumerate(l):
    s += n
    # if s != t:
    #   s += n
    if s == t:
      endPoint = index

    # Find target or reach the end or greater than limit.
    if s == t or index == len(l) - 1 or s > 250:
      return endPoint

def solution(l, t):
  fromAndTo = [-1, -1]
  endPoint = 0
  for i in range(len(l)):
    partial = slice(i, len(l), 1)
    endPoint = startFinding(l[partial], t)
    #print('i',i,'sliced list',l[partial],'endPoint',endPoint)
    if endPoint != 0:
      fromAndTo[1] = endPoint + i
      fromAndTo[0] = i
  print(fromAndTo)
  return(fromAndTo)
solution([4, 3, 10, 2, 8], 12)
solution([1, 2, 3, 4], 15)