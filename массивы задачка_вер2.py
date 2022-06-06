# версия 3.1 by mk

mass = [4, 1, 8, 9, 5, 4, 3]
c = nc = sum = 0
pr = mass[1 - 1] * mass[3 - 1] * mass[6 - 1]

for i in mass:
    sum += i
    if i % 2 == 0:
        c += 1
    else:
        nc += 1

print('сумма', sum) if c > nc else print('произведение', pr)


# for n in range (1,10):
#     for i in range(1,5):
#         print(i, "x", n, "=", n*i, end = '\t')
#     print ('')
# print ('')
# for n in range (1,10):
#     for i in range(5,9):
#         print(i, "x", n, "=", n*i, end = '\t')
#     print ('')
