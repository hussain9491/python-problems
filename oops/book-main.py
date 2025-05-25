from bookoops import book

book1 =book("Life lesson", "John", 2020, 200, True)
book2 = book("Make Money", "Jane", 2019, 300, True)
book3 =book("python development", "rossum", 2008, 400, False)

print(book3.title)
print(book1.author)
book2.read()   
print(f"Sorry this {book3.title} book is {book3.available} available")  # Output: Sorry this False book is not available
