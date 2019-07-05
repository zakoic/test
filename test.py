# a = float(input('请输入第一条边：'))
# b = float(input('请输入第二条边：'))
# c = float(input('请输入第三条边：'))
# if a+b > c and a+c > b and b+c > a :
#     d = (a + b + c) / 2
#     print((d*(d-a)*(d-b)*(d-c))**0.5)
# else :
#     print('三边无法组成三角形！')

# print('PLEASE CONVERT THIS SENTENCE TO LOWER CASE.'.lower())

# a= str(input('请输入卡号：'))
# while len(a) < 16 :
#     a = '0'+a
# print(a)

# a = str(input('请输入年份：'))
# b = str(input('请输入月份：'))
# c = str(input('请输入日期：'))
# if len(b) ==1:
#     b = '0'+b
# if len(c) ==1:
#     c = '0'+c
# print(a+'.'+b+'.'+c)

# a = True
# b = False
# print((a and  not b) or(not a and b))

# a = float(input('请输入身高(单位/m)：'))
# b = float(input('请输入体重(单位/kg)：'))
# c = round(b / (a*a),2)
# if c <18.5 :
#     print('BMI值为'+str(c)+'，体重过轻。')
# elif c<24:
#     print('BMI值为' + str(c) + '，属正常范围。')
# elif c<27:
#     print('BMI值为' + str(c) + '，稍重。')
# elif c<30:
#     print('BMI值为' + str(c) + '，轻度肥胖。')
# elif c<35:
#     print('BMI值为' + str(c) + '，中度肥胖。')
# else:
#     print('BMI值为' + str(c) + '，重度肥胖。')

# a = int(input('请输入年份：'))
# if a % 400 == 0 :
#     print('该年为闰年')
# elif a % 100 == 0:
#     print('该年为平年')
# elif a % 4 == 0:
#     print('该年为闰年')
# else:
#     print('该年为平年')

# a = int(input('请输入答对题数：'))
# if a > 8 :
#     print('分数为：'+str(8*8+(a-8)*6))
# else:
#     print('分数为：' + str(a*8))

# a = input('请输入三个数，以空格分开:')
# b = a.split()
# x = float(b[0])
# y = float(b[1])
# z = float(b[2])
# if y > x :
#     x,y = y,x
# if z > x :
#     x, z = z, x
# if z > y :
#     y, z = z, y
# if x > y +z :
#     print(False)
# else:
#     if x**2 == y**2 + z**2 :
#         print('Right Triangle')
#     else:
#         print('Non-Right Triangles')

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if b**2 - 4 * a * c < 0:
#     print('无实根')
# else:
#     x1 = round((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a),2)
#     x2 = round((-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a),2)
#     if x1 == x2 :
#         print('重根：x = '+str(x1))
#     else:
#         print('有两个相异根：x1 = ' + str(x1) + ',x2 = '+ str(x2))

# for a in range(4):
#     for b in range(3-a):
#         print(' ',end='')
#     for c in range(2*a+1):
#         if c % 2 == 0 :
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# a = int(input('请输入第一个数字：'))
# b = int(input('请输入第二个数字：'))
# if a > b:
#     a,b = b,a
# for c in range(a,0,-1):
#     if a%c == 0 and b%c == 0:
#         print('最大公因数为：'+str(c))
#         break

# def f(n) :
#     x = 1
#     for a in range(1,n+1):
#         x = x*a
#     return x
# a = int(input('请输入一个整数：'))
# x = 0
# for b in range(1,a+1):
#     x = x + f(b)
# print('阶乘和为：'+str(x))

# def f(a):
#     n = 0
#     for i in range(1,a):
#         if a%i == 0:
#             n = n + i
#     return n
# for a in range(1,501):
#     if a == f(a):
#         print(str(a)+'为完全数。')

# a = int(input('请输入需要查询的斐波那契数列的个数：'))
# n1 = 0
# n2 = 1
# s = '0 1'
# for i in range(2,a):
#     n = n1 + n2
#     n1 = n2
#     n2 = n
#     s = s + ' '+ str(n)
# print(s)

# a = '1234'
# s = input('请输入预测的四位数：')
# A = 0
# B = 0
# for i in range(4):
#     if a[i] == s[i]:
#         A = A +1
#     if s[i] in a:
#         B = B + 1
# print(str(A)+'A'+str(B)+'B')

# a = int(input('请输入一个正整数：'))
# n = 0
# m = a
# while abs((n+m)/2 - a**0.5) >0.1 :
#     if (n+m)/2 > a**0.5:
#         m = (n+m)/2
#     else:
#         n = (n + m) / 2
# print('平方根为：+-'+str(round((n+m)/2,2)))

