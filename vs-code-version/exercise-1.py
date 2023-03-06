# Create a class called cart that retains items and has methods to add, remove, and show

class Cart:
    def __init__(self, inCart=[], totalItems=[]):
        self.inCart = inCart
        self.totalItems = totalItems

    def addToCart(self):
        x = input("What would you like to add to your cart?\n")
        self.inCart.append(x.strip())
        y = int(input(f"How many {x.strip()}'s would you like?\n"))
        self.totalItems.append(y)

    def showCart(self):
        u = sum(self.totalItems)
        print(
            f"Here are your items the cart so far!\nYou have {u} total items!")
        for i in self.inCart:
            print(i)
        for p in self.totalItems:
            print(p)

    def deleteCart(self):
        if len(self.inCart) == 0:
            print("Your cart us empty! You will need to add items to remove!")
        else:
            z = input(
                f"Please select from the following items to remove!\n {self.inCart}\n")
            q = int(input(f"Please select how many you had.\n {self.totalItems}\n"))
            if z not in self.inCart or q not in self.totalItems:
                print("Not a valid entry! Try again!")

            else:
                self.inCart.remove(z)
                self.totalItems.remove(q)

    def runIt(self):
        while True:
            r = int(input("Welcome to Bruce Mart! What would you like to do?\n Type 1 - to Add to your cart! \n Type 2 - to Show your cart! \n Type 3 - to Remove something form your cart!\n Type 0 - to Quit!\n"))
            if r == 1:
                self.addToCart()

            elif r == 2:
                self.showCart()

            elif r == 3:
                self.deleteCart()

            elif r == 0:
                print("Thanks you for shopping at Bruce Mart! See you next time!")
                break

            else:
                print("INVALID!")


test = Cart()
test.runIt()
