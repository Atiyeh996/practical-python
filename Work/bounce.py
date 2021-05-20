# bounce.py
#
# Exercise 1.5
# bounce.py

height = 100
bounce = 10
i = 1
while bounce > 0:
    height = height * (3/5)
    print(i, height)
    bounce -= 1
    i = i+1
