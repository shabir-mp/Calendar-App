import calendar, os, time

print("\033[34mCALENDAR APP \033[0m")
print("\033[30m©2024 ShabirMP Programming Project \033[0m")
time.sleep(4)
os.system("clear")

def print_calendar(year, month):
    print(calendar.month(year, month))

while True:
    os.system("clear")
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    if month > 12 or month < 1 :
        print("\033[41mMonth Not Available. Please Try Again \033[0m")
        time.sleep(2)
        os.system("clear")
        continue
    time.sleep(1)
    os.system("clear")
    print_calendar(year, month)
    
    while True:
        print()
        answer = input("Check another date? (y/n): ").lower().strip()
        if answer == 'y':
            break
        elif answer == 'n':
            os.system("clear")
            print("Thakyou For Using Calendar App")
            exit()
        else:
            print("Please enter 'y' or 'n'.")
