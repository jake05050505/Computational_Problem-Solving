from memory_profiler import profile
from prettytable import PrettyTable

viewinventory = PrettyTable(['1: Adhesive tape','2: Alcohol wipes','3: Antihistamine tablets','4: Elastic Bandages','5: Epinephrine Injector (EpiPen)']) # Inventory
viewinventory.add_row(['6: Gloves (latex)','7: Gloves (non-latex)','8: Hydrogen peroxide solṉ','9: Instant cold packs','10: Paracetomol & Ibuprofen'], divider=True)
viewinventory.add_row(['11: Plasters','12: Scissors','13: Sterile Gauze Pads','14: Thermometers','15: Tweezers'], divider=True)
#print(viewinventory)
inventory={1:'Adhesive tape',2:'Alcohol wipes',3:'Antihistamine tablets',4:'Elastic Bandages',5:'Epinephrine Injector (EpiPen)',6: 'Gloves (latex)',7:'Gloves (non-latex)',8:'Hydrogen peroxide soln',9:'Instant cold packs',10:'Paracetomol & Ibuprofen',11: 'Plasters',12:'Scissors',13:'Sterile Gauze Pads',14:'Thermometers',15:'Tweezers'}

orders={} # Initialize new dictionaries to prevent errors
s_orders={}

def fetch():
    with open('orderslist.txt','r') as f:       # reads orderslist.txt and converts into machine-readable format
        lines=f.read().splitlines()
        for i in range(len(lines)):
            id=int(lines[i].split(':')[0])               # splits the ID and items, converts list index 0 (ID) to int
            items=lines[i].split(':')[1].split(',')      # removes first two characters and splits by ', '; outputs a list of items
            orders[id] = items
    for i in lines:
        orders[id]=items

def findnextindex():    # Find next available index in orders to add an value to
    try:                # this try,except statement returns 0 if there are no pairs in the dictionary to check, used for debugging as the dictionary should never be empty (it should contain index=None for empty entries)
        for index in range(len(orders)):
            if index not in orders:
                return index
        return index+1
    except KeyError: # this error should NEVER be raised, program quits if it is.
        print('fni() KeyError')
        quit()
    except UnboundLocalError:
        return 0

def getitems(): # prompts input for five items
    items=[]
    print('Please enter five items.')
    try:
        for i in range(5):
            items.append(inventory[(int(input('>>>')))])
    except ValueError:
        print('ValueError')
        getitems()
    except KeyError:
        print('KeyError')
        getitems()
    return items

def getindex():
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

def printall(): # Print orders dictionary
    for i in orders:
        print(i,orders[i])

def writeto():
    s_orders = dict(sorted(orders.items()))
    with open('orderslist.txt','w') as f:
        for i in s_orders:
            f.write(str(i)+':'+s_orders[i][0]+', ')
            f.write(s_orders[i][1]+', ')
            f.write(s_orders[i][2]+', ')
            f.write(s_orders[i][3]+', ')
            f.write(s_orders[i][4])
            f.write('\n')

def createorder(items):
    id = findnextindex()
    modifyorder(id,items)

def modifyorder(index,items):
    orders[index]=items

#@profile
def main():
    # fetch() see bottom of program
    choice = input('Menu\n[1]Create Order\n[2]Modify Order\n[3]Delete Order\n[4]View Order\n[0]Cancel\n>>>')

    if choice == '1': # Create Order
        items=[]
        print('Please select an item from the table below, you will need to add five items.')
        print(viewinventory)
        items = getitems()
        createorder(items)
        writeto()

    elif choice == '2': # Modify Order
        printall()
        index = getindex()
        print(orders[index])
        items=getitems()
        modifyorder(index,items)
        writeto()

    elif choice == '3': # Delete Order
        printall()
        index = getindex()
        confirmation = str(input(f'Please type \"CONFIRM\" to  delete order {index}\n>>>'))
        if confirmation == 'CONFIRM':
            orders.pop(index)
            print(f'Order {index} was deleted.')
        else: print(f'Order {index} was not deleted.')
        writeto()

    elif choice == '4': # View Order
        printall()

    elif choice == '5': # used to run whatever is outside if statement - hidden (selects no option)
        pass

    elif choice == '0':
        quit()

    else:
        print('Invalid choice')
        main()

        # main() # see comment below

if __name__ == '__main__':
    fetch()
    main()
    # can be run infinitely if main() is called at the end of main() (thus recursive) and will continue until option 0 is selected (Quit), list is updated after every iteration
    # for this to work fetch must also be called at the start of main()
