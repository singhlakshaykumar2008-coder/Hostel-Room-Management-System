rooms = {"A101": ["Rahul Sharma", "Aman Verma", "Bhavya Bhardwaj"],
         "A102": ["Rohit Singh", "Kunal Jain","Raghavendra"],
         "B201": ["Aditya Gupta", "Sahil Mehta", "Harsh Singh"],
         "C304": ["Lakshay Kumar", "Ekansh Singh", "Dushiyant Bhardwaj"]}
while True:
    print("\n HOSTEL ROOM MANAGEMENT ")
    print("1 Find students by room")
    print("2 Update student name")
    print("3 Change student room")
    print("4 Add new student")
    print("5 Display all rooms")
    print("6 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        room = input("Enter room number: ").upper()
        if room in rooms:
            print("Students in", room, ":")
            for student in rooms[room]:
                print("-", student)
            else:
                  print("Room not found.")
                 
    elif choice == "2":
        old = input("Enter current student name: ")
        if any(old in students for students in rooms.values()):
            for students in rooms.values():
                if old in students:
                    new = input("Enter new name: ")
                    students[students.index(old)] = new
                    print("Name updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
                    name = input("Enter student name: ")
                    new_room = input("Enter new room number: ").upper()
                    for room, students in rooms.items():
                     if name in students:
                        students.remove(name)
                        rooms.setdefault(new_room, []).append(name)
                        print("Room changed successfully.")
                        break
                     else:
                        
                         print("Student not found.")

    elif choice == "4":
        name = input("Enter student name: ")
        room = input("Enter room number: ").upper()
        rooms.setdefault(room, []).append(name)
        print("Student added successfully.")

    elif choice == "5":
        for room, students in rooms.items():
            print(room, ":", ", ".join(students))

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")