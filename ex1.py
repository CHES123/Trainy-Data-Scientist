'''Нашей компании нужно сгруппировать клиентов для АБ-тестов. Алгоритм группировки очень простой - взять ID клиента (состоит из 5-7 цифр, например 7412567) и найти сумму всех его цифр. Получившееся число и является номером группы, в которую входит данный клиент.

Для того, чтобы понять, насколько хорош такой простой алгоритм, тебе нужно написать следующие диагностические функции:

   1. Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и начинается с 0. На вход функция получает целое число n_customers (количество клиентов).
   2. Функция, аналогичная первой, если ID начинается с произвольного числа. На вход функция получает целые числа: n_customers (количество клиентов) и n_first_id (первый ID в последовательности).
'''
'''0000000 - 9999999'''
from collections import Counter, OrderedDict

def fu_count_in_group(n_customers, n_first_id):    
    try:    
        if n_first_id == n_customers:
            return 'Первый id равен кол-ву клиентов'
            
        elif n_first_id > n_customers:
            return 'Первый id больше кол-ва клиентов'
        
        elif len(str(n_customers)) > 7 or len(str(n_first_id)) > 7:
            return 'Длина id больше 7'
            
        elif n_customers > 0 and  n_first_id >= 0  and n_first_id < n_customers:
            #генерируем список id            
            n_List_Id = [str(x) for x in range(n_first_id, n_customers + 1)]
            #генерируем список  sum id
            n_List_Sum_id =[sum([int(x) for x in list(y)]) for y in n_List_Id] 
            #Считаем кол-во групп и сортируем (№ группы(сум), кол-во)
            res = dict(OrderedDict(Counter(n_List_Sum_id)))            
            return res
                
    except (TypeError):        
        print('id некорректный')
    

n_customers = 1000
n_first_id =  99
#1
def fu_Count_In_Group_Full(n_customers):
    return fu_count_in_group(n_customers, 0)

print(fu_Count_In_Group_Full(n_customers))
print()
#2
def fu_Count_In_Group_srez(n_customers, n_first_id):
    return fu_count_in_group(n_customers, n_first_id)

print(fu_Count_In_Group_srez(n_customers, n_first_id))
