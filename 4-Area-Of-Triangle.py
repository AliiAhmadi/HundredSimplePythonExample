# We have more than one solution but here use heron formula we learned in school
import math
first = 3
second = 4
third = 5

para = (first + second + third) / 2

area = math.sqrt(para*(para-first)*(para-second)*(para-third))

print(area)
