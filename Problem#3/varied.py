def process_input(input_string):
  # Split into separate strings
  userSplt = user_input.split(' ')
    
  # Convert strings to floats
  userFlt = [float(num) for num in userSplt]
                  
  # Get max and average
  max_value = sum(userFlt) / len(userFlt)
  average_value = max(userFlt)
  return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
