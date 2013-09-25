import arithmetic
# greet user
# tell user to insert operator followed by number(s) to process
# read input
# tokenize input
# if the first token is 'q', quit
# if input is not according to format, alert user
# call the math function on the input
# print output

def turn_to_int(list):
    list2 = list[1: len(list)]
    for i in range(len(list2)):
        list2[i] = int(list2[i])
    return list2

def main():
    print "Welcome to the calculator."

    user_input = raw_input("Please specify numbers to process, \nstarting with the operand, \
separated by a single space: ")

    user_input_list = user_input.split(' ')
    #print user_input_list[0]

    if user_input_list[0] == "":
        del(user_input_list[0]) 

    if user_input_list[0] == "q":
        print "I'm quitting."
        exit(0)

    product = 1

    if user_input_list[0] not in ["+", "-", "/", "*", "mod", "square", "pow", "cube"]:
        print "I don't understand. Please use the format specified above."

    elif user_input_list[0] == "+": 
        print sum(turn_to_int(user_input_list))
    elif user_input_list[0] == "-":
        print arithmetic.subtract(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "/":
        divide_list = turn_to_int(user_input_list)
        divide = divide_list[0]
        for i in divide_list[1: len(divide_list)]:
            divide = divide / i
        print divide 
        # print arithmetic.divide(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "*":
        product_list = turn_to_int(user_input_list)
        for i in product_list:
            product = product * i
        print product 
    elif user_input_list[0] == "mod":
        print arithmetic.mod(int(user_input_list[1]), int(user_input_list[2]))
    elif user_input_list[0] == "square":
        print arithmetic.square(int(user_input_list[1]))
    elif user_input_list[0] == "cube":
        print arithmetic.cube(int(user_input_list[1]))
    elif user_input_list[0] == "pow":
        print arithmetic.pow(int(user_input_list[1]), int(user_input_list[2]))

main()




