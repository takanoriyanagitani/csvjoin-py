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
  m1 = map(lambda e: ((k1(e), 1), e), i1)
  m2 = map(lambda e: ((k2(e), 2), e), i2)
  m = heapq.merge(*(m1,m2))
  g = itertools.groupby(map(lambda t: (t[0][0], t), m), itemgetter(0))
  return map(lambda e: fi(e), g)

def join_ff(f1=sys.stdin, f2=sys.stdin): return join_ii(
  csv.reader(f1),
  csv.reader(f2),
)

def join_dd(r1=sys.stdin, r2=sys.stdin, f1=None, f2=None, k1=itemgetter("key"), k2=itemgetter("key")): return join_ii(
  csv.DictReader(r1,fieldnames=f1),
  csv.DictReader(r2,fieldnames=f2),
  k1,
  k2,
)

def join_nf(n1="f1.csv", n2="f2.csv"):
  with open(n1, mode="r", newline="") as f1:
    with open(n2, mode="r", newline="") as f2:
      return join_ff(f1, f2)

def join_nd(n1="f1.csv", n2="f2.csv", f1=None, f2=None, k1=itemgetter("key"), k2=itemgetter("key")):
  with open(n1, mode="r", newline="") as r1:
    with open(n2, mode="r", newline="") as r2:
      return join_dd(r1, r2, f1, f2, k1, k2)
