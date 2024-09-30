expense = {"January": 2200 ,"February" :2350,"March":2600,"April":2130,"May":2190}
print (expense["February"]-expense["January"])
print (expense["February"]+expense["January"]+expense["March"])

print(2000 in expense)

expense["June"] = 1980
print(expense)

expense["April"] = expense["April"] - 200

print(expense)