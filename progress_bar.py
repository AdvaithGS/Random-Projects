import sys,time
from math import floor,ceil
def progress(done,total,length = 40):
  arg = "Progress: |" + "█"*floor(done*40/total) + " "*ceil(40 - done*40/total) + f"| {done}/{total}{' Complete!' if done == total else ''}\r"
  sys.stdout.write(arg)
  sys.stdout.flush()
  return arg