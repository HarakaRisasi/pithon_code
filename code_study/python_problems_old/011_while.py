##_*_ coding: utf-8 _*_
##Итерация - это один полный цикл
##Циклы продолжаются, пока проверочное выражение равно TRUE
##Циклы могут быть вложенными один в другого
i = 0 
while i <= 4 :
    print('\nOuter loop iteration: ', i)
    ##i += 1 -  переменная счетчик
    i += 1

j = 1
while j < 4 :
    print('\tInner loop iteration: ', j)
    j += 1

##+= - сокращенная запись i = i + 1
##*=, /=, -=
