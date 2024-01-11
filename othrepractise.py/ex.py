# # s_name = input("enter a number")
# # s_marks = int(input("enter the marks"))

# num_students = int(input("Enter the number of students: "))

# student_names = []
# student_marks = []
# for i in range(num_students):
#     name = input(f"Enter the name of student {i + 1}: ")
#     mark = float(input(f"Enter the marks of {name}: "))

#     student_names.append(name)
#     student_marks.append(mark)
# print("\nStudent Names with Marks:")
# for i in range(num_students):
#     print(f"{student_names[i]}: {student_marks[i]}")

# import requests


# def get_data(self, api):
#         response = requests.get(f"{api}")
#         if response.status_code == 200:
#             print("sucessfully fetched the data")
#             self.formatted_print(response.json())
#         else:
#             print(f"Hello person, there's a {response.status_code} error with your request")

# parameters = {
#             "username": "kedark"
#         }

# def get_user_data(self, api, parameters):
#         response = requests.get(f"{api}", params=parameters)
#         if response.status_code == 200:
#             print("sucessfully fetched the data with parameters provided")
#             self.formatted_print(response.json())
#         else:
#             print(
#                 f"Hello person, there's a {response.status_code} error with your request")