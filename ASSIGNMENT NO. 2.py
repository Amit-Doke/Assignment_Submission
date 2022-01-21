
'''
ASSIGNMENT NO.2 (DAY 2)
Email: amitdoke121@gmail.com
'''

variable = [10,4.5,'Hello World',True,(1,2,3,4,5),dict({'Amit':12,'Sumit':14,'Anil':16}),{1,23,4,53,2,6,2,8},[23,455,6,88,'amit']]

for i in range(len(variable)):
    print()
    print(i+1,')',variable[i],':',type(variable[i]))
    print('%s) %s : %s'%(i+1,variable[i],type(variable[i])))
    print('{}) {} : {}'.format(i+1,variable[i],type(variable[i])))
    print(f'{i+1}) {variable[i]} : {type(variable[i])}')
    
'''
OUTPUT:-
test\ASSIGNMENT NO. 2.py"

1 ) 10  :  <class 'int'>
1) 10 : <class 'int'>
1) 10 : <class 'int'>
1) 10 : <class 'int'>

2 ) 4.5  :  <class 'float'>
2) 4.5 : <class 'float'>
2) 4.5 : <class 'float'>
2) 4.5 : <class 'float'>

3 ) Hello World  :  <class 'str'>      
3) Hello World : <class 'str'>
3) Hello World : <class 'str'>
3) Hello World : <class 'str'>

4 ) True  :  <class 'bool'>
4) True : <class 'bool'>
4) True : <class 'bool'>
4) True : <class 'bool'>

5 ) (1, 2, 3, 4, 5)  :  <class 'tuple'>
5) (1, 2, 3, 4, 5) : <class 'tuple'>
5) (1, 2, 3, 4, 5) : <class 'tuple'>
5) (1, 2, 3, 4, 5) : <class 'tuple'>

6 ) {'Amit': 12, 'Sumit': 14, 'Anil': 16}  :  <class 'dict'>
6) {'Amit': 12, 'Sumit': 14, 'Anil': 16} : <class 'dict'>
6) {'Amit': 12, 'Sumit': 14, 'Anil': 16} : <class 'dict'>
6) {'Amit': 12, 'Sumit': 14, 'Anil': 16} : <class 'dict'>

7 ) {1, 2, 4, 53, 6, 23, 8}  :  <class 'set'>
7) {1, 2, 4, 53, 6, 23, 8} : <class 'set'>
7) {1, 2, 4, 53, 6, 23, 8} : <class 'set'>
7) {1, 2, 4, 53, 6, 23, 8} : <class 'set'>

8 ) [23, 455, 6, 88, 'amit']  :  <class 'list'>
8) [23, 455, 6, 88, 'amit'] : <class 'list'>
8) [23, 455, 6, 88, 'amit'] : <class 'list'>
8) [23, 455, 6, 88, 'amit'] : <class 'list'>
'''