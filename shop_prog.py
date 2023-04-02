import qrcode

# list of all products
PRODUCTS = []
basket = []

# function :: read data from db
def read_from_db():
    db = open('database.txt', 'r')
    for line in db:
        detail = line.split(',')
        prod = {'code': int(detail[0]), 'name': detail[1], 'price': int(
            detail[2]), 'count': int(detail[3])}
        PRODUCTS.append(prod)
    db.close()

# function :: show menu
def show_menu():
    print('1- Add')
    print('2- Edit')
    print('3- Remove')
    print('4- Search')
    print('5- Show List')
    print('6- Buy')
    print('7- Product QRCode')
    print('8- Exit')

# function :: menu functions
def Add():
    code = int(input('Enter product code: '))
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))
    count = int(input('Enter product count: '))
    new_product = {'code':code, 'name':name, 'price':price, 'count':count}
    PRODUCTS.append(new_product)
    print('New product add to list successfully')

def Edit():
    code = int(input('Enter product code: '))
    for product in PRODUCTS:
        if product['code'] == code :
            print('Which property do you want to edit: ')
            print('1- Name')
            print('2- Price')
            print('3- Count')
            prop = int(input('Enter property code: '))

            if prop == 1 :
                name = input("Enter new product name (" + product['name'] + "): ")
                product['name'] = name

            elif prop ==2:
                price = int(input("Enter new product price (" + str(product['price']) + "): "))
                product['price'] = price

            elif prop ==3:
                count = int(input("Enter new product count (" + str(product['count']) + "): "))
                product['count'] = count

            else:
                price('Enter property code to edit...')

            print('Product update successfully...')
            break
    else:
        print('Product code in invalid...')

def Remove():
    code = int(input('Enter product code for delete: '))
    i= 0
    for product in PRODUCTS:
        if product['code'] == code :
            PRODUCTS.pop(i)
            break
        else:
            i+=1
    else:
        print('Code not found...')
    
    print("Product remove successfully...")

def Search():
    user_find = input("Type your keyword: ")
    for product in PRODUCTS:
        if product['code'] == user_find or product['name'] == user_find :
            print('code\tname\tprice\tcount')
            print(product['code'], '\t', product['name'], '\t', product['price'], '\t', 
                  product['count'])
            break
    else:
        print('Not Found...')

def Show_list():
    print('code\t\tname\tprice\t\tcount')
    for product in PRODUCTS:
        print(product['code'], '\t\t', product['name'], '\t\t',
              product['price'], '\t\t', product['count'])

def Buy():
    while True:
        code = int(input("Enter prod code: "))
        for product in PRODUCTS:
            if product['code'] == code:
                while True:
                    user_count = int(input("Enter product count: "))
                    if user_count > product['count']:
                        print('Store dont have enough product...')
                    else:
                        user_shop = {'name':product['name'], 'price':product['price'], 
                                     'count':user_count, 'sum':(product['price'] * user_count)}
                        basket.append(user_shop)
                        product['count'] = product['count'] - user_count
                        break
                break
        else:
            print('Product not found...')
        
        pos = input("do you want to buy more? y / n: ")
        if pos == 'n':
            print('============================')
            print("name\tprice\tcount\tsum")
            sum = 0
            for item in basket:
                print(item['name'], "\t", item['price'], "\t", item['count'], "\t", item['sum'])
                sum +=item['sum']
            print('--------------------')
            print("Total: ",sum)
            break

def show_qrcode():
    code = int(input('Enter product code: '))
    for product in PRODUCTS:
        if product['code'] == code :
            img = qrcode.make('code: ' + str(product['code']) + " \n name: " + product['name'] +
                              " \n price: " + str(product['price']) + " \n count: " + str(product['count']))
            img.save("product.png")

#function :: add to db
def write_to_db():
    db = open('database.txt','w')
    for product in PRODUCTS:
        result = str(product['code']) + ',' + product['name'] + ',' + str(product['price']) + ',' + str(product['count']) + "\n"
        db.write(result)

    db.close()

# Start Programm
print('🎉 Welcome To My Store 🎉')
print('⏳ Loading')
read_from_db()
print('✔ Data Loaded')
while True :
    print('============================')
    show_menu()
    print('============================')

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Add()

    elif choice == 2:
        Edit()

    elif choice == 3:
        Remove()

    elif choice == 4:
        Search()

    elif choice == 5:
        Show_list()

    elif choice == 6:
        Buy()

    elif choice == 7:
        show_qrcode()

    elif choice == 8:
        write_to_db()
        exit(0)

    else:
        print("Select Menu Item From 1 to 7")
