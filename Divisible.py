num = input("Enter the number (Numerator) ")
dem = input("enter the number(Denominator)")

if num%dem == 0:
    print("\n" , str(num) , "is divisible by" , str(dem))
else:
    print("\n" , str(num) , "is not divisible by" , str(dem))