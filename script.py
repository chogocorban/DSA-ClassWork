from typing import Final

number: int = 10
decimal: float = 2.5
active: bool = True

names: list = ["John", "Doe"]
#name: str = 'John Doe'

marks: tuple = (1,24,5)

# print(number)
# print(decimal)
# print(names)

def greet(name: str):
    print(name)
    return f'Welcome, {name.title()}'
#print(f'Welcome, {name}')
    # #age = 50
    # if age < 20:
    #     print('adult')
    # elif age > 50:
    #     print("adult")
    # else:
    #     print("under age")
    #     for i in range(10):
    #         print(i)
    # return None

# for i in range(10):
#     print(i)

def add(x: int,y: int) -> int:

    return x + y

def area_circle(radius: float) -> float:
    #pi = 3.14
    PI: Final = 3.14

    return PI * (radius ** 2)

def has_passed(average: float) -> bool:
    return average >= 50

def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))

    scores: list[int] = []

    for i in range(3):
        while True:
            try:
                score = int(input(f"Enter score for subject {i+1}: "))
                if score >= 0 or score <= 100 :
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number")

    average_score: float = compute_average(scores)
    is_pass: bool = has_passed(average_score)

    print("\n ---- Report Card ----")
    print(f"Name            : {name}")
    print(f"Scores          : {scores}")
    print(f"Average         : {average_score:.2f}")
    print(f"Status          : {'Pass' if is_pass else 'Fail'}")

    assignments_done: int = 5
    pts: float = 2.5
    total_score: float = average_score + pts

    print(f"Bonus Pts : + {pts} for {assignments_done} assignments")
    print(f"Final Score : {total_score:.2f}")

# if __name__ == "__main__":
#     students_performance()


