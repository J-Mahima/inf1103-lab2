inventory = 0
error = 0
while True:
    stock = input("Enter a stock quantity: ")
    if stock.lower() == "quit" or (stock.isdigit() and int(stock) > 500):
        print("Total Units Processed: ", inventory)
        print("Number of Failed Entries: ", error)
        break
    elif stock.isdigit() and int(stock) > 0:
        stock = int(stock)
        inventory += stock
        continue
    else:
        error += 1
        print("Error: Please enter a valid number")
        continue



        