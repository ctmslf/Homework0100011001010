
x = int(input())
x = abs(x)
if 100 <= x <= 999:
   s = (x // 100) + ((x // 10) % 10) + (x % 10)
    print(s % 2 == 0)
else:
    print(False)



a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
   if a != b and b != c and a != c:
       print(True)
   else:
       print(False)
else:
    print(False)