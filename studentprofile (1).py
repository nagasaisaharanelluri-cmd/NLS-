print("=" * 55)
print("        🎓 PERSONALIZED LEARNING AGENT")
print("             CBSE STUDENT PROFILE")
print("=" * 55)

# Student Name
name = input("\nEnter student name: ")

# Board is fixed
board = "CBSE"

# Class selection
while True:
    student_class = input("Enter your class (8, 9, or 10): ")

    if student_class in ["8", "9", "10"]:
        break
    else:
        print("❌ Please enter only 8, 9, or 10.")


# Available Subjects
available_subjects = [
    "Maths",
    "Science",
    "Social Science",
    "English",
    "Hindi",
    "Sanskrit",
    "IT",
    "AI"
]

# Display subjects
print("\n📚 Available Subjects:")

for i, subject in enumerate(available_subjects, 1):
    print(f"{i}. {subject}")


# Subject selection
while True:

    choice = input(
        "\nEnter subject numbers separated by commas "
        "(Example: 1,2,4,5): "
    )

    numbers = choice.split(",")

    selected_subjects = []
    valid = True

    for number in numbers:

        number = number.strip()

        if number.isdigit() and 1 <= int(number) <= len(available_subjects):

            subject = available_subjects[int(number) - 1]

            if subject not in selected_subjects:
                selected_subjects.append(subject)

        else:
            valid = False
            break

    if valid and len(selected_subjects) > 0:
        break

    print("❌ Please select valid subject numbers.")


# Learning Goal
goal = input("\n🎯 What is your learning goal? ")


# Display Student Profile
print("\n")
print("=" * 55)
print("              ✅ STUDENT PROFILE")
print("=" * 55)

print(f"Name          : {name}")
print(f"Board         : {board}")
print(f"Class         : {student_class}")
print(f"Subjects      : {', '.join(selected_subjects)}")
print(f"Learning Goal : {goal}")

print("=" * 55)

print("\n🎉 Student profile created successfully!")

# ============================================
# PERFORMANCE ANALYSIS FOR EACH SUBJECT
# Personalized Learning Recommendation Agent
# ============================================

subjects = [
    "Mathematics",
    "Science",
    "Social Science",
    "English",
    "Hindi",
    "Sanskrit",
    "AI",
    "IT"
]

marks = {}

