"""
File: class_reviews.py
Name: Wei
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    Function: The program can keep record the scores either for class SC001 or SC101 and return the maximum, minimum and
    average scores for both course.
    Principle: Since there is no limited time to insert the scores, while loop is used. The max. and min. scores is
    recorded by comparing the value. Counter is set to calculate the average scores.
    """

    t_001 = int(0)
    max_001 = int(0)
    min_001 = int(0)
    avg_001 = float(0.0)
    a_001 = int(0)
    t_101 = int(0)
    max_101 = int(0)
    min_101 = int(0)
    avg_101 = float(0.0)
    a_101 = int(0)

    c = str(input("Which class?"))
    c_upper = c.upper()  # case-insensitive

    if c_upper == "-1":  # In the case that the user insert -1 at the very beginning
        print("No class scores were entered")
    else:
        while c_upper != "-1":
            if c_upper == "SC001":  # Separate the the SC001 and SC101
                grade_sc001 = int(input("Score:"))
                t_001 += 1
                if t_001 == 1:  # only for first time, to have initial value
                    max_001 = grade_sc001
                    min_001 = grade_sc001
                    avg_001 = grade_sc001
                    a_001 = grade_sc001
                else:
                    if grade_sc001 > max_001:
                        max_001 = grade_sc001
                    if grade_sc001 < min_001:
                        min_001 = grade_sc001
                    a_001 = a_001 + grade_sc001
                    avg_001 = a_001 / t_001
                c = str(input("Which class?"))
                c_upper = c.upper()
            if c_upper == "SC101":
                grade_sc101 = int(input("Score:"))
                t_101 += 1
                if t_101 == 1:  # only for first time
                    max_101 = grade_sc101
                    min_101 = grade_sc101
                    avg_101 = grade_sc101
                    a_101 = grade_sc101
                else:
                    if grade_sc101 > max_101:
                        max_101 = grade_sc101
                    if grade_sc101 < min_101:
                        min_101 = grade_sc101
                    a_101 = a_101 + grade_sc101
                    avg_101 = a_101 / t_101
                c = str(input("Which class?"))
                c_upper = c.upper()
        print("======SC001=======")
        print("Max (001):" + str(max_001))
        print("Min (001):" + str(min_001))
        print("Avg (001):" + str(avg_001))
        print("======SC101=======")
        print("Max (101):" + str(max_101))
        print("Min (101):" + str(min_101))
        print("Avg (101):" + str(avg_101))



# Time spent: 2 hours

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
