n, m = [int(i) for i in input().split()]

summ = bin(int(n)+int(m))
mult = bin(int(n)*int(m))
sub = bin(int(n) - int(m))
div = bin(int(n)//int(m))

print(int(summ, 2), '--->', summ)
print(int(mult, 2), '--->', mult)
print(int(sub, 2), '--->', sub)
print(int(div, 2), '--->', div)
