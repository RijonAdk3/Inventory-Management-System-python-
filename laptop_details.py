def display_laptops():
    # Open the file in read mode
    with open('laptop.txt', 'r') as file:
        print("--------------------================== Available laptops are: =================-----------------------------")
        print("-" * 108)
        # Print the heading for each column
        print("|{:<20}|{:<20}|{:<10}|{:<10}|{:<20}|{:<20} |".format("Laptop Name", "Brand", "Price", "Quantity", "Processor", "Graphics Card"))
        # Looping through each of line in the file
        print("-" * 108)
        for line in file:
            # Split the line into separate values
            laptop_details = line.strip().split(', ')
            laptop_details[2] = laptop_details[2].replace("$", "")
            # Print the values in a formatted table row
            print("|{:<20}|{:<20}|{:<10}|{:<10}|{:<20}| {:<20}|".format(laptop_details[0], laptop_details[1], laptop_details[2], 
                                                                        laptop_details[3], laptop_details[4], laptop_details[5]))
        print("-" * 108)