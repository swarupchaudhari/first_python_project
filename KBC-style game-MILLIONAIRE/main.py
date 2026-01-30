# main.py

questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote Romeo and Juliet?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2],
    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3]
]

prizes = [
    100000, 200000, 300000, 400000,
    500000, 750000, 1000000, 1500000,
    2000000, 3000000, 4000000, 5000000
]

total_prize = 0
option_map = {"a": 1, "b": 2, "c": 3, "d": 4}

print("🎉 Welcome to the Quiz Game 🎉")

for i, question in enumerate(questions):
    print("\nQ", i + 1, ":", question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    answer = input("Enter your answer (a/b/c/d): ").lower()

    if answer not in option_map:
        print("❌ Invalid input! Game Over.")
        break

    answer_number = option_map[answer]

    if answer_number == question[5]:
        total_prize += prizes[i]
        print("✅ Correct Answer!")
        print(f"💰 You won ₹{prizes[i]}")
        print(f"🏦 Total Prize Money: ₹{total_prize}")
    else:
        print(f"❌ Wrong Answer! Correct option was {question[5]}")
        break

print("\n🎮 Game Over")
print(f"🏆 Final Prize Money: ₹{total_prize}")