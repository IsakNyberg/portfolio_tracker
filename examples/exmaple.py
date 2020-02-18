from portfolio_tracker import Portfolio
from time import sleep


example = Portfolio("example")
example.load()

print(example)

while 1:
    example.update()
    day_change = example.day_change
    day_precent = example.day_change_percent

    print('day_change:', day_change)
    print('day_change_percent', day_precent)
    sleep(10)

