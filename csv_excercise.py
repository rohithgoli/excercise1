import csv

def count_lines():
    existing_lines = 0
    with open('users.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            existing_lines+=1
    return existing_lines

def write_data():
    existing_lines = count_lines()
    print("Enter data")
    is_terminated = False
    while (is_terminated==False):
        data = input()
        if data=='':
            is_terminated = True
            break
        else:
            data = data.split(",")
            with open('users.csv','a+',newline='') as csv_file:
                fieldnames = ['Name','Age','Gender','email']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                if existing_lines==0:
                    writer.writeheader()
                writer.writerow({'Name':data[0], 'Age':data[1], 'Gender':data[2], 'email':data[3]})

def read_data():
    print("Enter column name to search:")
    search_column = input()
    print("Enter search value:")
    search_value = input()
    count = 0
    with open('users.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if search_value in row[search_column]:
                print(row)
                count+=1
        if count==0:
            print("No results found matching search value")
        else:
            print(f"{count} results found")
        
        
def do_task():
    print("Welcome")
    print("Enter 1 to write data")
    print("Enter 2 to search data")
    
    user_choice = input()

    if user_choice=='1':
        write_data()
    elif user_choice=='2':
        read_data()
    else:
        print("Error!!! Choice does not exist \n Please enter valid choice")
        do_task()

try:
    do_task()
except FileNotFoundError:
    print(":( File does not exist !!!")
except KeyError:
    print(":( Column does not exist !")
except:
    print("Sorry :( an exception occured")
