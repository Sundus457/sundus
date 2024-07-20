
def generate_even_squares_and_slice(original_list, start_index, end_index):
   
    even_squares = [x ** 2 for x in original_list if x % 2 == 0]
    
   
    sliced_list = original_list[start_index:end_index]
    
    return even_squares, sliced_list


input_list = input("Enter the list of integers : ")
original_list = list(map(int, input_list.strip('[]').split(',')))


start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))


even_squares, sliced_list = generate_even_squares_and_slice(original_list, start_index, end_index)


print("List of squares of even numbers:", even_squares)
print("Sublist:", sliced_list)




