
# function creation

def calculate_discount(price, discount_percent):
    
    #condition to apply the discount
    
    if discount_percent >= 20:
        
        discount_amount = price * (discount_percent / 100)
        
        final_price = price - discount_amount 
        
        return final_price
    else:
        
        #Case if there is no discount
    
        return price
    

# Prompt user for inputs

try:
     
     price = float(input("Enter the original price of the item: "))
    
     discount_percent = float(input("Enter the discount percentage:  "))
     
     
     #calculate the final price
     
     final_price = calculate_discount(price, discount_percent)
     
     #display the result
     
     if discount_percent >=20:
         
         print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
     else:
         print(f"No discount applied. Final price: {final_price:.2f}")
         
except ValueError:
    print("Please enter valid numeric values for price and discount.")        