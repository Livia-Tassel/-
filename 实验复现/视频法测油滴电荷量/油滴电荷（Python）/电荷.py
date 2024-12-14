from decimal import *
import math
getcontext().prec = 24
# 设置每个油滴上下往返时间的测量次数
# text_times = 5

# 相关参数值
p = Decimal('1.013e5')  # 空气压强，单位 Pa
b = Decimal('8.22e-3')  # 修正常数，单位根据上下文定义
n = Decimal('1.83e-5')  # 粘滞系数，单位 Pa·s
d = Decimal('0.005')  # 平行极板间距离，单位 m
L = Decimal('0.0016')  # 匀速上升/下降的距离，单位 m
g = Decimal('9.79')  # 重力加速度，单位 m/s²
rou = Decimal('981')  # 油的密度，单位 kg/m³
# rou = Decimal('1.2928')  # 空气的密度，单位 kg/m³
pi = Decimal(str(math.pi))  # 圆周率π
e = Decimal('1.6021892e-19')  # 理论元电荷值，单位 C

# data_tg = []  # 用于存储下降时间
# data_te = []  # 用于存储下降时间
# for i in range(1, text_times+ 1 ):
#     tg = input("输入匀速下降时间：tg" + str(i) + "= ")
#     data_tg.append(Decimal(tg))
# tgp = sum(data_tg)/Decimal(text_times)
# print("计算得到的tg平均值："+str(sum(data_tg)/Decimal(text_times)) )
# for i in range(1, text_times+ 1 ):
#     te = input("输入匀速上升时间：te" + str(i) + "= ")
#     data_te.append(Decimal(te))
# tep = sum(data_te)/Decimal(text_times)
# print("计算得到的te平均值："+str(sum(data_te)/Decimal(text_times)) )

vg = input("输入匀速下降速度：vg = ")
v = Decimal(vg)
U = input("输入平衡电压：U = ")
U = Decimal(U)

# 中间变量a/k
a = (18 * pi) / pow(Decimal(2) * rou * g, Decimal('0.5'))  # 将0.5转换为Decimal类型
k = d / U
# 电荷量与电子数
q = a * k * (pow((n * v) / (1 + b / p), Decimal('1.5')))  # 将1.5转换为Decimal类型
N = q / e

#  结果显示
print("油滴所带的电荷量：q=",end='');print('%e'% q)
print("q=",end='');print(q)
print('q/e:N=',end='');print(N)
input("结束，按任意键继续")

