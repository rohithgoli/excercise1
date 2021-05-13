import csv

print("Welcome")
print("Enter 1 to write data")
print("Enter 2 to search data")

user_choice = input()

if user_choice=='1':
    print("Enter data and after completion enter -1")
    is_terminated = False
    while (is_terminated==False):
        data = input()
        if data=='-1':
            is_terminated = True
            break
        else:
            data = data.split(",")
            with open('users.csv','a+',newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)
elif user_choice=='2':
    print("Enter search value:")
    search_value = input()
    count = 0
    with open('users.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if search_value in line:
                print(line)
                count+=1
        if count==0:
            print("No results found matching search value")
        else:
            print(f"{count} results found")
else:
    print("Error!!! Choice does not exist")
