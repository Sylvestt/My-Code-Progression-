class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, solution):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.solution = solution

    def get_question(self):
        return self.question

    def get_answers(self):
        return [self.answer1, self.answer2, self.answer3, self.answer4]

    def get_solution(self):
        return self.solution

    def __str__(self):
        return f"{self.question}\n1: {self.answer1}\n2: {self.answer2}\n3: {self.answer3}\n4: {self.answer4}"

def get_trivia_questions():
    questions = [
        Question("What is the name of Naruto's mother?", "Kushina", "Kaguya", "Kurama", "Sakura", 1),
        Question("Who was Sakura's Master?", "Tsunade", "Kakashi", "Jiraiya", "Orochimaru", 1),
        Question("What is the name of Naruto's son?", "Boruto", "Naruto", "Sarada", "Mitsuki", 1),
        Question("Who is the 1st Hokage?", "Madara", "Tobirama", "Hashirama", "Kakashi", 3),
        Question("What is the name of Luffy's pirate crew in 'One Piece'?", "Straw Hat Pirates", "Red Hair Pirates", "Whitebeard Pirates", "Blackbeard Pirates", 1),
        Question("Who is known as the 'Pirate King' in 'One Piece'?", "Gol D. Roger", "Monkey D. Luffy", "Whitebeard", "Blackbeard", 1),
        Question("What is the name of the main character in 'Attack on Titan'?", "Eren Yeager", "Levi Ackerman", "Mikasa Ackerman", "Armin Arlert", 1),
        Question("What is the name of the main character in 'My Hero Academia'?", "Izuku Midoriya", "Katsuki Bakugo", "Shoto Todoroki", "Ochaco Uraraka", 1),
        Question("Who is known as the 'Strongest Hero' in 'My Hero Academia'?", "All Might", "Endeavor", "Hawks", "Best Jeanist", 1),
        Question("What is the name of the giant humanoid creatures in 'Attack on Titan'?", "Titans", "Giants", "Colossals", "Eldians", 1),
        Question("Who is the captain of the 'Straw Hat Pirates' in 'One Piece'?", "Zoro", "Nami", "Sanji", "Luffy", 4),
        Question("What is the name of Naruto's rival in 'Naruto'?", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake", "Shikamaru Nara", 1),
        Question("Who is the captain of Squad 11 in 'Bleach'?", "Ichigo Kurosaki", "Byakuya Kuchiki", "Renji Abarai", "Kenpachi Zaraki", 4),
        Question("What is the name of the main character in 'Dragon Ball Z'?", "Goku", "Vegeta", "Piccolo", "Gohan", 1),
        Question("Who is known as the 'Prince of Saiyans' in 'Dragon Ball Z'?", "Goku", "Vegeta", "Piccolo", "Krillin", 2),
        Question("What is the name of the magical world in 'Fairy Tail'?", "Fiore", "Magnolia", "Edolas", "Alvarez", 1),
        Question("Who is known as the 'Salamander' in 'Fairy Tail'?", "Gray Fullbuster", "Natsu Dragneel", "Erza Scarlet", "Lucy Heartfilia", 2),
        Question("What is the name of the organization in 'Naruto' that Sasuke joins after leaving the Leaf Village?", "Akatsuki", "Sound Village", "Hidden Rain Village", "Orochimaru's Army", 1),
        Question("Who is the protagonist in 'Death Note'?", "Light Yagami", "L", "Misa Amane", "Ryuk", 1),
        Question("What is the name of the sword wielded by Ichigo Kurosaki in 'Bleach'?", "Zangetsu", "Senbonzakura", "Tensa Zangetsu", "Bankai", 3)
    ]
    return questions

def get_player_choice(player_name):
    while True:
        try:
            choice = int(input(f"Enter your choice {player_name}: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a valid choice (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    print("Welcome to the ultimate Anime trivia game!")
    player1_name = input("Please enter your name, Player 1: ")
    player2_name = input("Please enter your name, Player 2: ")
    player1_score = 0
    player2_score = 0
    questions = get_trivia_questions()

    for i in range(20):
        # Player 1's turn
        print(f"\nQuestion {i + 1} for {player1_name}:")
        print(questions[0-20])
        player1_choice = get_player_choice(player1_name)
        if player1_choice == questions[i].get_solution():
            player1_score += 1

        # Player 2's turn
        print(f"\nQuestion {i + 1} for {player2_name}:")
        print(questions[0-20])
        player2_choice = get_player_choice(player2_name)
        if player2_choice == questions[i].get_solution():
            player2_score += 1

    print(f"\n{player1_name} earned a total score of {player1_score} out of 20!")
    print(f"{player2_name} earned a total score of {player2_score} out of 20!")

    if player1_score > player2_score:
        print(f"Congratulations to {player1_name}, the winner!")
    elif player2_score > player1_score:
        print(f"Congratulations to {player2_name}, the winner!")
    else:
        print("It's a tie!")

    print("Thank you for playing the trivia game!")

if __name__ == "__main__":
    main()
