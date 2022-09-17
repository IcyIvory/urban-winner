def hello(emotion):
    match emotion:
        case "happy":
            return "Heya, user! :)"
        case "angry":
            return "Hey, fuckwad. You look like shit."
        case "sad":
            return "Hey. :("
        case _:
            return "Hello."


emotion = " "
while emotion != "quit":
    emotion = input("Please enter an emotion (happy, sad, angry), or 'quit' to quit: ")
    if emotion != "quit":
        print(hello(emotion))
    else:
        print("Goodbye.")