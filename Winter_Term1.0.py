print("Welcome to Winter Term Course Registration 1.0")
student_course_selections = {}
name = input("What is your name?")

def request_course_input():

    top_priority_course = input("What course do you pick as your Top Priority?")

    print("Excellent! Your top priority course of all course for Winter Term is ", top_priority_course , " .")

    block_1_first_choice = input("What course do you pick as your first choice for block 1?")
    block_1_second_choice = input("What course do you pick as your second choice for block 1?")
    block_1_third_choice = input("What course do you pick as your third choice for block 1?")
    block_1_fourth_choice = input("What course do you pick as your fourth choice for block 1?")
    block_1_fifth_choice = input("What course do you pick as your fifth choice for block 1?")

    print("For block 1 your choices in order of preference are: " , "\n",  block_1_first_choice ,  "\n", block_1_second_choice, "\n", block_1_third_choice, "\n", block_1_fourth_choice, "\n", block_1_fifth_choice)


    block_1_correct_response = input("Is this list of courses correct? [Y/N]")

    def is_course_input_complete():
        if block_1_correct_response == "Y":
            print("Awesome! You have now completed course registration")
        elif block_1_correct_response == "N":
            print("Sorry to hear that. Let's try this one more time")
            return request_course_input()
        else:
            print("I do not understand, but since your reponse whas not \"Y\" I will assume you need to redo your course input")
            return request_course_input()
            #set off a recursion error
    is_course_input_complete()


request_course_input()
