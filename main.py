# #1
# a = int(input())
# b = int(input(""))
# for i in range(a, b + 1):
#     print(i)
# #2
# a = int(input("Ввод числа"))
# b = int(input())
# if a < b:
#  for i in range(a, b + 1):
#     print(i)
# else:
#   for i in range(a, b - 1, -1):
#     print(i)
# #3
# n = int(input())
# sum = 0
# for i in range(n):
#     sum += int(input())
# print(sum)
# #4
# res = 1
# n = int(input())
# for i in range(1, n + 1):
#     res *= i
# print(res)
# #5
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#      print(j, sep='', end='')
# print()
# #6
# n = int(input())
# i = 1
# while i ** 2 <= n:
#      print(i ** 2)
# i += 1
# #7
# n = int(input())
# two_in_power = 2
# power = 1
# while two_in_power <= n:
#     two_in_power *= 2
#     power += 1
# print(power - 1, two_in_power // 2)
# #8
# n = int(input())
# two_in_power = 2
# power = 1
# while two_in_power <= n:
#     two_in_power *= 2
#     power += 1
# print(power - 1, two_in_power // 2)
# #9
# len = 0
# while int(input()) != 0:
#     len += 1
# print(len)
# #10
# prev = int(input())
# answer = 0
# while prev != 0:
#     next = int(input())
#     if next != 0 and prev < next:
#         answer += 1
#     prev = next
# print(answer)
# #11
# first_max = int(input())
# second_max = int(input())
# if first_max < second_max:
#     (first_max, second_max) = (second_max,first_max)
# element = int(input())
# while element != 0:
#     if element > first_max:
#         second_max, first_max = first_max, element
#     elif element > second_max:
#         second_max = element
#     element = int(input())
# print(second_max)
# #12
# a = int(input())
# if a == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, a + 1):
#         a, b = b, a + b
#     print(b)
# #13
# n = int(input("Введите число: "))
# if n == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     print(b)
# #14
# a = input().split()
# print(a[::2])
# #15
# n = [int(asd) for asd in input("Введите переменную: ").split()]
# for asd in range(1, len(n)):
#     if a[asd] > a[asd - 1]:
#         print(a, [asd])
# #16
# imap = 0
# a = [int(i) for i in input("Введите число: ").split()]
# for i in range(1, len(a)):
#     if a[i] > a[imap]:
#         imap = i
# print(a[imap], imap)
# #17
# a = [int(s) for s in input().split()]
# n = int(input())
# for i in range(len(a)):
#     if n > a[i]:
#         print(i+1)
#         break
#     elif i == len(a)-1:
#         print(len(a)+1)
# #18
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
# #19
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
# #20
# a = [int(s) for s in input().split()]
# min = 0
# max = 0
# for i in range(1, len(a)):
#     if a[i] > a[max]:
#         max = i
#     if a[i] < a[min]:
#         min = i
# a[min], a[max] = a[max], a[min]
# print(' '.join([str(i) for i in a]))
# #21
# a = [7, 6, 5, 4, 3, 2, 1]
# b = 2
# result = a[:b] + a[b + 1:]
# print(result)
# #22
# a = [int(i) for i in input().split()]
# a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
# print(' '.join([str(i) for i in a]))
# #23
# fnum = [int(s) for s in input("Введите число").split()]
# snum = int(input("Введите второе число: "))
# for i in range(snum + 1, len(fnum)):
#     fnum[i - 1] = fnum[i]
# a.pop()
# print(' '.join([str(i) for i in a]))
# #24
# a=[int(i) for i in input("Введите число: ").split()]
# b=a+[0]
# c=[int(i) for i in input().split()]
# d=b[0]
# e=b[1]
# for i in range (0, len(b)):
#     if i==d:
#         b[i:]=[e]+b[i:len(b)]
# b.pop()
# print(' ' .join(str(i) for i in b))