print("=" * 50)
print("       📊 STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

# Get marks from the student
for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= score <= 100:
                marks[subject] = score
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Function to determine performance level
def performance_level(score):
    if score >= 90:
        return "Excellent 🌟"
    elif score >= 75:
        return "Very Good 👍"
    elif score >= 60:
        return "Good 🙂"
    elif score >= 40:
        return "Needs Improvement 📚"
    else:
        return "Needs Serious Improvement ⚠️"


# Display analysis
print("\n" + "=" * 70)
print("                  SUBJECT-WISE ANALYSIS")
print("=" * 70)

for subject, score in marks.items():
    level = performance_level(score)

    print(f"{subject:<20} | Marks: {score:>5.1f} | {level}")


# Find strongest and weakest subjects
strong_subjects = [
    subject for subject, score in marks.items()
    if score >= 75
]

weak_subjects = [
    subject for subject, score in marks.items()
    if score < 60
]


# Overall performance
total_marks = sum(marks.values())
average = total_marks / len(subjects)

print("\n" + "=" * 70)
print("                     PERFORMANCE SUMMARY")
print("=" * 70)

print(f"Overall Average: {average:.2f}%")

if average >= 90:
    overall = "Excellent Performance 🌟"
elif average >= 75:
    overall = "Very Good Performance 👍"
elif average >= 60:
    overall = "Good Performance 🙂"
elif average >= 40:
    overall = "Needs Improvement 📚"
else:
    overall = "Needs Serious Improvement ⚠️"

print(f"Overall Status: {overall}")


# Strong subjects
print("\n💪 Strong Subjects:")
if strong_subjects:
    for subject in strong_subjects:
        print(f"   • {subject}")
else:
    print("   No strong subjects identified yet.")


# Weak subjects
print("\n📚 Subjects Needing Improvement:")
if weak_subjects:
    for subject in weak_subjects:
        print(f"   • {subject}")
else:
    print("   Great! No major weak subjects identified.")


# Personalized recommendations
print("\n" + "=" * 70)
print("                 📖 LEARNING RECOMMENDATIONS")
print("=" * 70)

for subject, score in marks.items():

    print(f"\n{subject}:")

    if score >= 90:
        print("  ✓ Maintain your performance.")
        print("  → Try advanced questions and challenging quizzes.")

    elif score >= 75:
        print("  ✓ Good performance.")
        print("  → Practice higher-level questions to improve further.")

    elif score >= 60:
        print("  → Revise important concepts regularly.")
        print("  → Practice 5-10 questions every day.")

    elif score >= 40:
        print("  ⚠ Focus more on this subject.")
        print("  → Start with basic concepts and watch learning videos.")
        print("  → Practice questions after each topic.")

    else:
        print("  ⚠ This subject requires more attention.")
        print("  → Review fundamentals first.")
        print("  → Use notes, videos and beginner-level practice.")
        print("  → Consider asking a teacher for help.")

print("\n" + "=" * 70)
print("       🎓 Personalized analysis completed!")
print("=" * 70)
import random

# ============================================================
# CBSE STUDENT PRACTICE QUESTION GENERATOR
# Classes: 8, 9, 10
# Subjects: Maths, Science, Social Science, English, Hindi,
#           Sanskrit, AI, IT
# ============================================================


QUESTION_BANK = {

    # ========================================================
    # CLASS 8
    # ========================================================

    8: {

        "Maths": [
            {
                "q": "What is the value of 3/4 + 1/8?",
                "options": ["5/8", "7/8", "1/2", "3/8"],
                "answer": "7/8"
            },
            {
                "q": "Which of the following is a perfect square?",
                "options": ["36", "42", "50", "60"],
                "answer": "36"
            },
            {
                "q": "What is the square of 15?",
                "options": ["125", "200", "225", "250"],
                "answer": "225"
            },
            {
                "q": "If x + 7 = 15, what is x?",
                "options": ["6", "7", "8", "9"],
                "answer": "8"
            },
            {
                "q": "A polygon having 5 sides is called a:",
                "options": ["Triangle", "Quadrilateral", "Pentagon", "Hexagon"],
                "answer": "Pentagon"
            },
            {
                "q": "What is 25% of 200?",
                "options": ["25", "40", "50", "75"],
                "answer": "50"
            }
        ],

        "Science": [
            {
                "q": "Which microorganism is commonly used in making curd?",
                "options": ["Virus", "Lactobacillus", "Algae", "Protozoa"],
                "answer": "Lactobacillus"
            },
            {
                "q": "Which force pulls objects towards the Earth?",
                "options": ["Magnetic force", "Friction", "Gravitational force", "Muscular force"],
                "answer": "Gravitational force"
            },
            {
                "q": "Which organ helps humans in breathing?",
                "options": ["Heart", "Lungs", "Kidney", "Stomach"],
                "answer": "Lungs"
            },
            {
                "q": "What is the process by which plants make food?",
                "options": ["Respiration", "Photosynthesis", "Digestion", "Transpiration"],
                "answer": "Photosynthesis"
            },
            {
                "q": "Which of these is a non-renewable resource?",
                "options": ["Sunlight", "Wind", "Coal", "Water"],
                "answer": "Coal"
            },
            {
                "q": "Which part of a cell controls most cell activities?",
                "options": ["Cell wall", "Nucleus", "Cytoplasm", "Vacuole"],
                "answer": "Nucleus"
            }
        ],

        "Social Science": [
            {
                "q": "Who was the first Mughal emperor of India?",
                "options": ["Akbar", "Babur", "Shah Jahan", "Aurangzeb"],
                "answer": "Babur"
            },
            {
                "q": "Which is the largest continent?",
                "options": ["Africa", "Europe", "Asia", "Australia"],
                "answer": "Asia"
            },
            {
                "q": "What is the main function of Parliament?",
                "options": [
                    "Making laws",
                    "Running schools",
                    "Building roads",
                    "Conducting exams"
                ],
                "answer": "Making laws"
            },
            {
                "q": "Which soil is suitable for growing cotton?",
                "options": ["Black soil", "Sandy soil", "Mountain soil", "Laterite soil"],
                "answer": "Black soil"
            },
            {
                "q": "What is democracy?",
                "options": [
                    "Rule by one person",
                    "Rule by the people",
                    "Rule by the army",
                    "Rule by a king"
                ],
                "answer": "Rule by the people"
            }
        ],

        "English": [
            {
                "q": "Choose the correct plural of 'child'.",
                "options": ["Childs", "Children", "Childes", "Childrens"],
                "answer": "Children"
            },
            {
                "q": "Identify the adjective: 'The beautiful flower bloomed.'",
                "options": ["The", "Beautiful", "Flower", "Bloomed"],
                "answer": "Beautiful"
            },
            {
                "q": "Choose the correct verb: 'She ___ to school every day.'",
                "options": ["go", "goes", "going", "gone"],
                "answer": "goes"
            },
            {
                "q": "What is the opposite of 'ancient'?",
                "options": ["Old", "Modern", "Historic", "Past"],
                "answer": "Modern"
            }
        ],

        "AI": [
            {
                "q": "What does AI stand for?",
                "options": [
                    "Automatic Internet",
                    "Artificial Intelligence",
                    "Advanced Information",
                    "Automated Input"
                ],
                "answer": "Artificial Intelligence"
            },
            {
                "q": "Which is an example of AI?",
                "options": [
                    "Voice assistant",
                    "Notebook",
                    "Pencil",
                    "Chair"
                ],
                "answer": "Voice assistant"
            },
            {
                "q": "What is data?",
                "options": [
                    "Information collected for processing",
                    "Only numbers",
                    "Only pictures",
                    "Computer hardware"
                ],
                "answer": "Information collected for processing"
            }
        ]
    },


    # ========================================================
    # CLASS 9
    # ========================================================

    9: {

        "Maths": [
            {
                "q": "What is the degree of a linear polynomial?",
                "options": ["0", "1", "2", "3"],
                "answer": "1"
            },
            {
                "q": "What is the value of √81?",
                "options": ["7", "8", "9", "10"],
                "answer": "9"
            },
            {
                "q": "The coordinates of the origin are:",
                "options": ["(1,1)", "(0,1)", "(1,0)", "(0,0)"],
                "answer": "(0,0)"
            },
            {
                "q": "A triangle having all three sides equal is called:",
                "options": [
                    "Scalene triangle",
                    "Isosceles triangle",
                    "Equilateral triangle",
                    "Right triangle"
                ],
                "answer": "Equilateral triangle"
            },
            {
                "q": "What is the probability of getting a head when a fair coin is tossed?",
                "options": ["0", "1/4", "1/2", "1"],
                "answer": "1/2"
            }
        ],

        "Science": [
            {
                "q": "What is the SI unit of force?",
                "options": ["Joule", "Newton", "Watt", "Pascal"],
                "answer": "Newton"
            },
            {
                "q": "Which state of matter has a definite volume but no definite shape?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": "Liquid"
            },
            {
                "q": "What is the basic unit of life?",
                "options": ["Tissue", "Organ", "Cell", "Organ system"],
                "answer": "Cell"
            },
            {
                "q": "Which gas is essential for respiration?",
                "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"],
                "answer": "Oxygen"
            },
            {
                "q": "What is the acceleration due to gravity near Earth's surface approximately?",
                "options": ["2.8 m/s²", "5.6 m/s²", "9.8 m/s²", "15 m/s²"],
                "answer": "9.8 m/s²"
            }
        ],

        "Social Science": [
            {
                "q": "Which event is associated with the beginning of the French Revolution?",
                "options": [
                    "Storming of the Bastille",
                    "Industrial Revolution",
                    "World War I",
                    "Russian Revolution"
                ],
                "answer": "Storming of the Bastille"
            },
            {
                "q": "Which imaginary line divides Earth into Northern and Southern Hemispheres?",
                "options": [
                    "Tropic of Cancer",
                    "Equator",
                    "Prime Meridian",
                    "Tropic of Capricorn"
                ],
                "answer": "Equator"
            },
            {
                "q": "What is the Constitution?",
                "options": [
                    "A set of fundamental rules",
                    "A newspaper",
                    "A political party",
                    "A court order"
                ],
                "answer": "A set of fundamental rules"
            },
            {
                "q": "Which sector includes farming and fishing?",
                "options": [
                    "Primary sector",
                    "Secondary sector",
                    "Tertiary sector",
                    "Service sector"
                ],
                "answer": "Primary sector"
            }
        ],

        "English": [
            {
                "q": "Choose the correct form: 'They ___ playing cricket.'",
                "options": ["is", "am", "are", "was"],
                "answer": "are"
            },
            {
                "q": "Identify the noun: 'The teacher entered the classroom.'",
                "options": ["teacher", "entered", "the", "classroom"],
                "answer": "teacher"
            },
            {
                "q": "What is a synonym of 'rapid'?",
                "options": ["Slow", "Fast", "Weak", "Quiet"],
                "answer": "Fast"
            },
            {
                "q": "Which tense is used in 'She has completed her work'?",
                "options": [
                    "Simple past",
                    "Present perfect",
                    "Simple present",
                    "Future tense"
                ],
                "answer": "Present perfect"
            }
        ],

        "AI": [
            {
                "q": "Which of the following is a common application of AI?",
                "options": [
                    "Recommendation systems",
                    "Paper books",
                    "Wooden tables",
                    "Manual clocks"
                ],
                "answer": "Recommendation systems"
            },
            {
                "q": "What is machine learning?",
                "options": [
                    "A method where computers learn patterns from data",
                    "Making computer hardware",
                    "Typing documents",
                    "Installing software"
                ],
                "answer": "A method where computers learn patterns from data"
            },
            {
                "q": "Which technology is commonly used to understand human language?",
                "options": [
                    "NLP",
                    "GPS",
                    "USB",
                    "HTML"
                ],
                "answer": "NLP"
            }
        ]
    },


    # ========================================================
    # CLASS 10
    # ========================================================

    10: {

        "Maths": [
            {
                "q": "What is the HCF of 36 and 48?",
                "options": ["6", "8", "12", "16"],
                "answer": "12"
            },
            {
                "q": "What is the discriminant of ax² + bx + c?",
                "options": [
                    "a² - 4bc",
                    "b² - 4ac",
                    "b² + 4ac",
                    "a² + 4bc"
                ],
                "answer": "b² - 4ac"
            },
            {
                "q": "What is the value of sin 90°?",
                "options": ["0", "1/2", "1", "√3/2"],
                "answer": "1"
            },
            {
                "q": "The distance between two points is calculated using:",
                "options": [
                    "Distance formula",
                    "Midpoint formula only",
                    "Area formula",
                    "Heron's formula"
                ],
                "answer": "Distance formula"
            },
            {
                "q": "If the probability of an event is 1, the event is:",
                "options": [
                    "Impossible",
                    "Certain",
                    "Unlikely",
                    "Random"
                ],
                "answer": "Certain"
            }
        ],

        "Science": [
            {
                "q": "What is the pH of a neutral solution at room temperature approximately?",
                "options": ["0", "5", "7", "14"],
                "answer": "7"
            },
            {
                "q": "Which acid is present in vinegar?",
                "options": [
                    "Hydrochloric acid",
                    "Acetic acid",
                    "Sulfuric acid",
                    "Nitric acid"
                ],
                "answer": "Acetic acid"
            },
            {
                "q": "Which part of the human brain controls balance and coordination?",
                "options": [
                    "Cerebrum",
                    "Cerebellum",
                    "Medulla",
                    "Spinal cord"
                ],
                "answer": "Cerebellum"
            },
            {
                "q": "Which phenomenon causes a rainbow?",
                "options": [
                    "Dispersion of light",
                    "Reflection only",
                    "Magnetism",
                    "Conduction"
                ],
                "answer": "Dispersion of light"
            },
            {
                "q": "Which gas is released during photosynthesis?",
                "options": [
                    "Oxygen",
                    "Nitrogen",
                    "Hydrogen",
                    "Methane"
                ],
                "answer": "Oxygen"
            }
        ],

        "Social Science": [
            {
                "q": "Which movement was launched by Mahatma Gandhi in 1930?",
                "options": [
                    "Non-Cooperation Movement",
                    "Civil Disobedience Movement",
                    "Quit India Movement",
                    "Swadeshi Movement"
                ],
                "answer": "Civil Disobedience Movement"
            },
            {
                "q": "Which is the most abundant gas in Earth's atmosphere?",
                "options": [
                    "Oxygen",
                    "Nitrogen",
                    "Carbon dioxide",
                    "Hydrogen"
                ],
                "answer": "Nitrogen"
            },
            {
                "q": "What is federalism?",
                "options": [
                    "Division of power between levels of government",
                    "Rule by a king",
                    "Rule by the military",
                    "Absence of government"
                ],
                "answer": "Division of power between levels of government"
            },
            {
                "q": "Which sector includes banking and transport?",
                "options": [
                    "Primary",
                    "Secondary",
                    "Tertiary",
                    "Agricultural"
                ],
                "answer": "Tertiary"
            }
        ],

        "English": [
            {
                "q": "Which figure of speech compares two things using 'like' or 'as'?",
                "options": [
                    "Metaphor",
                    "Simile",
                    "Personification",
                    "Irony"
                ],
                "answer": "Simile"
            },
            {
                "q": "Choose the correct reported speech: He said, 'I am tired.'",
                "options": [
                    "He said that he was tired.",
                    "He said that I am tired.",
                    "He says he was tired.",
                    "He said he is tired."
                ],
                "answer": "He said that he was tired."
            },
            {
                "q": "What is the opposite of 'optimistic'?",
                "options": [
                    "Hopeful",
                    "Positive",
                    "Pessimistic",
                    "Confident"
                ],
                "answer": "Pessimistic"
            },
            {
                "q": "Which part of a formal letter contains the main message?",
                "options": [
                    "Body",
                    "Address",
                    "Date",
                    "Signature"
                ],
                "answer": "Body"
            }
        ],

        "AI": [
            {
                "q": "What is the purpose of training data in machine learning?",
                "options": [
                    "To teach a model patterns",
                    "To turn off a computer",
                    "To store passwords only",
                    "To connect a printer"
                ],
                "answer": "To teach a model patterns"
            },
            {
                "q": "What does NLP stand for?",
                "options": [
                    "Natural Language Processing",
                    "Network Learning Program",
                    "New Language Protocol",
                    "Natural Logic Process"
                ],
                "answer": "Natural Language Processing"
            },
            {
                "q": "Which is an example of computer vision?",
                "options": [
                    "Image recognition",
                    "Text printing",
                    "Keyboard typing",
                    "File compression"
                ],
                "answer": "Image recognition"
            },
            {
                "q": "Why is data privacy important in AI?",
                "options": [
                    "It protects personal information",
                    "It makes computers heavier",
                    "It increases screen size",
                    "It removes the need for data"
                ],
                "answer": "It protects personal information"
            }
        ]
    }
}


