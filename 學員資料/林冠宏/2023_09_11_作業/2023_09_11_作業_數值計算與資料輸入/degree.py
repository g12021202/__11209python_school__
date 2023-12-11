import math
a = float(input("請輸入對邊:"))
b = float(input("請輸入斜邊:"))

print("直角三角形的角度為:",round(math.degrees(math.asin(a/b))),"degree")