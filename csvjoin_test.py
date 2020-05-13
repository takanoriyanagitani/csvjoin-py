import unittest

import csvjoin

class iter2list(unittest.TestCase):
  def test_empty(self): self.assertEqual(("", []), csvjoin.iter2list(("", [])))
  pass

def main(): return unittest.main()

def try_exec(): return "__main__" == __name__ and main()

try_exec()
