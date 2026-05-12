# define function to calculate double values


# user_input = int(input("Enter a number: "))
#
#
# def double_score(x):
#
#     result = x*2
#
#     return result
#
#
#
# result = double_score(user_input)
#
#
# print(f"The doubled_score is {result}")



# Write a function called filter_passing that:
#
# Takes a list of scores as input
# Returns only scores above 50 using a list comprehension inside the function



# Main function to filter user input to process and filter scores

def filter_passing(score_list):
    return  [score for score in score_list if score >= 50]




# list comprehension for user input

passed_data = [int(x) for x in input("Please enter the scores").split()]
# print(passed_data)

# print(f" The filtered list {converted}")


# calling the main function
print(f" The filtered list {filter_passing(passed_data)}")