# ============================================================
# QUESTION GENERATOR
# ============================================================

def generate_questions(class_number, subject, number_of_questions):
    """Generate random questions for selected class and subject."""

    questions = QUESTION_BANK[class_number][subject]

    # If requested number is greater than available questions,
    # allow questions to repeat.
    if number_of_questions <= len(questions):
        return random.sample(questions, number_of_questions)

    return random.choices(questions, k=number_of_questions)


# ============================================================
# QUIZ FUNCTION
# ============================================================

def start_quiz(class_number, subject, number_of_questions):

    questions = generate_questions(
        class_number,
        subject,
        number_of_questions
    )

    score = 0

    print("\n" + "=" * 60)
    print("           CBSE STUDENT PRACTICE QUIZ")
    print("=" * 60)

    print(f"Class   : {class_number}")
    print(f"Subject : {subject}")
    print(f"Questions: {number_of_questions}")
    print("=" * 60)

    for i, question in enumerate(questions, start=1):

        print(f"\nQuestion {i}:")
        print(question["q"])

        for j, option in enumerate(question["options"], start=1):
            print(f"{j}. {option}")

        while True:
            try:
                choice = int(input("Enter your answer (1-4): "))

                if 1 <= choice <= 4:
                    break

                print("Please enter a number between 1 and 4.")

            except ValueError:
                print("Please enter a valid number.")

        selected_answer = question["options"][choice - 1]

        if selected_answer == question["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Incorrect.")
            print("Correct answer:", question["answer"])

    percentage = (score / number_of_questions) * 100

    print("\n" + "=" * 60)
    print("                 RESULT")
    print("=" * 60)

    print(f"Score      : {score}/{number_of_questions}")
    print(f"Percentage : {percentage:.1f}%")

    if percentage >= 80:
        print("Performance: Excellent")
    elif percentage >= 60:
        print("Performance: Good")
    elif percentage >= 40:
        print("Performance: Needs Improvement")
    else:
        print("Performance: More Practice Recommended")

    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n==============================================")
    print("     📚 CBSE PERSONALIZED PRACTICE SYSTEM")
    print("==============================================")

    print("\nAvailable Classes:")
    print("8")
    print("9")
    print("10")

    while True:
        try:
            class_number = int(input("\nEnter your class (8-10): "))

            if class_number in QUESTION_BANK:
                break

            print("Please select Class 8, 9 or 10.")

        except ValueError:
            print("Please enter a valid class.")

    subjects = list(QUESTION_BANK[class_number].keys())

    print("\nAvailable Subjects:")

    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")

    while True:
        try:
            subject_choice = int(input("\nSelect subject: "))

            if 1 <= subject_choice <= len(subjects):
                subject = subjects[subject_choice - 1]
                break

            print("Select a valid subject number.")

        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            number_of_questions = int(
                input("\nHow many questions? (10-15): ")
            )

            if 10 <= number_of_questions <= 15:
                break

            print("Please enter a number between 10 and 15.")

        except ValueError:
            print("Enter a valid number.")

    start_quiz(
        class_number,
        subject,
        number_of_questions
    )


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()


    import json
