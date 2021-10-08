movie = input()
ascii = 0
counter = 0
sum = 0
current_sum = 0
best_sum = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercase = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while movie != "STOP":
    for index in movie:
        ascii = ord(index)
        if index in lowercase:
            sum = ascii - (2 * len(movie))
            current_sum += sum
        elif index in uppercase:
            sum = ascii - len(movie)
            current_sum += sum
        elif index == " ":
            sum = ord(index)
            current_sum += sum
        elif index in numbers:
            sum = ord(index)
            current_sum += sum
    counter += 1
    if current_sum > best_sum:
        best_sum = current_sum
        last_name = movie
    if counter == 7:
        print("The limit is reached.")
        break
    sum = 0
    current_sum = 0
    movie = input()
print(f"The best movie for you is {last_name} with {best_sum} ASCII sum.")



