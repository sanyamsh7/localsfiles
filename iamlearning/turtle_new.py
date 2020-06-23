from turtle import *

color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        print(abs(pos()))
        break
end_fill()
done()