import random
import os
from datetime import datetime

PROFILE_FILE = "student_profiles.json"


# ============================================================
# SAMPLE NCERT-ALIGNED QUESTION BANK
# ============================================================
# You can expand this with questions from the chapters you
# actually teach/use. Avoid copying large portions of textbooks.

QUESTION_BANK = {

    "Mathematics": {

        8: [
            {
                "q": "What is the additive inverse of -7/9?",
                "options": ["7/9", "-7/9", "9/7", "0"],
                "answer": 0
            },
            {
                "q": "What is the square of 15?",
                "options": ["125", "225", "250", "215"],
                "answer": 1
            },
            {
                "q": "If x + 5 = 12, what is x?",
                "options": ["5", "6", "7", "8"],
                "answer": 2
            },
            {
                "q": "A polygon with 5 sides is called a:",
                "options": ["Quadrilateral", "Pentagon", "Hexagon", "Triangle"],
                "answer": 1
            },
            {
                "q": "What is 25% of 200?",
                "options": ["25", "40", "50", "75"],
                "answer": 2
            },
            {
                "q": "The cube root of 64 is:",
                "options": ["2", "4", "6", "8"],
                "answer": 1
            },
            {
                "q": "How many diagonals does a quadrilateral have?",
                "options": ["1", "2", "3", "4"],
                "answer": 1
            },
            {
                "q": "What is the perimeter of a square of side 6 cm?",
                "options": ["12 cm", "18 cm", "24 cm", "36 cm"],
                "answer": 2
            },
            {
                "q": "The probability of an impossible event is:",
                "options": ["0", "1", "2", "0.5"],
                "answer": 0
            },
            {
                "q": "Which number is irrational?",
                "options": ["4", "9", "√2", "16"],
                "answer": 2
            }
        ],

        9: [
            {
                "q": "Which of the following is a polynomial?",
                "options": ["1/x", "x² + 2x + 1", "√x", "1/(x+1)"],
                "answer": 1
            },
            {
                "q": "The degree of 5x³ + 2x² + 1 is:",
                "options": ["1", "2", "3", "5"],
                "answer": 2
            },
            {
                "q": "The coordinates of the origin are:",
                "options": ["(1,1)", "(0,0)", "(0,1)", "(1,0)"],
                "answer": 1
            },
            {
                "q": "A linear equation in two variables has:",
                "options": ["No solution", "One solution", "Infinitely many solutions", "Only two solutions"],
                "answer": 2
            },
            {
                "q": "The sum of angles of a triangle is:",
                "options": ["90°", "180°", "270°", "360°"],
                "answer": 1
            },
            {
                "q": "The probability of a certain event is:",
                "options": ["0", "0.5", "1", "2"],
                "answer": 2
            },
            {
                "q": "The distance between (0,0) and (3,4) is:",
                "options": ["3", "4", "5", "7"],
                "answer": 2
            },
            {
                "q": "A quadrilateral with all sides equal is called a:",
                "options": ["Rectangle", "Rhombus", "Trapezium", "Kite"],
                "answer": 1
            },
            {
                "q": "What is the median of 2, 4, 6, 8, 10?",
                "options": ["4", "5", "6", "8"],
                "answer": 2
            },
            {
                "q": "The square root of 144 is:",
                "options": ["10", "11", "12", "14"],
                "answer": 2
            }
        ],

        10: [
            {
                "q": "The roots of x² - 5x + 6 are:",
                "options": ["2 and 3", "1 and 6", "3 and 4", "2 and 4"],
                "answer": 0
            },
            {
                "q": "The discriminant of ax² + bx + c is:",
                "options": ["b² + 4ac", "b² - 4ac", "a² - 4bc", "4ac - b²"],
                "answer": 1
            },
            {
                "q": "sin 90° is:",
                "options": ["0", "1", "1/2", "√3/2"],
                "answer": 1
            },
            {
                "q": "The distance formula is:",
                "options": [
                    "√((x₂-x₁)²+(y₂-y₁)²)",
                    "x₂-x₁",
                    "y₂-y₁",
                    "(x₁+x₂)/2"
                ],
                "answer": 0
            },
            {
                "q": "The nth term of an arithmetic progression is:",
                "options": [
                    "a + (n-1)d",
                    "a + nd",
                    "an + d",
                    "a - nd"
                ],
                "answer": 0
            },
            {
                "q": "The probability of an event always lies between:",
                "options": ["-1 and 1", "0 and 1", "1 and 2", "0 and 100"],
                "answer": 1
            },
            {
                "q": "If two triangles are similar, their corresponding angles are:",
                "options": ["Unequal", "Equal", "Always 90°", "Always 60°"],
                "answer": 1
            },
            {
                "q": "The circumference of a circle is:",
                "options": ["πr²", "2πr", "πd²", "r²"],
                "answer": 1
            },
            {
                "q": "A quadratic equation has maximum how many roots?",
                "options": ["1", "2", "3", "4"],
                "answer": 1
            },
            {
                "q": "tan 45° is:",
                "options": ["0", "1", "√3", "1/√3"],
                "answer": 1
            }
        ]
    },


    "Science": {

        8: [
            {
                "q": "The process by which green plants prepare food is called:",
                "options": ["Respiration", "Photosynthesis",
                            "Digestion", "Transpiration"],
                "answer": 1
            },
            {
                "q": "The basic unit of life is:",
                "options": ["Tissue", "Organ", "Cell", "Organ system"],
                "answer": 2
            },
            {
                "q": "Which microorganism is used to make bread?",
                "options": ["Yeast", "Virus", "Algae", "Protozoa"],
                "answer": 0
            },
            {
                "q": "Coal and petroleum are:",
                "options": [
                    "Renewable resources",
                    "Fossil fuels",
                    "Metals",
                    "Minerals only"
                ],
                "answer": 1
            },
            {
                "q": "Which force pulls objects towards Earth?",
                "options": ["Friction", "Magnetic force",
                            "Gravitational force", "Muscular force"],
                "answer": 2
            },
            {
                "q": "The SI unit of pressure is:",
                "options": ["Newton", "Pascal", "Joule", "Watt"],
                "answer": 1
            },
            {
                "q": "Sound cannot travel through:",
                "options": ["Air", "Water", "Steel", "Vacuum"],
                "answer": 3
            },
            {
                "q": "Which organ pumps blood through the body?",
                "options": ["Lungs", "Heart", "Kidney", "Brain"],
                "answer": 1
            },
            {
                "q": "Friction generally acts:",
                "options": [
                    "In the direction of motion",
                    "Opposite to relative motion",
                    "Vertically",
                    "Upwards only"
                ],
                "answer": 1
            },
            {
                "q": "Which gas is essential for respiration?",
                "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"],
                "answer": 1
            }
        ],

        9: [
            {
                "q": "The smallest unit of an element that retains its chemical properties is:",
                "options": ["Cell", "Atom", "Tissue", "Molecule only"],
                "answer": 1
            },
            {
                "q": "The SI unit of force is:",
                "options": ["Joule", "Newton", "Pascal", "Watt"],
                "answer": 1
            },
            {
                "q": "Which particle has a negative charge?",
                "options": ["Proton", "Electron", "Neutron", "Nucleus"],
                "answer": 1
            },
            {
                "q": "The acceleration due to gravity on Earth is approximately:",
                "options": ["9.8 m/s²", "98 m/s²", "0.98 m/s²", "8 m/s²"],
                "answer": 0
            },
            {
                "q": "Which tissue transports water in plants?",
                "options": ["Phloem", "Xylem", "Epidermis", "Parenchyma"],
                "answer": 1
            },
            {
                "q": "The chemical formula of water is:",
                "options": ["CO₂", "H₂O", "O₂", "H₂"],
                "answer": 1
            },
            {
                "q": "Which law states that mass is neither created nor destroyed in a chemical reaction?",
                "options": [
                    "Law of conservation of mass",
                    "Law of gravitation",
                    "Ohm's law",
                    "Newton's law"
                ],
                "answer": 0
            },
            {
                "q": "The movement of particles from higher concentration to lower concentration is:",
                "options": ["Osmosis", "Diffusion", "Filtration", "Evaporation"],
                "answer": 1
            },
            {
                "q": "Which cell organelle is known as the powerhouse of the cell?",
                "options": ["Nucleus", "Mitochondria", "Ribosome", "Vacuole"],
                "answer": 1
            },
            {
                "q": "Work is said to be done when force produces:",
                "options": ["Mass", "Displacement", "Temperature", "Pressure"],
                "answer": 1
            }
        ],

        10: [
            {
                "q": "The pH of a neutral solution at room temperature is approximately:",
                "options": ["0", "5", "7", "14"],
                "answer": 2
            },
            {
                "q": "Which gas is released when an acid reacts with a metal?",
                "options": ["Oxygen", "Hydrogen", "Nitrogen", "Chlorine"],
                "answer": 1
            },
            {
                "q": "The functional unit of the kidney is:",
                "options": ["Neuron", "Nephron", "Alveolus", "Villus"],
                "answer": 1
            },
            {
                "q": "Ohm's law is represented by:",
                "options": ["V = IR", "P = VI", "F = ma", "W = mg"],
                "answer": 0
            },
            {
                "q": "The SI unit of electric current is:",
                "options": ["Volt", "Ampere", "Ohm", "Watt"],
                "answer": 1
            },
            {
                "q": "Which part of the brain controls balance and coordination?",
                "options": ["Cerebrum", "Cerebellum", "Medulla", "Spinal cord"],
                "answer": 1
            },
            {
                "q": "The process of conversion of glucose into energy in cells is associated with:",
                "options": ["Respiration", "Photosynthesis",
                            "Transpiration", "Excretion"],
                "answer": 0
            },
            {
                "q": "A convex lens is generally:",
                "options": [
                    "Converging",
                    "Diverging",
                    "Flat",
                    "Opaque"
                ],
                "answer": 0
            },
            {
                "q": "DNA is primarily responsible for:",
                "options": [
                    "Digestion",
                    "Heredity",
                    "Respiration",
                    "Blood circulation"
                ],
                "answer": 1
            },
            {
                "q": "The chemical formula of methane is:",
                "options": ["CH₄", "C₂H₆", "CO₂", "CH₃OH"],
                "answer": 0
            }
        ]
    },


    "Social Science": {

        8: [
            {
                "q": "Who was the first Governor-General of independent India?",
                "options": ["Lord Mountbatten", "Warren Hastings",
                            "Lord Curzon", "Robert Clive"],
                "answer": 0
            },
            {
                "q": "The Indian Constitution came into effect on:",
                "options": [
                    "15 August 1947",
                    "26 January 1950",
                    "26 November 1949",
                    "2 October 1950"
                ],
                "answer": 1
            },
            {
                "q": "Which institution makes laws for the country?",
                "options": ["Parliament", "Police", "Court", "Election Commission"],
                "answer": 0
            },
            {
                "q": "Which sector includes farming?",
                "options": ["Primary", "Secondary", "Tertiary", "IT"],
                "answer": 0
            },
            {
                "q": "A government elected by the people is called:",
                "options": ["Monarchy", "Democracy", "Dictatorship", "Empire"],
                "answer": 1
            },
            {
                "q": "The Himalayas are located in the:",
                "options": ["North of India", "South of India",
                            "East only", "West only"],
                "answer": 0
            },
            {
                "q": "The Constitution guarantees:",
                "options": [
                    "Fundamental Rights",
                    "Only economic rights",
                    "Only voting rights",
                    "No rights"
                ],
                "answer": 0
            },
            {
                "q": "Which is a renewable resource?",
                "options": ["Coal", "Petroleum", "Solar energy", "Natural gas"],
                "answer": 2
            },
            {
                "q": "The Mughal Empire was founded by:",
                "options": ["Akbar", "Babur", "Shah Jahan", "Aurangzeb"],
                "answer": 1
            },
            {
                "q": "The Equator divides Earth into:",
                "options": [
                    "Eastern and Western hemispheres",
                    "Northern and Southern hemispheres",
                    "Four parts",
                    "Tropical zones"
                ],
                "answer": 1
            }
        ],

        9: [
            {
                "q": "The French Revolution began in:",
                "options": ["1789", "1776", "1857", "1947"],
                "answer": 0
            },
            {
                "q": "Democracy means government by:",
                "options": ["A king", "The people", "The army", "Judges"],
                "answer": 1
            },
            {
                "q": "The Green Revolution is associated mainly with:",
                "options": ["Industry", "Agriculture", "Transport", "Banking"],
                "answer": 1
            },
            {
                "q": "The Tropic of Cancer passes through:",
                "options": ["India", "Australia", "UK", "Brazil only"],
                "answer": 0
            },
            {
                "q": "The Indian Constitution was drafted by the:",
                "options": [
                    "Constituent Assembly",
                    "Supreme Court",
                    "Election Commission",
                    "Planning Commission"
                ],
                "answer": 0
            },
            {
                "q": "Which is an example of a primary activity?",
                "options": ["Banking", "Farming", "Teaching", "Manufacturing"],
                "answer": 1
            },
            {
                "q": "Monsoon winds are important for India's:",
                "options": ["Agriculture", "Space programme",
                            "Railways", "Mining only"],
                "answer": 0
            },
            {
                "q": "The voting age in India is:",
                "options": ["16", "18", "21", "25"],
                "answer": 1
            },
            {
                "q": "A constitution provides a framework for:",
                "options": [
                    "Government",
                    "Weather",
                    "Agriculture only",
                    "Trade only"
                ],
                "answer": 0
            },
            {
                "q": "The Industrial Revolution first began in:",
                "options": ["Britain", "India", "Japan", "China"],
                "answer": 0
            }
        ],

        10: [
            {
                "q": "Power sharing is important because it:",
                "options": [
                    "Reduces the possibility of conflict",
                    "Ends elections",
                    "Creates dictatorship",
                    "Removes democracy"
                ],
                "answer": 0
            },
            {
                "q": "Federalism involves:",
                "options": [
                    "One level of government only",
                    "Multiple levels of government",
                    "No government",
                    "Military government"
                ],
                "answer": 1
            },
            {
                "q": "GDP measures the value of:",
                "options": [
                    "Final goods and services",
                    "Only agricultural products",
                    "Only imports",
                    "Only exports"
                ],
                "answer": 0
            },
            {
                "q": "Which organisation publishes the Human Development Report?",
                "options": ["UNDP", "WHO", "WTO", "UNESCO"],
                "answer": 0
            },
            {
                "q": "Globalisation involves increased:",
                "options": [
                    "International interconnectedness",
                    "Isolation",
                    "Local production only",
                    "Barter only"
                ],
                "answer": 0
            },
            {
                "q": "The Civil Disobedience Movement was associated with:",
                "options": [
                    "Mahatma Gandhi",
                    "Lord Curzon",
                    "Robert Clive",
                    "Dalhousie"
                ],
                "answer": 0
            },
            {
                "q": "Which is a non-renewable resource?",
                "options": ["Solar energy", "Wind", "Coal", "Water"],
                "answer": 2
            },
            {
                "q": "The tertiary sector provides:",
                "options": [
                    "Services",
                    "Only crops",
                    "Only minerals",
                    "Only manufactured goods"
                ],
                "answer": 0
            },
            {
                "q": "Democratic government is based on:",
                "options": [
                    "Popular participation",
                    "Hereditary rule",
                    "Military rule",
                    "Absolute monarchy"
                ],
                "answer": 0
            },
            {
                "q": "The Consumer Protection Act is intended to protect:",
                "options": ["Consumers", "Only producers",
                            "Only exporters", "Only banks"],
                "answer": 0
            }
        ]
    }
}


