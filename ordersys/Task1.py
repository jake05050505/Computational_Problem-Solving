#todo: sort orders list before printing - add to writeto() or fetch()

from memory_profiler import profile
from prettytable import PrettyTable
from collections import OrderedDict

viewinventory = PrettyTable(['1: Adhesive tape','2: Alcohol wipes','3: Antihistamine tablets','4: Elastic Bandages','5: Epinephrine Injector (EpiPen)']) # Inventory
viewinventory.add_row(['6: Gloves (latex)','7: Gloves (non-latex)','8: Hydrogen peroxide solṉ','9: Instant cold packs','10: Paracetomol & Ibuprofen'], divider=True)
viewinventory.add_row(['11: Plasters','12: Scissors','13: Sterile Gauze Pads','14: Thermometers','15: Tweezers'], divider=True)
#print(viewinventory)
inventory={1:'Adhesive tape',2:'Alcohol wipes',3:'Antihistamine tablets',4:'Elastic Bandages',5:'Epinephrine Injector (EpiPen)',6: 'Gloves (latex)',7:'Gloves (non-latex)',8:'Hydrogen peroxide soln',9:'Instant cold packs',10:'Paracetomol & Ibuprofen',11: 'Plasters',12:'Scissors',13:'Sterile Gauze Pads',14:'Thermometers',15:'Tweezers'}

orders={} # Initialize new dictionaries to prevent errors

def fetch():
    with open('orderslist.txt','r') as f:       # reads orderslist.txt and converts into machine-readable format
        lines=f.read().splitlines()
        for i in range(len(lines)):
            id=int(lines[i][0].split(': ')[0])   # function scope # splits the ID from start of list, converts list index 0 (ID) to int
            items=lines[i][2:].split(', ')      # removes first two characters and splits by ', '; outputs a list of items
            orders[id] = items
    for i in lines:
        orders[id]=items

def findnextindex():    # Find next available index in orders to add an value to
    try:                # this try,except statement returns 0 if there are no pairs in the dictionary to check, used for debugging as the dictionary should never be empty (it should contain index=None for empty entries)
        for index in range(len(orders)):
            if index not in orders:
                print(index)
                return index
    except KeyError:
        print('KeyError')
    except UnboundLocalError:
        print('UnboundLocalError')

def createorder(items):
    id = findnextindex()
    orders[id]=items
    #print(f'createorder{orders}')
    # with open('orderslist.txt','a') as f:
    #     f.write(id,orders[id])

def getitems():
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
        valid = orders[i]
        print(valid)
    except KeyError:
        print('KeyError')
        getindex()
    except ValueError:
        print('ValueError')
        getindex()

def modifyorder(index,items):
    orders[index]=items

def printall(): # Print orders dictionary
    for i in orders:
        print('printall',i,orders[i])

def writeto():
    s_orders = OrderedDict(sorted(orders.items()))
    with open('orderslist.txt','w')as f:
        for i in s_orders:
            if s_orders[i]!=None:
                f.write(str(i)+':'+s_orders[i][0]+', ')
                f.write(s_orders[i][1]+', ')
                f.write(s_orders[i][2]+', ')
                f.write(s_orders[i][3]+', ')
                f.write(s_orders[i][4])
                f.write('\n')
            else: continue

#@profile
def main():
    fetch()
    choice = input('Menu\n[1]Create Order\n[2]Modify Order\n[3]View Order\n[4]Delete Order\n[0]Cancel\n>>>')

    if choice == '1': # Create Order
        items=[]
        print('Please select an item from the table below, you will need to add five items.')
        print(viewinventory)
        items = getitems()
        createorder(items)
        writeto()

    elif choice == '2': # Modify Order
        index = int(input('Please enter your order ID\n>>>'))
        items=getitems()
        modifyorder(index,items)
        writeto()

    elif choice == '3': # View Order
        index=getindex()
        print(index,orders[index])

    elif choice == '4': # Delete Order
        index = int(input('Please enter your order ID\n>>>'))
        confirmation = str(input(f'Please type \'CONFIRM\' to  delete order {index}\n>>>'))
        if confirmation == 'CONFIRM':
            orders[index]=None
            print(f'Order {index} was deleted.')
        else: print(f'Order {index} was not deleted.')
        writeto()

    elif choice == '5':
        pass

    elif choice == '0':
        quit()

    else:
        print('Invalid choice')
        main()
    
    for i in orders:
        print(orders.items())

if __name__ == '__main__':
    main()