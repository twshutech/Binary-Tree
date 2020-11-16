from operator import itemgetter, attrgetter
l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

def solution(l):
  result = []
  isDigit = lambda n:isinstance(int(n), float)
  typeCheck = lambda n: isDigit(n)
  integer_priority = lambda n: [int(i) if typeCheck(i) else i for i in n.split('.')]
  toStr = lambda n: '.'.join(n)
  toInt = map(integer_priority,l)
  toInt.sort()
  while len(toInt) > 0:
    verArr = map(str,toInt.pop(0))

    result.append(toStr(verArr))
  return result
def digi(l):
  result = []
  isDigit = lambda n:isinstance(n, float)
  typeCheck = lambda n: n.isdigit()
  integer_priority = lambda n: [int(i) if typeCheck(i) else i for i in n.split('.')]
  toStr = lambda n: '.'.join(n)
  toInt = map(integer_priority,l)
  toInt.sort()
  while len(toInt) > 0:
    verArr = map(str,toInt.pop(0))

    result.append(toStr(verArr))
  return result
print 'itemgetter',sorted(l, key=lambda n: [itemgetter(i) for i,v in enumerate(n.split('.'))])
# print solution(l)
# print digi(l)
# print type(float('2.0.0')),float('2.0.0')