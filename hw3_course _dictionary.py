# Name: Hasin Shadab Rahman                                                                        UID:U87513234
# This code creates three dictionaries (course_names, instructors, and class_times) to store information related to various courses.
# Each dictionary uses the course numbers (e.g., "COP 2510") as keys and associates them with relevant information such as course names, instructors, and class times.
# The program prompts the user to input a course number (e.g., "COP 2510").
# It then checks if the entered course number exists in the dictionaries. If found, it retrieves and displays the corresponding course name, instructor, and class times.
# If the entered course number is not found in the dictionaries, it prints a message indicating that the course is not found.
# In summary, this code allows users to input a course number, and if the course information is available, it retrieves and displays it. It's a simple example of a dictionary-based data retrieval system for educational course information.
course_names = {
    "COP 2510": "Programming Concepts",
    "EGN 3000L": "Foundations of Engineering Lab",
    "MAC 2281": "Calculus I",
    "MUH 3016": "Survey of Jazz",
    "PHY 2048": "General Physics I"
}

instructors = {
    "COP 2510": "S. Small",
    "EGN 3000L": "J. Anderson",
    "MAC 2281": "A. Makaryus",
    "MUH 3016": "A. Wilkins",
    "PHY 2048": "G. Pradhan"
}

class_times = {
    "COP 2510": "TR 8:00am - 9:15am",
    "EGN 3000L": "TR 11:00am - 12:15pm",
    "MAC 2281": "MW 9:30am - 10:45am",
    "MUH 3016": "online asynchronous",
    "PHY 2048": "TR 5:00pm - 6:15pm"
}

# Get user input for the course number
course = input("Enter a course number: ")

# Check if the course is in the dictionaries
if course in course_names:
    print('The course detail are:')
    print(f"Course Name: {course_names[course]}")
    print(f"Instructor: {instructors[course]}")
    print(f"Class Times: {class_times[course]}")
else:
    print(f"{course} is an invalid course number")
