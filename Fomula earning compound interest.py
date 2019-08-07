p = 10000
n = 12
r = 0.08
t =int(input("Input number of years the money be compounded for:"))
a = p*((1+r/n)**(n*t))
print(a)
