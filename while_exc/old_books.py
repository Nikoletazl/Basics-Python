searched_book = input()
current_book = input()
books_count = 0
while True:
    current_book = input()
    books_count += 1
    if current_book == searched_book:
        print(f"You checked {books_count} books and found it.")
    elif current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_count} books.")
        break

