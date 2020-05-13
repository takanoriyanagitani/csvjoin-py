import csv
import heapq
import itertools
import sys
from operator import itemgetter

def iter2list(e=tuple(), ig=itemgetter(1)):
  k = e[0]
  i = map(ig, e[1])
  return (
    k,
    list(i),
  )

def join_ii(i1=iter([]), i2=iter([]), k1=itemgetter(0), k2=itemgetter(0), fi=iter2list):
  m1 = map(lambda e: (k1(e), e), i1)
  m2 = map(lambda e: (k2(e), e), i2)
  m = heapq.merge(*(m1,m2))
  g = itertools.groupby(m, itemgetter(0))
  return map(lambda e: fi(e), g)

def join_ff(f1=sys.stdin, f2=sys.stdin): return join_ii(
  csv.reader(f1),
  csv.reader(f2),
)

def join_dd(r1=sys.stdin, r2=sys.stdin, f1=None, f2=None): return join_ii(
  csv.DictReader(r1,fieldnames=f1),
  csv.DictReader(r2,fieldnames=f2),
)
