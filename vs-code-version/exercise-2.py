class String:
    def __init__(self, printStatment=[]):
        self.printStatment = printStatment

    def get_String(self):
        x = input("Type in something and we'll make it ALL UPPER CASE FOR YOU!\n")
        self.printStatment.append(x.upper())

    def print_String(self):
        if len(self.printStatment) == 0:
            print("You have not typed anything! Please enter - 1 to type something!")
        else:
            print(self.printStatment)

    def lower_it(self):
        if len(self.printStatment) == 0:
            print("You have not typed anything! Please enter - 1 to type something!")
        else:
            k = input(
                f"What Statment would you like to Reverse back to lower case?\n {self.printStatment}\n").upper()
            if k not in self.printStatment:
                print("Your statment entered was not found!")
            else:
                print(f'"{k}" has successfully been reversed!')
                n = k.lower()
                self.printStatment.remove(k)
                self.printStatment.append(n)

    def delete_String(self):
        if len(self.printStatment) == 0:
            print("You have not typed anything! Please enter - 1 to type something!")
        else:
            o = input(
                f"What Statment would you like to remove?\n Please copy and paste the statment, or type it as seen! This is case senstive!\n {self.printStatment}\n")
            if o not in self.printStatment:
                print("Your statment entered was not found!")
            else:
                print(f'"{o}" has successfully been removed!')
                self.printStatment.remove(o)

    def runIt(self):
        while True:
            z = int(input("Welcome to the CAPS LOCK program, is your CAPS LOCK and SHIFT key broken? What would you like to do?\n Type 1 - To type in something to make CAPS\n Type 2 - To print out your CAPS program!\n Type 3 - To reverse the CAPS and lower a selected statment!\n Type 4 - To Delete your String\n Type 0 - to Quit!\n"))
            if z == 1:
                self.get_String()
            elif z == 2:
                self.print_String()
            elif z == 3:
                self.lower_it()
            elif z == 4:
                self.delete_String()
            elif z == 0:
                print("Thanks for trying my program! Come again!")
                break
            else:
                print("INVALID CHOICE! TRY AGAIN")


sendit = String()
sendit.runIt()
