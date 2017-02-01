#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# https://www.codewars.com/kata/bouncing-balls/python
# One I had to think about because I didn't at first factor in the bounce checking

def bouncingBall(h, bounce, window):
    bounces = 0
    if h <= window or bounce <= 0 or bounce >=1:
        return -1
    while h > window:
        bounces = bounces + 1
        h = h * bounce
        if h > window:
            bounces = bounces + 1
    if bounces == 0:
        bounces = -1

    return bounces

print(bouncingBall(3, 0.66, 1.5))
print(bouncingBall(30, 0.66, 1.5))
print(bouncingBall(10, 0.66, 10))
print(bouncingBall(100, 0.66, 1.5))
print(bouncingBall(100, 0.66, 99))
print(bouncingBall(100, 0.1, 1.5))
print(bouncingBall(100, 0.99, 1.5))
print(bouncingBall(100, 1, 1.5))
print(bouncingBall(100, 0, 1.5))
