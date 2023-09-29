cars = {'mercedez':'sedan','volvo':'saloon'}

def intro():
    print('welcome to the database')
    print("to get access enter your password")
    enter_password()
def enter_password(): 
    password = '123456'
    entry1 = input('Enter password:')
    if (len(entry1)< 3 and (entry1 != password)):
        print('Access denied!')
    else:
        print("Access Granted")
        data_base()
def data_base():
    x = int(input("clear(1), update(2), print(3) : "))
    if x == 1:
        cars.clear()
        print(cars)
        print("Database cleared")
    elif x==2:
        update_dictionary()
    elif x == 3:
        print(cars)

def update_dictionary():
    for i in range(3):
        name =input("Enter name 0f the car: ")
        desc = input("Enter the description: ")  
        cars[name] = desc   
        print(cars) 
        break   
intro()                              