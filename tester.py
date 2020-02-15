import portfolio
import time


p = portfolio.Portfolio("tester")


p.add('amd', 153.26/3, 3)
p.add('msFt', 161.94, 1)
p.add('snap', 85.65/5, 5)

t = time.time()
p.update()
t = time.time() -t

print(t)
print(p)
print("op",p.open)
print("cl",p.close)
print("value",p.value)
print("day change",p.day_change)
print("day %", p.day_change_percent)

print("change",p.change)
print("change %",p.change_percent)

