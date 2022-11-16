#aa = open('ltest2.txt')
a = 'газонокосилка'# ввод с клавиатуры    .count(7)

b = 'газон'# косилка '#aa.read()##'косилка'
c = 'алиса'
d = ['алиса\nгазон\nкосилка\nзона']#\nальфредо']
'''

газон солона
ариня
:xp1
#
танок,
квітка
аакуватий
абажур
абажурний
абажурчик
абаз
абазія
абайя
:ua_1992
'''

def ravno(a,b):
    stroka = ''
    aa = list(a)
    for i in b:
        if i in a:
            aa.remove(i)
            stroka += i
    if stroka == b:
        return b
    else:
        None
print(d)
for i in d:

    print(ravno(a,i))