# List = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# for i in range(9,0,-1):
#     for j in range(i):
#         if  List[j] > List[j+1] :
#             List[j + 1],List[j] = List[j],List[j+1]
# print(List)

# a = list(input('请输入一串数字：'))
# print('倒序为：'+''.join(a[::-1]))

# a = ['长山','小玉','花轮','永泽','小丸子']
# b = ['永泽','花轮','丸尾','野口','美环']
# c = list()
# d = list()
# for n in a:
#     if n not in b :
#         c.append(n)
# for n in b:
#     if n not in a :
#         d.append(n)
# print('数学及格且英文不及格的同学名单为：'+str(c))
# print('数学不及格且英文及格的同学名单为：'+str(d))

# i = [1,2,3,4,5,6,7,8,9,10]
# folder = i[::-1]
# j = []
# for n in range(len(folder)):
#     j.append(folder.pop())
# print(j)

# s = 'The Beatles split up in April 1970.'
# a = s.split(' ')
# print(a[2])

# a = input('请输入第一行的三位数，用逗号隔开：').split(',')
# b = input('请输入第二行的三位数，用逗号隔开：').split(',')
# c = [a,b]
# d = [[0,0],[0,0],[0,0]]
# for i in range(2):
#     for j in range(3):
#         d[j][i] = c[i][j]
# print(d)

# a = [[1,0,2],[-1,3,1]]
# b = [[3,1],[2,1],[1,0]]
# c = [[0,0],[0,0]]
# for i in range(2):
#     for j in range(2):
#         c[i][j] = a[i][0]*b[0][j]+a[i][1]*b[1][j]+a[i][2]*b[2][j]
# print(c)

# a = [[2,5],[3,7]]
# b = [[0,0],[0,0]]
# c = a[0][0]*a[1][1] - a[0][1]*a[1][0]
# if c == 0:
#     print(False)
# else:
#     b[0][0] = a[1][1]/c
#     b[0][1] = -a[0][1] / c
#     b[1][0] = -a[1][0] / c
#     b[1][1] = a[0][0] / c
#     print(b[0])
#     print(b[1])

# progression = [1, 2, 4, 8]
# if progression[1] - progression[0] == progression[2] - progression[1] == progression[3] - progression[2]:
#     print('该数列为等差数列，下一项为：'+str(progression[3]*2 - progression[2]))
# elif progression[1] / progression[0] == progression[2] / progression[1] == progression[3] / progression[2]:
#     print('该数列为等比数列，下一项为：' + str(progression[3] ** 2 / progression[2]))

# a = {'P':'Python','R':'Ruby','J':'Java'}
# b = input('请输入字符：')
# print(a[b])

# a = {}
# while True:
#     n = int(input('请输入一个数字：'))
#     if n in a:
#         a[n] = a[n]+1
#     else:
#         a[n] = 1
#     m = max(a.values())
#     print('众数为：')
#     for x in a.keys():
#         if a[x] == m:
#             print(x,end=' ')
#     print()
#     print('该数字出现的次数为：'+str(a[n]))

# import tkinter as tk
# from tkinter import ttk
#
# def hit_me():
#     var.set('kisu')
#
# window = tk.Tk()  # 主窗口
# window.title('my window')  # 窗口标题
# window.geometry('600x480')  # 窗口尺寸
#
# ### 这里是窗口的内容###
#
# var = tk.StringVar()    # 文字变量储存器
# var.set('OMG! This is TK!')
# l = tk.Label(window,
#     textvariable=var,   # 使用 textvariable 替换 text, 因为这个是可以变化的
#     bg='red', font=('Arial', 12), width=15, height=2)
# l.pack()
#
# b = tk.Button(window,
#     text='hit me',
#      width=15, height=2,
#      command=hit_me)
# b.pack()
#
# var2 = tk.StringVar()
# var2.set((11, 22, 33, 44))  # 为变量设置值
#
# # 创建Listbox
# lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox
#
# # 创建一个list并将值循环添加到Listbox控件中
# # list_items = [1, 2, 3, 4]
# # for item in list_items:
# #     lb.insert('end', item)  # 从最后一个位置开始加入值
# #
# # lb.insert(1, 'first')  # 插入操作，在第一个位置加入'first'字符
# # lb.insert(2, 'second')  # 在第二个位置加入'second'字符
# # lb.delete(2)  # 删除操作，删除第二个位置的字符
# lb.pack()
#
# cx = ttk.Combobox(window,textvariable=var2)
# cx.pack()
#
# window.mainloop()

import paddle.fluid

paddle.fluid.install_check.run_check()



















































