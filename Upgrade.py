print("Hello and welcome to this or that game!")
print("You have often seen those 'this or that' questions on social media.")
print("In this game, you will be presented with two options, and you have to choose one.")
print("Let's get started!")
name = input("First, please enter your name: ")
print(f"Great to meet you, {name}! Let's begin the game.")
print("Would you rather have the ability to fly or be invisible?")
choice = input("Type 'fly' to choose flying or 'invisible' to choose invisibility: ")
if choice.lower() == 'fly':
    print("You chose to fly! Soaring through the skies sounds amazing!")
elif choice.lower() == 'invisible':
    print("You chose to be invisible! Sneaking around unseen is quite the power!")
else:
    print("Invalid choice. Please choose either 'fly' or 'invisible'.")
print("Would you rather live in the mountains or by the beach?")
choice = input("Type 'mountains' to choose the mountains or 'beach' to choose the beach: ")
if choice.lower() == 'mountains':
    print("You chose the mountains! Enjoy the fresh air and stunning views!")
elif choice.lower() == 'beach':
    print("You chose the beach! Relaxing by the ocean sounds perfect!")
else:
    print("Invalid choice. Please choose either 'mountains' or 'beach'.")
print("would you rather have a pet dragon or a pet unicorn?")
choice = input("Type 'dragon' to choose a pet dragon or 'unicorn' to choose a pet unicorn: ")
if choice.lower() == 'dragon':
    print("You chose a pet dragon! That's a fiery and majestic companion!")
elif choice.lower() == 'unicorn':
    print("You chose a pet unicorn! A magical and beautiful friend!")
else:
    print("Invalid choice. Please choose either 'dragon' or 'unicorn'.")
print("would you rather be able to speak all languages or play all musical instruments?")
choice = input("Type 'languages' to choose speaking all languages or 'instruments' to choose playing all musical instruments: ")
if choice.lower() == 'languages':
    print("You chose to speak all languages! Communication with anyone around the world is now possible!")
elif choice.lower() == 'instruments':
    print("You chose to play all musical instruments! You can create beautiful music anytime!")
else:
    print("Invalid choice. Please choose either 'languages' or 'instruments'.")
    print("I have a fun question for you!")
print("Would you rather travel to the past or the future?")
choice = input("Type 'past' to choose traveling to the past or 'future' to choose traveling to the future: ")
if choice.lower() == 'past':
    print("You chose to travel to the past! Exploring history firsthand sounds fascinating!")
elif choice.lower() == 'future':
    print("You chose to travel to the future! Seeing what lies ahead is exciting!")
else:
    print("Invalid choice. Please choose either 'past' or 'future'.")
    print("This question is made for only football lovers!")
    print("messi or ronaldo?")
choice = input("Type 'messi' to choose Messi or 'ronaldo' to choose Ronaldo: ")
if choice.lower() == 'messi':
    print("You chose Messi! An incredible player with amazing skills!")
elif choice.lower() == 'ronaldo':
    print("You chose Ronaldo! A phenomenal athlete with unmatched talent!")
else:
    print("Invalid choice. Please choose either 'messi' or 'ronaldo'.")
print("Thanks for playing the game! Hope you had fun making your choices!")