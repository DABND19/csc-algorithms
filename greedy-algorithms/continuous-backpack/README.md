# Задача на программирование: непрерывный рюкзак


Первая строка содержит количество предметов *1 $\le$ n $\le$ $10^3$* и вместимость рюкзака *0 $\le$ W $\le$ 2 $\cdot$ $10^6$*. Каждая из следующих *n* строк задаёт стоимость *0 $\le$ $c_i$ $\le$ 2 $\cdot$ $10^6$* и объём *0 $\lt$ $w_i$ $\le$ 2 $\cdot$ $10^6$* предмета (*n*, *W*, *$c_i$*, *$w_i$* — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

### Sample Input:
```
3 50
60 20
100 50
120 30
```
### Sample Output:
```
180.000
```