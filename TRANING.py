aa = open('ltest2.txt')
a = input('Введіть слово - ')
d = aa.read()
aa.close()
def ravno(a,b):
    for k in b:
        if b.count(k) > a.count(k):
            return False
            break
    return b
dd = list(set(d.split('\n')))#прибираються слова які повторюються
click = 0
for i in range(len(dd)):
    if ravno(a,dd[i]) != False and int(len(dd[i]) > 2):
        click += 1
        print(click,' - ',ravno(a,dd[i]))
       


