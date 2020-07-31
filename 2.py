y = 0

def Increment(x):
    global y
    x = x + 1
    y = y + 1
    
x = 0
print("x={}, y={}".format(x, y))
x = 10
Increment(x)
print("x={}, y={}".format(x, y))
Increment(x)
print("x={}, y={}".format(x, y))
