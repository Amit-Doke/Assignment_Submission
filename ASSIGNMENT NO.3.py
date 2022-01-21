'''
ASSIGNMENT NO.3 (DAY 3)
Email: amitdoke121@gmail.com
'''
def Display_user(_user):
    print("######Details of User######")
    i=0
    while True:
        print('Customer No.', i+1)
        _len=len(_user[i])
        for item in range(_len):
            print(_user[i][item])
            
        if(input("Do you want to continue (y/n) : ") == 'y'):
            i+=1
        else:
            print("Thank You For using Service")
            break        
                
    return
def main():
    user_data=[]
    while True:
        _data=[]
        _data.append(input('Enter your Name : '))
        _data.append(input('Enter your Email : '))
        _data.append(input('Enter your Age : '))
        _data.append(input('Enter your Birth Date : '))
        _data.append(input('Enter your Studied at : '))
        _data.append(input('Enter your Phone Number : '))
        _data.append(input('Enter your Country : '))
        user_data.append(_data)
        del _data
        if(input("Do you want to continue (y/n) : ") == 'y'):
            continue
        else:
            break
    
   
    Display_user(user_data)
    
if __name__ == '__main__':
    main()
    
'''
test\ASSIGNMENT NO.3.py"
Enter your Name : Amit Doke
Enter your Email : amitdoke121@gmail.com
Enter your Age : 21
Enter your Birth Date : 07/09/2000
Enter your Studied at : SPPU
Enter your Phone Number : 9534562551
Enter your Country : India
Do you want to continue (y/n) : y
Enter your Name : Sumit Pawar
Enter your Email : sumitpawar007@gmail.com
Enter your Age : 21
Enter your Birth Date : 08/03/2000
Enter your Studied at : SPPU
Enter your Phone Number : 9855612231
Enter your Country : India
Do you want to continue (y/n) : n
######Details of User######
Customer No. 1
Amit Doke
amitdoke121@gmail.com
21
07/09/2000
SPPU
9534562551
India
Do you want to continue (y/n) : y
Customer No. 2
Sumit Pawar
sumitpawar007@gmail.com
21
08/03/2000
SPPU
9855612231
India
Do you want to continue (y/n) : n
Thank You For using Service
'''