""".
Write a program that prompts the user to input number of calls and calculate the 
monthly telephone bills as per the following rule: 
Minimum Rs. 200 for up to 100 calls. 
Plus Rs. 0.60 per call for next 50 calls. 
Plus Rs. 0.50 per call for next 50 calls. 
Plus Rs. 0.40 per call for any call beyond 200 calls.
 """
    
#num_of_call = int(input("ENTER THE YHE NUMBER OF CALL : "))

# Prompt the user to input the number of calls
num_calls = int(input("Enter the number of calls: "))

# Define the billing rules
min_charge = 200
charge_per_call_1 = 0.60
charge_per_call_2 = 0.50
charge_per_call_3 = 0.40
call_limit_1 = 100
call_limit_2 = 150

# Calculate the monthly telephone bill
if num_calls <= call_limit_1:
    total_bill = min_charge
elif num_calls <= call_limit_2:
    total_bill = min_charge + (num_calls - call_limit_1) * charge_per_call_1
else:
    total_bill = min_charge + 50 * charge_per_call_1 + (num_calls - call_limit_2) * charge_per_call_2

# Print the calculated bill
print(f"Monthly telephone bill: Rs. {total_bill:.2f}")


