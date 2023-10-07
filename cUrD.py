"""simple CuRd"""
# Main_Dict={}
# print("---------Welcome to This CrUD------------")
# while True:
#     print("1:- Create\n 2:- Read\n 3:- Update\n 4:- Deletion")
#     choose=int(input("enter option:- "))
#     if choose==1:
#         Name=(input("enter name:- "))
#         Email=(input("enter Email:- "))
#         Password=(input("enter password:- "))
#         Phone=int(input("enter phone:- "))
#         Dict={"name":Name,"Email":Email,"password":Password}
#         Main_Dict.update({Phone:Dict})
#     elif choose==2:
#         mob=int(input("Enter User mobile Number :->"))
#         if mob in Main_Dict:
#             print(Main_Dict[mob])
#             continue
#         else:
#             print("it is not there")
#     elif choose==3:
#         mob=int(input("enter number:- "))
#         if mob in Main_Dict:
#             print(" 1:- name\n 2:- Email\n 3:- password\n 4:-Number")
#             choose1=int(input("select option:- "))
#             if choose1==1:
#                 new_name=input("enter new name:-")
#                 Main_Dict[mob]["name"]=new_name
#             elif choose1==2:
#                 new_Email=input("enter new Email:- ")
#                 Main_Dict[mob]["Email"]=new_Email
#             elif choose1==3:
#                 new_password=input("enter new password:- ")
#                 Main_Dict[mob]["Password"]=new_password
#             elif choose1==4:
#                 new_mob = int(input("Please enter new number:-"))
#                 # if mob in Main_Dict:
#                 Main_Dict[new_mob]=Main_Dict[mob]
#                 del Main_Dict[mob]
#         else:
#             print("it is not present in our data")
#     elif choose==4:
#         mob=int(input("enter number:- "))
#         if mob in Main_Dict:
#             del Main_Dict[mob]
#         else:
#             print("user is not find")
#     else:
#           print("Invalid Choice. Please try Again")

"""using Json cUrD"""
# import json
# import os

# # Load data from the JSON file
# def load_data():
#     try:
#         with open("data.json", "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#         data = {}
#     return data

# # Save data to the JSON file
# def save_data(data):
#     with open("data.json", "w") as file:
#         json.dump(data, file, indent=4)

# Main_Dict = load_data()

# print("---------Welcome to This CrUD------------")

# while True:
#     print("1:- Create\n2:- Read\n3:- Update\n4:- Deletion")
#     choose = int(input("enter option:- "))

#     if choose == 1:
#         Name = input("enter name:- ")
#         Email = input("enter Email:- ")
#         Password = input("enter password:- ")
#         Phone = int(input("enter phone:- "))
#         Dict = {"name": Name, "Email": Email, "Password": Password}
#         Main_Dict[Phone] = Dict
#         save_data(Main_Dict)
#         print("User data created and saved.")

#     elif choose == 2:
#         mob = int(input("Enter User mobile Number: "))
#         if mob in Main_Dict:
#             print(Main_Dict[mob])
#         else:
#             print("User not found")

#     elif choose == 3:
#         mob = int(input("enter number: "))
#         if mob in Main_Dict:
#             print("1:- name\n2:- Email\n3:- password\n4:- Number")
#             choose1 = int(input("select option:- "))

#             if choose1 == 1:
#                 new_name = input("enter new name:-")
#                 Main_Dict[mob]["name"] = new_name
#             elif choose1 == 2:
#                 new_Email = input("enter new Email:- ")
#                 Main_Dict[mob]["Email"] = new_Email
#             elif choose1 == 3:
#                 new_password = input("enter new password:- ")
#                 Main_Dict[mob]["Password"] = new_password
#             elif choose1 == 4:
#                 new_mob = int(input("Please enter new number:-"))
#                 if new_mob not in Main_Dict:
#                     Main_Dict[new_mob] = Main_Dict[mob]
#                     del Main_Dict[mob]
#                     save_data(Main_Dict)  # Save data after updating
#                     print("User data updated and saved.")
#                 else:
#                     print("The new number already exists.")
#             else:
#                 print("Invalid option for update.")
#         else:
#             print("User not present in our data")

#     elif choose == 4:
#         mob = int(input("enter number: "))
#         if mob in Main_Dict:
#             del Main_Dict[mob]
#             save_data(Main_Dict)  # Save data after deletion
#             print("User data deleted and saved.")
#         else:
#             print("User not found")

#     else:
#         print("Invalid choice. Please try again.")
