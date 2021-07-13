"""
    create table product(
        productId integer primary key auto_increment,
        productName varchar(30),
        price integer,
        qty integer
    );

"""

import  mysql.connector as c

mydb = c.connect(host="localhost",user="root",password="root",database="21pythonr")

cur  = mydb.cursor() #this will helps you to execute query


while True:
    print("1 For Add Product")
    print("2 For Delete Product")
    print("3 For Update Product")
    print("4 For View Product") #single product via product id
    print("5 For List all Product")# all products from database
    print("0 For Exit")

    choice = int(input("Enter choice"))

    if choice == 1:
         productName = input("Enter productName")
         price = int(input("Enter price"))
         qty = int(input("Enter qty"))
         cur.execute("insert into product (productName,price,qty) values (%s,%s,%s)",(productName,price,qty))
         mydb.commit()
    elif choice==2:
        print("Enter Product ID")
        productId = int(input())
        cur.execute(" delete  from product where productId = %s", (productId,))
        print(cur.rowcount,"record(s) deleted")
        mydb.commit()
    elif choice==3:
        print("Enter Product ID")
        productId = int(input())
        cur.execute("select * from product where productId = %s", (productId,))
        product = cur.fetchone()
        print(product)
        productId = product[0]
        productName =product[1]
        price = product[2]
        qty=product[3]

        print("old ProductName : ",productName)
        print("Do you want to change?Y|N")
        change = input()
        if change == "Y":
            print("Enter New Product Name")
            productName = input()

        # print("old Product Price : ", price)
        # print("Do you want to change?Y|N")
        # change = input()
        # if change == "Y":
        #     print("Enter New Product Price")
        #     price = int(input())

        # print("old Product Qty : ", qty)
        # print("Do you want to change?Y|N")
        # change = input()
        # if change == "Y":
        #     print("Enter New Product Qty")
        #     qty = int(input())

        # cur.execute("update product set productName = %s , price = %s, qty = %s where productId = %s",(productName,price,qty,productId))
        cur.execute("update product set productName = %s  where productId = %s",(productName,  productId))
        print(cur.rowcount," record(s) updated..")
        mydb.commit()


    elif choice == 4:
        print("1 For View By Id\n2 For View by Name")
        subChoice = int(input("Enter choice: "))

        if subChoice == 1:
            print("Enter Product ID")
            productId = int(input())
            cur.execute("select * from product where productId = %s",(productId,))
            product  = cur.fetchall()
            print(product)

        elif subChoice == 2:
            print("Enter Product Name")
            productName = input()
            cur.execute("select * from product where productName like %s", ("%"+productName+"%",))
            product = cur.fetchall()
            print(product)


    elif choice == 5:
        cur.execute("select * from product")
        products = cur.fetchall()
        print("ProductId  ProductName  Price  Qty")
        for p in products:
            print(p[0]," ",p[1]," ",p[2]," ",p[3]) #tuple
    elif choice == 0:
        exit(0)
    else:
        print("****Invalid choice*****")









