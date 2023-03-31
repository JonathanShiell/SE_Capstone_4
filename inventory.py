
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        # Let us cast cost and quantity to numeric types if possible
        # We will try to cast price to integer, then float

        # Try/except then raise allows for a more appropriate error message.
        try:
            cost = int(cost)
        except ValueError:
            try:
                cost = float(cost)
            except:
                raise ValueError("Cost cannot be cast to a valid numeric value")

        # Let us cast quantity to an integer. Otherwise it is not valid
        try:
            quantity = int(quantity)
        except:
            raise ValueError("Quantity cannot be cast to a valid numeric value")
        try:
            assert quantity > 0
        except AssertionError:
            raise ValueError("Quantity must be a positive integer")

        # Floating-point types are inappropriate for quantity unless their value is 
        # equivalent to a positive integer. Therefore only integer casting is 
        # attempted for quantity.

        # Finally, let us set the object attributes    
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        """Does not accept any arguments when called

        Returns the cost of the shoe
        
        """    
        return self.cost

    def get_quantity(self):
        """Does not accept any arguments when called

        Returns the quantity of shoes on hand as an integer
        """
        return self.quantity

    def __str__(self):
        """
        Returns a string representation of a class.

        This is achieved by joining the strings of the attributes with a 
        single comma using the string.join method, to produce the same format as the file.
        """
        return ','.join((self.country, self.code, self.product, str(self.cost), str(self.quantity)))


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # Read in the file data
    filename = "inventory.txt"
    with open(filename, "rt") as f:
        file_input = f.read()

    items_file = file_input.split('\n')

    for i, item in enumerate(items_file):
        # Skip first line
        if not i:
            continue
        # Split line describing item item, then map to a new instance of a Shoe object
        try:
            item_args = item.split(',')
            new_shoe = Shoe(*item_args)
            shoe_list.append(new_shoe)
        except:
            pass


def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    new_code = input("Please enter the product code:")
    new_product = input(f"Please enter the product name for {new_code}:")
    new_country = input(f"Please enter the country for {new_code}:")
    new_cost = input(f"Please enter the sale cost of {new_code}:")
    new_quantity = input(f"Please enter the quantity of {new_code}:")

    # Instantiate new instance of shoe object
    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)

    # Append to `shoe_list`
    shoe_list.append(new_shoe)

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        print(str(shoe))

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Get lowest stock level
    lowest_stock = min(shoe.get_quantity() for shoe in shoe_list)

    # Initialise lowest_shoe as None
    lowest_shoe = None

    # Find shoe
    for shoe in shoe_list:
        if shoe.get_quantity() == lowest_stock:
            lowest_shoe = shoe
        
    #First print result:
    print("Lowest quantity shoe:")
    print(str(lowest_shoe))

    # Offer to restock
    restock = input("Do you wish to restock? (Y)es/No?")

    # Quit function and return control flow from function if not restocking
    if not restock.lower().startswith("y"):
        return

    # Get restock code
    restock_code = lowest_shoe.code

    # If restocking, obtain stock to add as integer
    restock_amount = int(input("How many would you like to add to the stock? "))

    # Add to stock
    lowest_shoe.quantity += restock_amount
    filename = "inventory.txt"

    # Iterate through file, re-write other lines as is but change stock line.
    # Start by reading in shoe file
    with open(filename, "rt") as f:
        file_input = f.read()

    # Get list of shoe strings from file as read in
    items_file = file_input.split('\n')

    # Write blank over shoes_file
    with open(filename, "wt") as f:
        f.write("")

    # Instantiate line counter
    line_counter = 0

    # Iterate over shoe, re-write with shoe attributes and '\n' if not being restocked
    # Change quantity then re-write otherwise.
    for shoe_line in items_file:
        country,code,product,cost,quantity = shoe_line.split(",")

        # Write '\n' if after first line, increment `line_counter`
        if line_counter:
            with open(filename, "at") as f:
                f.write("\n")
        line_counter += 1

        #Write directly back to file if code does not match
        if code != restock_code:
            with open(filename, "at") as f:
                f.write(shoe_line)

        # If code matches (using else) write updated description
        else:
            with open(filename, "at") as f:
                f.write(str(lowest_shoe))  
    

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    shoe_code = input("Please enter the shoe code: ")

    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(str(shoe))

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(shoe.product+",", "code:", shoe.code, "value of stock is", value)

def highest_qty():
    pass
    '''
    To determine the product with the highest quantity and print this shoe as 
being for sale. May print multiple shoes if they both/all have the same (highest) 
stock level.
    '''
    # Get maximum stock
    highest_amount = max(shoe.get_quantity() for shoe in shoe_list)

    # Iterate over shoe_list, print those with highest amount
    for shoe in shoe_list:
        if shoe.get_quantity() == highest_amount:
            print(shoe.product+",", "code:", shoe.code, "is for sale.")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Read in shoe data before menu:
read_shoes_data()
# Print message:
print("Shoe data read in OK")
print("Stored at inventory.txt in comma-separated format")

menu_message = """Please select an option:
v = View all shoes
e = Enter new shoe type
r = get least-stocked shoe, restock if required
s = search for shoe by code
a = get value for shoes in stock
h = get the most-stocked shoe type(s)
q = quit
"""

# Add formatting to menu message
menu_message = "="*80 + "\n\n" + menu_message + "\n\n" + "="*80 + "\n"

while True:
    print("="*80 + "\n") # Print spacing/formatting.
    print(f"Shoe data read in OK with {len(shoe_list)} shoe types.\n") # Print pre-message with empty line.
    option = input(menu_message).lower()[0] # Take first character only as lower case.
    # Print spacer
    print("="*80 + "\n") # Print spacing/formatting.

    # View shoes if so asked:
    if option == "v":
        view_all()
        print(); print() # Print lines after to clear.

    # Allow to enter/capture new shoe
    elif option == "e":
        # Run in try/except to handle user errors
        try:
            capture_shoes()
        except:
            print("Input Error")

        print() # Single line to clear afterwards

    # Allow user to re-stock
    elif option == "r":
        re_stock()
        print(); print() # Print lines after to clear.

    # Allow user to search by code
    elif option == "s":
        seach_shoe()
        print() # Print single line after to clear.

    # Allow user to obtain value of stock
    elif option == "a":
        value_per_item()
        print(); print() # Print lines after to clear.

    # Allow user to get the highest quantity
    elif option == "h":
        highest_qty()
        print() # Print single line after to clear.

    # Implement exit option:
    elif option == "q":
        break

    # Return around loop without valid option
    else:
        continue
