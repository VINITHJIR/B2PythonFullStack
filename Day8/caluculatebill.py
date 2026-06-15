from billing import bill , gst

price = int(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))
#calculate the total bill
total = bill(price, quantity)
#claculate the gst amount
gst_amount = gst(total)

print("Total bill: ", total)
print("GST amount: ", gst_amount)
print("Total amount to be paid: ", total + gst_amount)
