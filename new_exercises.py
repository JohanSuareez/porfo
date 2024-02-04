# Define a function which can print a list where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
import random
def squrdic():
    dic = []
    for i in range(1, 5):
        n = random.randint(1, 20)
        dic.append(n)
    print(f' This is the original dictionary: {dic}')
    sec_dic = []
    for i in dic:
        m = i ** 2
        sec_dic.append(m)
    print(f'And this is the secondary list with all the keys squared {sec_dic}')



squrdic()
