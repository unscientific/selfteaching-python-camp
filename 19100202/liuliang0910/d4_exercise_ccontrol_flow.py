# 今天的作业是打印九九乘法表，我先想想用中文怎么样诠释
"""
a和b相乘，
a和b的取值范围是（1到9）
第一列，a*b，a是1到9，b是1
第二列，a*b，a是2到9，b是2
第三列，a*b，a是3到9，b是3
第四列，a*b，a是4到9，b是4
第五列，a*b，a是5到9，b是5
第六列，a*b，a是6到9，b是6
第七列，a*b，a是7到9，b是7
第八列，a*b，a是8到9，b是8
第九列，a*b，a是9到9，b是9
然后打印出来
我的中文思路，但是不会表达，啊哈哈，看看别人的思路咯

"""


for i in range(1,10):
    for j in range(1,i+1):
        print ('%d *'%i,'%d'%j,'=%-2d'%(i*j),end=' ')    #第三个对象是左对齐，宽度为2
    print('')
    





