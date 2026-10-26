# prompt for the student's name, score and attendance, and print the output
def main():
    name = input("What's your name: ")
    formatted_name = format_student(name)
    try:
        score = int(input("What's your score: "))
        attendance = float(input("What's your percentage attendance: "))
        category = get_result(score, attendance)
        if category is not None:
            remark = get_remark(category)
            print(
                f"{formatted_name} scored {score} with {attendance:.1f}% attendance — {category}. {remark}"
            )
        else:
            return None
    except ValueError:
        pass


# return the student's name in title case
def format_student(n):
    n = n.title().strip()
    return n


# return the result category based on the student's score and attendance
def get_result(s, a):
    if 100 < s or s < 0 or 100 < a or a < 0:
        return None
    elif a < 75:
        return "Disqualified"
    elif s >= 80:
        return "Distinction"
    elif s >= 60:
        return "Pass"
    else:
        return "Fail"


# return a short comment based on the result category
def get_remark(c):
    match c:
        case "Distinction":
            return "Outstanding work!"
        case "Pass":
            return "Solid effort"
        case "Fail":
            return "Needs improvement"
        case _:
            return "Attendance requirement not met"


if __name__ == "__main__":
    main()