# ============================================================
# ENGLISH
# ============================================================

ENGLISH_QUESTIONS = {

    8: [
        ("Choose the correct form: She ___ to school every day.",
         ["go", "goes", "going", "gone"], 1),

        ("A word used instead of a noun is called a:",
         ["Verb", "Pronoun", "Adjective", "Adverb"], 1),

        ("Choose the synonym of 'happy'.",
         ["Sad", "Joyful", "Angry", "Tired"], 1),

        ("Which is a proper noun?",
         ["city", "school", "India", "river"], 2),

        ("Identify the adjective: 'The beautiful flower bloomed.'",
         ["flower", "bloomed", "beautiful", "the"], 2),

        ("What is the past tense of 'go'?",
         ["goed", "gone", "went", "going"], 2),

        ("Choose the correct article: ___ apple.",
         ["A", "An", "The", "No article"], 1),

        ("A sentence that asks a question is:",
         ["Assertive", "Interrogative", "Imperative", "Exclamatory"], 1),

        ("Choose the antonym of 'ancient'.",
         ["Old", "Modern", "Historic", "Past"], 1),

        ("Which word is an adverb?",
         ["Quickly", "Quick", "Quickness", "Quicken"], 0)
    ],

    9: [
        ("Identify the noun: 'The teacher explained the lesson.'",
         ["teacher", "explained", "the", "lesson only"], 0),

        ("Choose the correct modal: You ___ obey traffic rules.",
         ["should", "might", "could", "would"], 0),

        ("The opposite of 'expand' is:",
         ["Increase", "Contract", "Grow", "Extend"], 1),

        ("A group of words expressing a complete thought is a:",
         ["Phrase", "Sentence", "Word", "Clause only"], 1),

        ("Choose the correct passive form: 'They built the house.'",
         ["The house was built by them.",
          "The house built them.",
          "They were built.",
          "The house is build."], 0),

        ("Identify the conjunction: 'I stayed home because it rained.'",
         ["I", "stayed", "because", "rained"], 2),

        ("The comparative form of 'good' is:",
         ["gooder", "better", "best", "more good"], 1),

        ("Which is a compound word?",
         ["beautiful", "sunlight", "running", "quickly"], 1),

        ("Choose the correct spelling:",
         ["Necessary", "Necesary", "Neccessary", "Necesarry"], 0),

        ("A figure of speech comparing using 'like' or 'as' is:",
         ["Metaphor", "Simile", "Personification", "Irony"], 1)
    ],

    10: [
        ("Choose the correct reported speech: He said, 'I am tired.'",
         ["He said that he was tired.",
          "He said that I am tired.",
          "He says he tired.",
          "He said he is tired."], 0),

        ("Which is an example of a metaphor?",
         ["He runs like a deer.",
          "Time is a thief.",
          "The sky is blue.",
          "She sings loudly."], 1),

        ("The opposite of 'optimistic' is:",
         ["Hopeful", "Pessimistic", "Cheerful", "Positive"], 1),

        ("Identify the subordinate clause: 'I stayed home because I was ill.'",
         ["I stayed home", "because I was ill",
          "I", "home"], 1),

        ("The passive form of 'The boy opened the door' is:",
         ["The door was opened by the boy.",
          "The door opened the boy.",
          "The boy was opened.",
          "The door is opening."], 0),

        ("Choose the correct preposition: He is good ___ mathematics.",
         ["in", "at", "on", "for"], 1),

        ("A poem's central idea is called its:",
         ["Theme", "Rhyme", "Stanza", "Meter only"], 0),

        ("Which is an example of alliteration?",
         ["Big brown bears bark.",
          "The sun is bright.",
          "She is happy.",
          "The bird flew."], 0),

        ("The plural of 'criterion' is:",
         ["criterions", "criteria", "criterion", "criterias"], 1),

        ("Choose the correct conditional sentence:",
         ["If it rains, we will stay home.",
          "If it rained, we stay home.",
          "If it rains, we stayed home.",
          "If rain, home."], 0)
    ]
}


