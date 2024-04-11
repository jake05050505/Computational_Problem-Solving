from memory_profiler import profile
# from prettytable import PrettyTable # Used for task 2

# Used for task 2
# viewinventory = PrettyTable(['1: Adhesive tape','2: Alcohol wipes','3: Antihistamine tablets','4: Elastic Bandages','5: Epinephrine Injector (EpiPen)']) # Inventory
# viewinventory.add_row(['6: Gloves (latex)','7: Gloves (non-latex)','8: Hydrogen peroxide solṉ','9: Instant cold packs','10: Paracetomol & Ibuprofen'], divider=True)
# viewinventory.add_row(['11: Plasters','12: Scissors','13: Sterile Gauze Pads','14: Thermometers','15: Tweezers'], divider=True)
# inventory={1:'Adhesive tape',2:'Alcohol wipes',3:'Antihistamine tablets',4:'Elastic Bandages',5:'Epinephrine Injector (EpiPen)',6: 'Gloves (latex)',7:'Gloves (non-latex)',8:'Hydrogen peroxide soln',9:'Instant cold packs',10:'Paracetomol & Ibuprofen',11: 'Plasters',12:'Scissors',13:'Sterile Gauze Pads',14:'Thermometers',15:'Tweezers'}

orders={} # Initialize new dictionaries to prevent errors
s_orders={}

def fetch(): # reads all data from respective orderslist.txt and formats it into dictionaries with int key and list value
    with open('orderslist.txt','r') as f:       # reads orderslist.txt and converts into machine-readable format
        lines=f.read().splitlines()
        for i in range(len(lines)):
            id=int(lines[i].split(':')[0])                  # splits the ID and items, converts list index 0 (ID) to int
            items=lines[i].split(':')[1].split(',')    # splits ID and items, takes list index 1 (items) and splits by ', '; outputs a list of items
            orders[id] = items

def findnextindex():    # Find next available index in orders to add an value to AFTER fetch() has been completed
    try:                # this try,except statement returns 0 if there are no pairs in the dictionary to check
        for index in range(len(orders)):
            if index not in orders:
                return index
        return index+1
    except UnboundLocalError:
        return 0
    except KeyError: # This error shouldn't be raised under normal conditions.
        print('fni() KeyError') # Informs the user that there was a KeyError in findnextindex() - fni() shorthand
        quit() # Just a failsafe, if something were to happen such as orderslist.txt being erased after an error, this stops it.

def getitems(): # Asks for five inputs and gets five inputs, if an erroneous or invalid input ever occurs, calls and restarts fn, getting 5 new inputs
    items=[]
    print('Please enter five items.')
    try:
        for i in range(5):
            items.append(str(input('>>>')))
    except ValueError:
        print('ValueError')
        getitems()
    except KeyError:
        print('KeyError')
        getitems()
    return items

def getindex(): # Used in delete order
    try:
        print('Please enter your order ID')
        i = int(input('>>>'))
        orders[i]
        return i
    except KeyError:
        print('KeyError')
        getindex()
    except ValueError:
        print('ValueError')
        getindex()

def writeto(): # Wipes orderslist.txt and writes all existing and new orders
    s_orders = dict(sorted(orders.items()))
    with open('orderslist.txt','w') as f:
        for i in s_orders:
            f.write(str(i)+':'+s_orders[i][0]+',')
            f.write(s_orders[i][1]+',')
            f.write(s_orders[i][2]+',')
            f.write(s_orders[i][3]+',')
            f.write(s_orders[i][4])
            f.write('\n')

def modifyorder(index,items):
    orders[index]=items
    writeto()

def printall(): # Print orders dictionary
    for i in orders:
        print(i,orders[i])

#@profile
def main():
    # fetch() # see comment under this function
    choice = input('Menu\n[1]Create Order\n[2]Modify Order\n[3]Delete Order\n[4]View Orders\n[0]Quit\n>>>')

    # Create and Modify both call functions with their respective names because they take items as an input, this was done in an attempt to visually clean up script
    if choice == '1': # Create Order
        items=[]
        id = findnextindex()
        # print(viewinventory) # Only used in task 2
        items = getitems()
        modifyorder(id,items)

    elif choice == '2': # Modify Order or Create order using custom ID
        printall()
        index = getindex()
        # print(viewinventory)
        items=getitems()
        modifyorder(index,items)

    elif choice == '3': # Delete Order
        printall()
        index = getindex()
        confirmation = str(input(f'Please type \"CONFIRM\" to delete order {index}\n>>>'))
        if confirmation == 'CONFIRM':
            orders.pop(index)
            print(f'Order {index} was deleted.')
        else: print(f'Order {index} was not deleted.')
        writeto()

    elif choice == '4': # View Orders
        printall()
        # index=getindex() # for viewing single order if orders list won't be shown to user
        # print(index,orders[index])

    elif choice == '5': # skip to anything written outside the if statement - hidden
        pass

    elif choice == '0':
        quit()

    else: # If the choice is invalid, calls and restarts main(). 
        print('Invalid choice')
        main()

    # main() # see comment below

if __name__ == '__main__':
    fetch()
    main()
    # Can be looped if main is called at the end of main() making the program an infinite loop until choice 0 is chosen (Quit), saves all after every iteration.
    # fetch() should also be called at the start of main() in order to do this^