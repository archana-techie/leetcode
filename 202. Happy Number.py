def happy_num(n):
    visited = set()
    while n!=1:
        summ = 0
        print(n)
        while n:
            a = n%10
            summ = summ + a**2
            n = n //10
        if summ in visited:
            return False
        visited.add(summ)
        n = summ

    return n==1


print(happy_num(2))
