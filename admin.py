def addProduct():
    print("enter productname and price")
    productName  = input()
    price = int(input())
    product = { "productName" : productName,"price":price}
    return product