# ============================================================
# PROFILE FUNCTIONS
# ============================================================

def load_profiles():

    if os.path.exists(PROFILE_FILE):

        try:
            with open(PROFILE_FILE, "r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return {}

    return {}


def save_profiles(profiles):

    with open(PROFILE_FILE, "w", encoding="utf-8") as file:

        json.dump(
            profiles,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# CREATE / LOAD STUDENT PROFILE
# ============================================================

def get_student_profile():

    profiles = load_profiles()

    name = input("\nEnter student name: ").strip()

    if name in profiles:

        print("\nWelcome back,", name)

        print(
            "Previous overall score:",
            profiles[name].get("overall_percentage", 0),
            "%"
        )

        return profiles, name

    print("\nNew student profile")

    while True:

        try:
            student_class = int(input("Enter class (8, 9 or 10): "))

            if student_class in [8, 9, 10]:
                break

            print("Please enter only 8, 9 or 10.")

        except ValueError:
            print("Enter a valid class.")

    profiles[name] = {

        "name": name,

        "class": student_class,

        "created_on": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "subjects": {},

        "quiz_history": [],

        "overall_percentage": 0

    }

    save_profiles(profiles)

    return profiles, name


# ============================================================
# CONVERT ENGLISH QUESTIONS
# ============================================================

def get_english_questions(student_class):

    questions = []

    for question, options, answer in ENGLISH_QUESTIONS[student_class]:

        questions.append({

            "q": question,

            "options": options,

            "answer": answer

        })

    return questions


# ============================================================
# RUN QUIZ
# ============================================================

def run_quiz(subject, student_class):

    if subject == "English":

        questions = get_english_questions(student_class)

    else:

        questions = QUESTION_BANK[subject][student_class]

    # Select 10 questions.
    # Change 10 to 15 if you add at least 15 questions
    # to each question bank.

    number_of_questions = min(10, len(questions))

    selected_questions = random.sample(
        questions,
        number_of_questions
    )

    score = 0

    print("\n")
    print("=" * 60)
    print(subject.upper(), "PRACTICE QUIZ")
    print("=" * 60)

    for number, question in enumerate(
        selected_questions,
        start=1
    ):

        print(f"\nQuestion {number}/{number_of_questions}")
        print(question["q"])

        for index, option in enumerate(
            question["options"],
            start=1
        ):

            print(f"{index}. {option}")

        while True:

            try:

                answer = int(
                    input("Your answer (1-4): ")
                )

                if 1 <= answer <= 4:
                    break

                print("Enter a number from 1 to 4.")

            except ValueError:

                print("Enter a valid number.")

        if answer - 1 == question["answer"]:

            print("Correct!")
            score += 1

        else:

            correct_option = question["options"][
                question["answer"]
            ]

            print(
                "Incorrect. Correct answer:",
                correct_option
            )

    percentage = (score / number_of_questions) * 100

    print("\n" + "-" * 60)
    print(f"{subject} Result")
    print("-" * 60)
    print(f"Marks: {score}/{number_of_questions}")
    print(f"Percentage: {percentage:.2f}%")

    return score, number_of_questions, percentage


# ============================================================
# UPDATE PROFILE
# ============================================================

def update_profile(
    profiles,
    name,
    subject,
    score,
    total,
    percentage
):

    profile = profiles[name]

    if subject not in profile["subjects"]:

        profile["subjects"][subject] = {

            "tests_taken": 0,

            "total_marks": 0,

            "total_questions": 0,

            "best_percentage": 0,

            "latest_percentage": 0

        }

    subject_data = profile["subjects"][subject]

    subject_data["tests_taken"] += 1

    subject_data["total_marks"] += score

    subject_data["total_questions"] += total

    subject_data["latest_percentage"] = round(
        percentage,
        2
    )

    subject_data["best_percentage"] = max(
        subject_data["best_percentage"],
        round(percentage, 2)
    )

    profile["quiz_history"].append({

        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "subject": subject,

        "marks": score,

        "total": total,

        "percentage": round(percentage, 2)

    })

    # Calculate overall performance from all subjects

    total_marks = 0
    total_questions = 0

    for data in profile["subjects"].values():

        total_marks += data["total_marks"]

        total_questions += data["total_questions"]

    if total_questions > 0:

        profile["overall_percentage"] = round(
            (total_marks / total_questions) * 100,
            2
        )

    save_profiles(profiles)


# ============================================================
# DISPLAY PROFILE
# ============================================================

def show_profile(profiles, name):

    profile = profiles[name]

    print("\n")
    print("=" * 60)
    print("STUDENT ACADEMIC PROFILE")
    print("=" * 60)

    print("Name:", profile["name"])
    print("Class:", profile["class"])

    print(
        "Overall Percentage:",
        profile["overall_percentage"],
        "%"
    )

    print("\nSUBJECT PERFORMANCE")
    print("-" * 60)

    if not profile["subjects"]:

        print("No quizzes completed yet.")

    else:

        for subject, data in profile["subjects"].items():

            print(f"\n{subject}")

            print(
                "  Tests:",
                data["tests_taken"]
            )

            print(
                "  Latest:",
                data["latest_percentage"],
                "%"
            )

            print(
                "  Best:",
                data["best_percentage"],
                "%"
            )

            print(
                "  Total marks:",
                data["total_marks"],
                "/",
                data["total_questions"]
            )

    print("\n" + "=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("=" * 60)
    print("PERSONALIZED CBSE LEARNING AGENT")
    print("=" * 60)

    profiles, name = get_student_profile()

    student_class = profiles[name]["class"]

    subjects = [
        "Mathematics",
        "Science",
        "Social Science",
        "English"
    ]

    while True:

        print("\n")
        print("=" * 60)
        print("MAIN MENU")
        print("=" * 60)

        print("1. Take a practice quiz")
        print("2. View my academic profile")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            print("\nAvailable subjects:")

            for i, subject in enumerate(
                subjects,
                start=1
            ):

                print(f"{i}. {subject}")

            while True:

                try:

                    subject_choice = int(
                        input(
                            "\nSelect subject: "
                        )
                    )

                    if 1 <= subject_choice <= len(subjects):
                        break

                    print("Invalid choice.")

                except ValueError:

                    print("Enter a valid number.")

            subject = subjects[
                subject_choice - 1
            ]

            score, total, percentage = run_quiz(
                subject,
                student_class
            )

            # AUTOMATICALLY SAVE MARKS
            update_profile(
                profiles,
                name,
                subject,
                score,
                total,
                percentage
            )

            print(
                "\nYour marks have been automatically "
                "saved to your student profile!"
            )

        elif choice == "2":

            show_profile(
                profiles,
                name
            )

        elif choice == "3":

            print(
                "\nProfile saved successfully."
            )

            print(
                "Thank you for using the "
                "Personalized Learning Agent!"
            )

            break

        else:

            print(
                "Please select 1, 2 or 3."
            )


if __name__ == "__main__":
    main()