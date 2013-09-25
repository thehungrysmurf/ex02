import arithmetic
# greet user
# tell user to insert operator followed by number(s) to process
# read input
# tokenize input
# if the first token is 'q', quit
# if input is not according to format, alert user
# call the math function on the input
# print output

def main():
    print "Welcome to the calculator."

    user_input = raw_input("Please specify numbers to process, \nstarting with the operand, \
separated by a single space: ")

    user_input_list = user_input.split(' ')
    # print user_input_list

    if user_input_list[0] == "":
        del(user_input_list[0]) 

    if user_input_list[0] == "q":
        print "I'm quitting."
        exit(0)

    if user_input_list[0] not in ["+", "-", "/", "*", "mod", "square", "pow", "cube"]:
        print "I don't understand. Please use the format specified above."

    elif user_input_list[0] == "+":
        print arithmetic.add(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "-":
        print arithmetic.subtract(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "/":
        print arithmetic.divide(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "*":
        print arithmetic.multiply(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "mod":
        print arithmetic.mod(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "square":
        print arithmetic.square(int(user_input_list[1]))
    elif user_input_list[0] == "cube":
        print arithmetic.cube(int(user_input_list[1]))
    elif user_input_list[0] == "pow":
        print arithmetic.pow(int(user_input_list[1]), int(user_input_list[2]))

main()




