def process_and_print(input_string):
  # Split into separate strings
  inputSplt =  input_string.split(' ')
  # Convert strings to integers and filter out negative values
  input_data = [int(num) for num in inputSplt]
  newList = [i for i in input_data if i < 0]
    
  newList.sort(reverse=True)

  resultList = ''.join(map(str, newList))
  print(resultList)

    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
