#this is a tool that can be used to understand bell curves, rolling two dice gives a sort of vell curve
from random import randrange
import matplotlib.pyplot as plt
db = {}
for i in range(10000):
    ans = randrange(1,7) + randrange(1,7)
    if ans not in db:
        db[ans] = 1
    else:
        db[ans] += 1
plt.bar(db.keys(),db.values(),color = 'aqua',width = 0.05)
plt.show()