num_list = [25, 10, 45, 90, 15, 60 , 159]

if not num_list:
    # return None  # Return None for an empty list
    print ("it is'nt number")
largest = num_list[0]  # Initialize largest with the first element
for num in num_list:
    if num > largest:
        largest = num  # Update largest if a larger number is found

if largest is not None:
    print("The largest number in the list is:", largest)
else:
    print("The list is empty.")
	