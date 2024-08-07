def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print('1 ' * i)

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
      
        print(' ' * (rows - i), end='')
    
        for j in range(1, i + 1):
            print(j, end='')
       
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()

def display_help():
    print("\nHelp: A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            rows = int(input("Enter the number of lines: "))
            display_right_angle_triangle(rows)
        elif choice == '2':
            rows = int(input("Enter the number of lines: "))
            display_palindromic_triangle(rows)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
