def startFinding(l ,t):
  endPoint = 0
  for i in range(len(l)):
    s = sum(l[0:i:1])
    if s == t:
      endPoint = i

    if s == t or i == len(l) - 1 or s > 250:
      # Find target or reach the end or greater than limit.
      break
  return endPoint

def solution(l, t):
  fromAndTo = [-1, -1]
  endPoint = 0
  for i in range(len(l)):
    endPoint = startFinding(l[i:], t) + i
    if endPoint >= i and sum(l[i:endPoint:1]) == t:
      fromAndTo[1] = endPoint - 1
      fromAndTo[0] = i
      break
    elif endPoint == i and l[i] == t:
      fromAndTo = [i, i]
      break
  return(fromAndTo)
# print(sum(range(250)[3:22:1]))
# print(solution(range(250), 111))
print(solution([4, 3, 10, 2, 8], 12))
print(solution([1, 2, 3, 4], 15))
print(solution([3, 2, 1, 3, 4, 8, 1, 1, 1, 30], 30))
print(solution([1, 2, 15, 3, 4, 8, 1, 1, 1, 1], 30))

