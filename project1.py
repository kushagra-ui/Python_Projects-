# Fake News Headline  Generator
# import the random module 
import random
print("Welcome to the Fake News Headline Generator")
subjects = [ "shahrukh khan",
"Prime Minister",
"Goa",
"Virat Kohli",
"Cancer",
"Sagittarius"]



actions=["visits", 
        "abused",
        "become",
        "ordered",
        "not harmful"
        ,"stablize"
        ]





places_of_things= ["Kanpur",
                   "Nirmala",
                   "peaceful",
                   "jammu and kashmir",
                   "for humans",
                   "business"
                   ]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places=  random.choice(places_of_things)

    headline= f"BREAKING NEWS :{subject} {action} {places}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline ? (y/n )").strip()
    if user_input == "no":
        break

print("Thankyou for using the Fake news headline generator ")

