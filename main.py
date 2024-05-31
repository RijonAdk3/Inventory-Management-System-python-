
from laptop_details import display_laptops
from order_from_manufacturer import  order_laptop
from sell_laptop import sell_To_customer
from welcome_message import print_welcome

# main py file to call all functions
def main():
    print_welcome()
    while True:
        choice = input("Please enter your choice (1-4): ")
        if choice == '1':
                display_laptops()
        elif choice == '2':
                    order_laptop()
        
        elif choice == '3':
                while True:
                    sell_To_customer()
                    another_sale = input("Do you want to buy some more laptop ? (Yeah/no)")
                    if another_sale.lower()=="no":
                        break

        elif choice == '4':
                print("Thank you for choosing our Laptop Shop!")
                break
        else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
 main()
