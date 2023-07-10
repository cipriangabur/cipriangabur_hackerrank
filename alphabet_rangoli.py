def print_rangoli(size):
    # your code goes here
    letters = [chr(letter) for letter in range(ord('a'), ord('a') + size)]
    reverse_letters = letters[::-1]
    rows = size * 2 - 1
    middle = "-".join(reverse_letters + letters[1:])
    len_mid = len(middle)
    for row in range(rows):
        if row < size-1:
            print("-".join(reverse_letters[:row+1] + letters[size-row:]).center(len_mid, "-"))
        elif row == size-1:
            print(middle)
        elif row > size - 1:
            print("-".join(reverse_letters[:rows - row] + letters[row - size + 2:]).center(len_mid, "-"))


if __name__ == '__main__':
    n = 5  # int(input())
    print_rangoli(n)
