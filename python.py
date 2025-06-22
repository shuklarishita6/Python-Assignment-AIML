#Python Assignment Questions  

# 1.  Write a Python program to find the second largest number in a list without using the sort() method. 
def second_largest(num):
    if len(num) < 2:
        return None
    a = b = float('-inf')
    for c in num:
        if c > a:
            b = a
            a = c
        elif a > c > b:
            b = c
    return b if b != float('-inf') else None


x = [10, 50, 30, 40]
print(second_largest(x))
print (hello)