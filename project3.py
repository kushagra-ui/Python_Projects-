import random

easy_words = ["apple" , "banana" ,"computer", "greenland"]
medium_words = ["Canada","Russia","Neerupma","Kushagra"]
hard_words= ["programming","refrigerator","air conditioner","compresion"]

print("Welcome to the word guessing game!")
print("Choose a difficulty level :easy ,medium, hard ")
level = input("Enter Difficulty !").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium" :
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Input . Default to easy level. ") 
    secret = random.choice(easy_words)

attempts = 0
print("/n Guess the secret word")

while True:
    guess = input("Enter your guess : ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessd it in {attempts} attempts ")
        break
    hint = ""


    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else :
            hint += "_"
    print("Hint:" + hint)

print("Game Over ! ")




