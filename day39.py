Questions = [
    ["What is the capital of France?", "Paris", "London", "Berlin", "Madrid", 1],
    ["Who wrote 'Romeo and Juliet'?", "Shakespeare", "Dickens", "Austen", "Hemingway", 1],
    ["What is the square root of 64?", "6", "7", "8", "9", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Who painted the Mona Lisa?", "Van Gogh", "Picasso", "Da Vinci", "Monet", 3],
    ["What is the boiling point of water?", "100°C", "90°C", "110°C", "120°C", 1],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Osmium", "Ozone", "Opium", 1],
    ["What is the tallest mountain in the world?", "Mount Everest", "K2", "Kangchenjunga", "Makalu", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Thailand", 3]
]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
money = 0

for i in range(len(Questions)):
    Question = Questions[i]
    print(f"a. {Question[1]}    b. {Question[2]}")
    print(f"c. {Question[3]}    d. {Question[4]}")
    print(f"Question for Rs.{levels[i]}")
    
    reply = int(input("Enter your answer [1-4]: "))
    
    if reply == Question[-1]:
        print(f"Correct answer! You have won Rs.{levels[i]}")
        money += levels[i]
        
        if i == len(Questions) - 1:
            print(f"Congratulations! You won a total of Rs.{money}")
            break
    else:
        print("Wrong answer!")
        break
    

print(f"Game Over! You won Rs.{money}")
