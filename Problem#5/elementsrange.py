def filter_and_print_range(input_list, min_val, max_val):
    newList = [i for i in input_list if min_val <= i <= max_val]
    print(newList)

if __name__ == '__main__':
    # Get input for the list of integers
    input_list = input("Enter a space-separated string of numbers: ")
    integer_list = [int(num) for num in input_list.split()]

    # Get input for the range (min and max values)
    input_range = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, input_range.split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)




