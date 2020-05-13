import unittest
import os
import csv

import csvjoin

class iter2list(unittest.TestCase):
  def test_empty(self): self.assertEqual(("", []), csvjoin.iter2list(("", [])))

class join_ii(unittest.TestCase):
  def test_empty(self): self.assertEqual(None, next(csvjoin.join_ii([],[]), None))

class join_ff(unittest.TestCase):
  def test1(self):
    os.makedirs("./.test/join_ff/test1", exist_ok=True)
    with open("./.test/join_ff/test1/f1.csv", "w", newline="") as f1: csv.writer(f1).writerows([
      ["amazon",    6, "cloud"],
      ["apple",     5, "phone"],
      ["facebook",  8, "sns"],
      ["google",    6, "search"],
      ["microsoft", 9, "os"],
    ])
    with open("./.test/join_ff/test1/f2.csv", "w", newline="") as f2: csv.writer(f2).writerows([
      ["amazon",    1, "shop"],
      ["apple",     2, "application"],
      ["facebook",  3, "ai"],
      ["google",    4, "os"],
      ["microsoft", 5, "cloud"],
    ])
    with open("./.test/join_ff/test1/f1.csv","r", newline="") as f1:
      with open("./.test/join_ff/test1/f2.csv","r", newline="") as f2:
        joined = csvjoin.join_ff(f1,f2)

        amazon = next(joined)
        self.assertEqual("amazon", amazon[0])
        self.assertEqual(["amazon", "6", "cloud"], amazon[1][0][1])
        self.assertEqual(["amazon", "1", "shop" ], amazon[1][1][1])

        apple = next(joined)
        self.assertEqual("apple", apple[0])
        self.assertEqual(["apple", "5", "phone"       ], apple[1][0][1])
        self.assertEqual(["apple", "2", "application" ], apple[1][1][1])

        facebook = next(joined)
        self.assertEqual("facebook", facebook[0])
        self.assertEqual(["facebook", "8", "sns" ], facebook[1][0][1])
        self.assertEqual(["facebook", "3", "ai"  ], facebook[1][1][1])

        google = next(joined)
        self.assertEqual("google", google[0])
        self.assertEqual(["google", "6", "search" ], google[1][0][1])
        self.assertEqual(["google", "4", "os"     ], google[1][1][1])

        microsoft = next(joined)
        self.assertEqual("microsoft", microsoft[0])
        self.assertEqual(["microsoft", "9", "os"    ], microsoft[1][0][1])
        self.assertEqual(["microsoft", "5", "cloud" ], microsoft[1][1][1])
      pass
    pass
  pass

def main(): return unittest.main()

def try_exec(): return "__main__" == __name__ and main()

try_exec()
