def solution(l):
  sort_versions = lambda ver: map(int, ver.split('.'))
  l.sort(key=sort_versions)
  return l