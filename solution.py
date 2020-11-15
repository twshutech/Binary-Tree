import re
l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
sequenceVersionList = []
print 'list of version: ',l
versionParser = re.compile("^(\d+\.?)(\d+)?(\.{1})(\*|\d+)?$")
splitDotParser = re.compile(".")
toInt = lambda v:int(v)
matchesList = lambda v: versionParser.findall(v)
splitDot = lambda v: v.split(".")

def toIntList(ver):
  list = splitDot(ver)
  return [toInt(i) for i in list]

# def getIndex(ver):
#   print 'sequenceVersionList',sequenceVersionList,'ver',ver
#   if len(sequenceVersionList) == 1:

#   elif len(sequenceVersionList) > 1:
#     print 'head',sequenceVersionList[0],'tail',sequenceVersionList[-1]
#   return len(sequenceVersionList)+1

def solution(l):
  list = map(toIntList, l)
  # while len(l) > 0:
  #   ver = l.pop()
  #   sequenceVersionList.insert(getIndex(ver), ver)
  #print(l,'l.sort()',l.sort())
  return list

for version in solution(l):
  print 'version',version