# ==================== WAREHOUSE INVENTORY LIST ====================

stock = {
    'A1' : {
        'Product' : 'Macbook',
        'Price' : 1299,
        'Supplier' : 'Erafone',
        'Qty' : 25
    },
    'A2' : {
        'Product' : 'iPhone',
        'Price' : 799,
        'Supplier' : 'iBox',
        'Qty' : 50
    },
    'A3' : {
        'Product' : 'iPad',
        'Price' : 999,
        'Supplier' : 'Digimap',
        'Qty' : 25
    },
    'A4' : {
        'Product' : 'iMac Pro',
        'Price' : 3999,
        'Supplier' : 'iBox',
        'Qty' : 10
    }
}

def main_menu():
    print('\n========== Warehouse Inventory List ==========')
    print('1. Read Data')
    print('2. Create Data')
    print('3. Update Data')
    print('4. Delete Data')
    print('5. Exit')
    choice = input('Please Select Menu [1-5] : ')
    if choice == '':
        main_menu()
    elif choice == '5':
        print('\n----------- Thank You and Good Bye -----------')
        quit()
    else:
        try:
            main_menus[choice]()
        except KeyError:
            print('\n---------------- invalid input ---------------')
            main_menu()
    return
    
def read_menu():
    while True :
        print('\n========== Read Menu ==========')
        print('1. Read All Data')
        print('2. Read Selection Data')
        print('3. Main Menu')
        choice = input('Please Select Menu [1-3] : ')
        if choice == '1':
            if len(stock) != 0:
                print('\n----------------------------------- All Data -----------------------------------')
                for k,v in stock.items():        
                    print(f"ID : {k}\t Product : {stock[k]['Product']} \tPrice : {stock[k]['Price']}\t Supplier : {stock[k]['Supplier']} \tQty : {stock[k]['Qty']}")
            else:
                print('\n------ No Data Available ------\n')
            continue
        elif choice == '2':
            if len(stock) != 0 :
                ID = input('Enter ID : ').upper()
                for k in stock.keys():
                    if k == ID:
                        print(f'\n------------------------------- Data With ID : {ID} ------------------------------')
                        print(f"ID : {k}\t Product : {stock[k]['Product']} \tPrice : {stock[k]['Price']}\t Supplier : {stock[k]['Supplier']} \tQty : {stock[k]['Qty']}")
                    else:
                        continue
                    read_menu()
                print('\n-------- Data Not Found -------')
            else:
                print('\n------ No Data Available ------\n')
        elif choice == '3':
            main_menu()
        else:
            continue

def create_menu():
    while True :
        print('\n========== Create Menu ==========')
        print('1. Create Data')
        print('2. Main Menu')
        choice = input('Please Select Menu [1-2] : ')
        if choice == '1':
            ID = input('Enter ID : ').upper()
            if ID in stock:
                print('\n------ Data Already Exists ------')
            else:
                Product = input('Enter Product : ')
                Price = input ('Enter Price : ')
                Supplier = input('Enter Supplier : ')
                Qty = input('Enter Qty : ')
                new_stock = {ID : {'Product' : '', 'Price' : '', 'Supplier' : '', 'Qty' : '' }}
                new_stock[ID] = {}
                new_stock[ID]['Product'] = Product
                new_stock[ID]['Price'] = Price
                new_stock[ID]['Supplier'] = Supplier
                new_stock[ID]['Qty'] = Qty
                print(f"ID : {ID}\t Product : {new_stock[ID]['Product']} \tPrice : {new_stock[ID]['Price']}\t Supplier : {new_stock[ID]['Supplier']} \tQty : {new_stock[ID]['Qty']}")
                while True:
                    confirm = input('Save This Data (y/n) : ').upper()
                    if confirm == 'Y':
                        stock.update(new_stock)
                        print('\n----------- Data Saved ----------')
                        create_menu()
                    elif confirm == 'N':
                        print('\n--------- Data Not Saved --------')
                        create_menu()
                    else:
                        continue
        elif choice == '2':
            main_menu()
        else:
            continue

def update_menu():
    while True :
        print('\n========== Update Menu ==========')
        print('1. Update Data')
        print('2. Main Menu')
        choice = input('Please Select Menu [1-2] : ')
        if choice == '1':
            ID = input('Select ID : ').upper()
            for k in stock.keys():
                if k == ID:
                    print(f"\nID : {k}\t Product : {stock[k]['Product']} \tPrice : {stock[k]['Price']}\t Supplier : {stock[k]['Supplier']} \tQty : {stock[k]['Qty']}")
                    while True:
                        confirm = input('Continue Update (y/n) : ').upper()
                        if confirm == '':
                            continue
                        elif confirm == 'Y':
                            columns = input('Enter Column to Update : ').capitalize()
                            if columns in stock[ID] :
                                new_stock = {ID : {'Product' : (stock[ID]['Product']), 'Price' : (stock[ID]['Price']), 'Supplier' : (stock[ID]['Supplier']), 'Qty' : (stock[ID]['Qty']) }}
                                new_stock[ID][columns] = input(f"Enter New {columns} : ").capitalize()
                                while True:
                                    confirm = input('Confirm Data Update (y/n) : ').upper()
                                    if confirm == 'Y':
                                        stock.update(new_stock)
                                        print('\n---------- Data Updated ---------')
                                        update_menu()
                                    elif confirm == 'N':
                                        print('\n-------- Data Not Updated -------')
                                        update_menu()
                                    else:
                                        continue
                            else:
                                continue
                        elif confirm == 'N':
                            print('\n-------- Data Not Updated -------')
                            update_menu() 
                        else:
                            continue  
                else:
                    continue
            print('\n--------- Data Not Found --------')
        elif choice == '2':
            main_menu()
        else:
            continue

def delete_menu():
    while True :
        print('\n========== Delete Menu ==========') 
        print('1. Delete Data')
        print('2. Main Menu')
        choice = input('Please Select Menu [1-2] : ')
        if choice == '1':
            ID = input('Select ID : ').upper()       
            for k in stock.keys():
                if k == ID:
                    print(f"\nID : {k}\t Product : {stock[k]['Product']} \tPrice : {stock[k]['Price']}\t Supplier : {stock[k]['Supplier']} \tQty : {stock[k]['Qty']}")                  
                    while True :
                        confirm = input('Confirm Delete (y/n) : ').upper()
                        if confirm == 'Y' :
                            stock.pop(ID)
                            print('\n---------- Data Deleted ---------')
                            delete_menu()
                        elif confirm == 'N':
                            print('\n-------- Data Not Deleted -------')
                            delete_menu()
                        else:
                            continue
                else:
                    continue
            print('\n--------- Data Not Found --------')
        elif choice == '2':
            main_menu()
        else:
            continue

main_menus = {
    '1' : read_menu,
    '2' : create_menu,
    '3' : update_menu,
    '4' : delete_menu
}

main_menu()

# James Nathanael Nainggolan 22/02/2022
