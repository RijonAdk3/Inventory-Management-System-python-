import time

def sell_To_customer():
    # Ask for personal details
    try:
        name = input("Please enter your name: ")
        while not all(c.isalpha() or c.isspace() for c in name):
            print("Please enter the name properly")
            name = input("Please enter your name: ")
        address = input("Enter your address: ")
        phone = input("Enter your phone number: ")
    except:
        print("Invalid input. Please try again.")
        return
    
    # Opening file in read mode and storing the data into a dictionary laptops
    laptops = {}
    try:
        with open('laptop.txt', 'r') as file:
            for line in file:
                laptop_details = line.strip().split(', ')
                laptop_id = laptop_details[0].lower().replace(" ", "_")
                laptops[laptop_id] = {
                    'name': laptop_details[0],
                    'brand': laptop_details[1],
                    'price': laptop_details[2],
                    'quantity': int(laptop_details[3]),
                    'processor': laptop_details[4],
                    'graphics_card': laptop_details[5]
                }
    except FileNotFoundError:
        print("File not found. Please make sure that the file exists and try again.")
        return
    
    # Ask for laptop name and quantity to buy
    while True:
        laptop_id = input("Enter the name of the laptop you want to buy: ").lower().replace(" ", "_")
        if laptop_id not in laptops:
            print("Invalid laptop , please try again.")
        else:
            break
    while True:
        try:
            quantity = int(input("Enter the quantity you want to buy: "))
            if quantity <= 0:
                print("Invalid quantity, please enter a positive integer.")
            elif quantity > laptops[laptop_id]['quantity']:
                print(f"Sorry, we only have {laptops[laptop_id]['quantity']} {laptops[laptop_id]['name']} available.")
            else:
                break
        except ValueError:
            print("Invalid quantity, please enter a positive integer.")
    
    # Asking the customer for shipped or not
    while True:
        try:
            shipped = input("Do you want the laptop to be shipped? (yes/no) ").lower()
            if shipped == "yes":
                shipping_cost = 50
                break
            elif shipped == "no":
                shipping_cost = 0
                break
            else:
                print("Invalid input, please enter 'yes' or 'no'.")
        except:
            print("An error occurred. Please try again.")
    
    # Calculating the total cost

    price = float(laptops[laptop_id]['price'].replace("$", ""))
    total_price_of_quantity_sold = price * quantity
    total_without_shipping = total_price_of_quantity_sold
    total = total_price_of_quantity_sold + shipping_cost

    # Generate the bill
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    bill_filename = f"{laptops[laptop_id]['name']}-{timestamp}.txt"

    #generate the bill in console
    print("|--------------------------------------------------|")
    print("|                   Invoice Generated              |")
    print("|--------------------------------------------------|")
    print("| Customer Name: {}".format(name))
    print("| Address: {}".format(address))
    print("| Phone: {}".format(phone))
    print("|--------------------------------------------------|")
    print("| Laptop: {} ({})".format(laptops[laptop_id]['name'], laptops[laptop_id]['brand']))
    print("| Quantity: {}".format(quantity))
    print("| Price: {} x {} = ${:.2f}".format(laptops[laptop_id]['price'], quantity, total_price_of_quantity_sold))
    print("|--------------------------------------------------|")
    print("| Shipping cost: ${:.2f}".format(shipping_cost))
    print(("| Total (including shipping cost): ${:.2f}\n".format(total)))
    print("| Total (without shipping cost): ${:.2f}\n".format(total_without_shipping))
    print("|--------------------------------------------------|")
    print("| Date of purchase: {}".format(time.strftime('%Y-%m-%d')))
    print("| Time of purchase: {}".format(time.strftime('%H:%M:%S')))
    print(" -------------------------------------------------- ")

    #generate the bill in txt file after a sell
    with open(bill_filename, 'w') as file:
        file.write("|---------------------------------------------------|\n")
        file.write("|                   Invoice Generated               |\n")
        file.write("|---------------------------------------------------|\n")
        file.write("| \t\tName: {}\n| \t\tAddress: {}\n| \t\tPhone: {}\n|\n".format(name, address, phone))
        file.write("|---------------------------------------------------|\n")
        file.write("| Laptop: {} ({})\n".format(laptops[laptop_id]['name'], laptops[laptop_id]['brand']))
        file.write("| Quantity: {}\n".format(quantity))
        file.write("| Price: {} x {} = ${:.2f}\n".format(laptops[laptop_id]['price'], quantity, total_price_of_quantity_sold))
        file.write("|---------------------------------------------------|\n")
        file.write("| Total (without shipping cost): ${:.2f}\n".format(total_without_shipping))
        file.write("| Shipping cost: ${:.2f}\n".format(shipping_cost))
        file.write("| Total (including shipping cost): ${:.2f}\n".format(total))
        file.write("|---------------------------------------------------|\n")
        file.write("| Date of purchase: {}\n".format(time.strftime('%Y-%m-%d')))
        file.write("| Time of purchase: {}\n".format(time.strftime('%H:%M:%S')))
        file.write("|---------------------------------------------------|\n")


# Update the laptop quantity in the dictionary
    laptops[laptop_id]['quantity'] -= quantity

# Write the updated values back to the text file without changing the format
    with open('laptop.txt', 'w') as file:
        for laptop_id, laptop_details in laptops.items():
            line = f"{laptop_details['name']}, {laptop_details['brand']}, {laptop_details['price']}, {laptop_details['quantity']}, {laptop_details['processor']}, {laptop_details['graphics_card']}\n"
            file.write(line)

