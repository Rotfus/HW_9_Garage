#import
from enum import Enum
import os
import csv

#Methods (enum)
#Add
#Delete
#print
#search
#exit

class Actions(Enum):
    PRINT = 0
    ADD = 1
    DELETE = 2
    SEARCH = 3
    UPDATE = 4
    EXIT = 6

cars=[]
#save function
def save_to_csv():
    with open("cars.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(cars)
      

#the display in the terminal
def display_menu():
    for x in Actions: print(f'{x.value} - {x.name}')
    return Actions(int(input('Your selection:')))



def main():
    while(True):
        user_selection=display_menu()
        if user_selection== Actions.PRINT: print(cars)
        if user_selection== Actions.ADD: cars.append({"brand":input("Please enter car brand"), "model":input("Please enter car model"), "color":input("Please enter car color")})
        if user_selection== Actions.EXIT: return 
        #update, del, and search not implemented yet.




if __name__=='__main__':
    main()
    save_to_csv()
    print("Thank you for visiting the garage :)")