import portfolio
import yfinance as yf
import time


p = portfolio.Portfolio("tester")


p.add('MSFT', 30, 33)
quit()
p.add('aapl', 30, 33)
p.add('v', 33)
p.add('ma', 30, 33)

print(p.value)
print(p.day_change)
print(p.day_change_percent)
print(p.change)
print(p.close)


aaa = yf.Ticker('msft')
print(aaa.get_info()['bid'])
time.sleep(10)
print(aaa.get_info()['bid'])
time.sleep(10)
print(aaa.get_info()['bid'])
time.sleep(10)
time.sleep(10)
time.sleep(10)
print(aaa.get_info()['bid'])

quit()