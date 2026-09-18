def get_valid_input():
    stock = input("Enter a stock quantity: ")
    return stock
def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    tax_rate = 0.10
    return tax_rate * amount

def generate_report(total_units, failed_attempts):
    print("Total Units Processed: ", total_units)
    print("Number of Failed Entries: ", failed_attempts)


inventory = 0
error = 0

while True:
    stock = input("Enter a stock quantity: ")

    if stock.lower() == "quit": 
        print("Total Units Processed: ", inventory)
        print("Number of Failed Entries: ", error)
        break
    
    elif stock.isdigit() and int(stock) > 0:

        if int(stock) + inventory > 500:
            error += 1
            print("Alert! Stock input exceeds maximum inventory capacity of 500 units.")
            print("Total Units Processed: ", inventory)
            print("Number of Failed Entries: ", error)
            break

        inventory += int(stock)
        tax_amount = tax(inventory)
        
    else:
        error += 1
        print("Error: Please enter a valid number")
        continue



        