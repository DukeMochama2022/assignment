def calculate_discount():

    price=float(input("Enter the original price:"))
    discount_percentage=int(input("Enter the discount:"))

    if discount_percentage >= 20:
        discount=price*(discount_percentage/100)
        final_price=price-discount
        print(final_price)
    elif  discount_percentage < 20:
        print(price)
    else:
        print(price)    

calculate_discount()