print("""Hi there, you on the table. I wonder if you'd mind taking a brief survey. \nFive questions. \nNow, I know you're sleepy, but I just bet it'll make you feel right as rain.\nI'd be just thrilled to chat once we've run the survey.""")

# prompt user to answer if they want to play
question = input("Shall we begin with question one? ")

while question != "yes":
    question = input("Shall we begin with quesion one? ")

print("Great! Off we go.")

# question 1
answer1 = input(
    "Who are you?\nFirst name will do.\nIf you can't answer the question, feel free to say, 'unknown'. ")
if answer1 == "idk":
    answer1 = "Unknown"
    print("Unknown")

answer2 = input("Question two, in which US state or territory were you born? ")
if answer2 == "idk":
    answer2 = "Unknown"
    print("Unknown")

answer3 = input("Question 3, please name any US state or territory. ")
if answer3 == "idk":
    answer3 = "Unknown"
    print("Unknown")

answer4 = input("Question four, what is Mr. Eagan's favorite breakfast? ")
if answer4 == "idk":
    answer4 = "Unknown"
    print("Unknown")

answer5 = input("Question five. And as a reminder, this is the final question.\nTo the best of your memory, what is or was the color of your mother's eyes? ")
if answer5 == "idk":
    answer5 = "Unknown"
    print("Unknown")

# repeat answers & count unknowns
print(
    f"So that's {answer1}, {answer2}, {answer3}, {answer4}, {answer5}.\nThat's a perfect score.")
