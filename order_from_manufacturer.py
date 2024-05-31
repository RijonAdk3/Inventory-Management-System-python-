import datetime

def order_laptop():
    # Ask for personal details
    try:
        name = input("Please enter the name of distributor: ")
        while not name.isalpha():
            print("Enter the name correctly without integer value")
            name=input("Please enter the name of distributor: ")
        
        address = input("Please enter your address: ")
        phone = int(input("Please enter your phone number: "))
        email = input("Enter the email for transaction: ")
        while "@" not in email:
            print("Invalid email please write correct email")
            email = input("Enter the email for transaction: ") 

    except:
        print("Invalid input. Please try again.")
        return

    # Ask for laptop ID and quantity to order
    while True:
            try:
                laptop_id = input("Please enter the name of the laptop you would like to order: ")
                quantity = int(input("Please enter the quantity you would like to order: "))
                break
            except:
                print("Invalid input. Please try again.")

    # Open the file in read mode and read the data into a list of dictionaries
    try:
        with open('laptop.txt', 'r') as file:
            laptops = []
            for line in file:
                laptop_details = line.strip().split(', ')
                laptops.append({
                    "name": laptop_details[0],
                    "brand": laptop_details[1],
                    "price": float(laptop_details[2].replace('$', '')),
                    "stock": int(laptop_details[3]),
                    "processor": laptop_details[4],
                    "graphics_card": laptop_details[5]
                })
    except:
        print("Error reading data from file.")
        return

    # Find the laptop with the given ID and update the stock
    laptop_found = False
    for laptop in laptops:
        if laptop["name"] == laptop_id:
            laptop["stock"] += quantity
            laptop_found = True
            break

    if not laptop_found:
        print("Laptop not found.")
        return

    # Write the updated data back to the file
    try:
        with open('laptop.txt', 'w') as file:
            for laptop in laptops:
                file.write("{}, {}, ${}, {}, {}, {}\n".format(
                    laptop["name"],
                    laptop["brand"],
                    laptop["price"],
                    laptop["stock"],
                    laptop["processor"],
                    laptop["graphics_card"]
                ))
    except:
        print("Error writing data to file.")
        return
    # Calculation of the total cost of order with VAT
    for laptop in laptops:
        if laptop["name"] == laptop_id:
            net_amount = laptop["price"] * quantity
            vat_amount = net_amount * 0.13
            gross_amount = net_amount + vat_amount

    # Generate bill with VAT in console and txt file
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y%m%d-%H%M%S")
    bill_filename = f"Orders_bill_{laptop_id}_{timestamp}.txt"

    # Generating bill with VAT in terminal / console
    print("|-------------------------------------------------------|")
    print("|                      Invoice Generated                |")
    print("|-------------------------------------------------------|")
    print("| \t\tName: {}\n| \t\tAddress: {}\n| \t\tPhone: {}\n| \t\tEmail: {}\n|".format(name, address, phone,email))
    print("|=======================================================|")
    print("| \t\tLaptop ordered: {}\n| \t\tQuantity: {}\n"
          "| \t\tTotal cost including 13% VAT: ${:.2f}\n"
          "| \t\tTotal cost without VAT: ${:.2f}\n"
          "| \t\tVAT Amount: ${:.2f}\n| ".format(laptop_id, quantity, gross_amount,net_amount,vat_amount))
    print("|=======================================================|")
    print("| \t\tOrder Date: {}\n| \t\tOrder Time: {}\n|".format(current_time.strftime("%Y-%m-%d"), current_time.strftime("%H:%M:%S")))
    print("|-------------------------------------------------------|")

    # generating the bill in txt file
    with open(bill_filename, 'w') as file:
        file.write("|-------------------------------------------------------|\n")
        file.write("|                   Invoice Generated                   |\n")
        file.write("|-------------------------------------------------------|\n")
        file.write("| \t\t\tName: {}                                              \n".format(name))
        file.write("| \t\t\tAddress: {}                                            \n".format(address))
        file.write("| \t\t\tPhone: {}                                             \n".format(phone))
        file.write("| \t\t\tEmail: {}                                              \n".format(email))
        file.write("|=======================================================|\n")
        file.write("| \t\t\tLaptop ordered: {}                                    \n".format(laptop_id))
        file.write("| \t\t\tQuantity: {}                                          \n".format(quantity))
        file.write("| \t\t\tTotal cost (with 13% VAT): ${:.2f}               \n".format(gross_amount))
        file.write("| \t\t\tTotal cost (with out 13% VAT): ${:.2f}               \n".format(net_amount))
        file.write("| \t\t\tVAT Amount: ${:.2f}               \n".format(vat_amount))
        file.write("|=======================================================|\n")
        file.write("| \t\t\tOrder Date: {}                                        \n".format(current_time.strftime("%Y-%m-%d")))
        file.write("| \t\t\tOrder Time: {}                                        \n".format(current_time.strftime("%H:%M:%S")))
        file.write("|-------------------------------------------------------|\n")

    print("Bill generated successfully! Please check {} for the details.".format(bill_filename))