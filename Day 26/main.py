import random

# Dict Comprehensions
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)

passed_students = {
    student: score for (student, score) in students_scores.items() if score > 60
}

# Words Dictionary Challenge
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
# print(words)
result = {word: len(word) for word in words}
# print(result)


# Weather Challenge
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (weather * 9 / 5) + 32 for (day, weather) in weather_c.items()}

# print(weather_f)

# Pandas DataFrame
import pandas

student_dict = {
    "student": ["Alex", "Beth", "Caroline"],
    "score": [56, 76, 98],
}

student_data_frame = pandas.DataFrame(student_dict)
df = student_data_frame
# print(student_data_frame)

# for key, value in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    # print(row)
    # if row.student == "Alex":
    #     print(row.score)
    pass

{new_key: new_value for (index, row) in df.iterrows()}
