# List uniqueness checker
# check if all elements in a list are unique , if a duplicate is found break  and the loop print the duplicate 

list =["Hyderabad", "karachi",  "karachi","Hyderabad", "lahore", "sukkur", "islamabad", "sukkur", "peshawar"]

unique_items= set()
for duplicate in list:
    if duplicate in unique_items:
        print(f"Duplicate found: {duplicate}")
        continue
    unique_items.add(duplicate)
else:
    print("Now All items are unique")