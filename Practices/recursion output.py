def f(n):
    if n <= 0:
        return
    print("j", end=" ")
    f(n//20)
    print("v", end=" ")
    f(n//40)
    print("f", end=" ")

f(1200)

