#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# Kata from https://www.codewars.com/kata/your-ride-is-here/python
# Just a fun one that I liked. My solution was pretty bad compared to the others.
def ride(group,comet):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    gnum = 1
    cnum = 1
    for c in group:
        gnum *= (abc.index(c)+1)
    for c in comet:
        cnum *= (abc.index(c)+1)
    if cnum%47 == gnum%47:
        return "GO"
    return "STAY"
