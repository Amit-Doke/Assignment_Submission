'''
ASSIGNMENT NO.4 (DAY 4)
Email: amitdoke121@gmail.com
'''

def _input_list(size):
    _list=list()
    i=0
    while i < size:
        _list.append(input("Enter data : "))  
        i+=1
    return _list
      
def data_print():
    variable = [10,4.5,'Hello World',True,(1,2,3,4,5),dict({'Amit':12,'Sumit':14,'Anil':16}),{1,23,4,53,2,6,2,8},[23,455,6,88,'amit']]
    for i in range(len(variable)):
        print()
        print(f'{i+1}) {variable[i]} : {type(variable[i])}')
    return

def list_data_print(_data):
    print(f'{_data}')
    return

def _list_data(var1,var2):
    _list_var=[]
    _list_var.append(var1)
    _list_var.append(var2)
    return _list_var

 
def main():
    data_print()
    print()
    list_data_print(_input_list(int(input("Enter Size Of your list : "))))
    print()
    print(f'{_list_data(_input_list(int(input("Enter Size Of your 1st list : "))),_input_list(int(input("Enter Size Of your 2nd list : "))))}')

if __name__ == '__main__':
    main()

'''
test\ASSIGNMENT NO.4.py"

1) 10 : <class 'int'>

2) 4.5 : <class 'float'>

3) Hello World : <class 'str'>

4) True : <class 'bool'>

5) (1, 2, 3, 4, 5) : <class 'tuple'>

6) {'Amit': 12, 'Sumit': 14, 'Anil': 16} : <class 'dict'>

7) {1, 2, 4, 53, 6, 23, 8} : <class 'set'>

8) [23, 455, 6, 88, 'amit'] : <class 'list'>

Enter Size Of your list : 4
Enter data : Amit
Enter data : doke
Enter data : 121
Enter data : 96.5
['Amit', 'doke', '121', '96.5']

Enter Size Of your 1st list : 3
Enter data : Let
Enter data : Me
Enter data : 122
Enter Size Of your 2nd list : 3
Enter data : fish
Enter data : 134
Enter data : 29.2
[['Let', 'Me', '122'], ['fish', '134', '29.2']]
'''