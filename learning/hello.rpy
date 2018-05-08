# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define samhita = Character("Samhita", color="#ff0000")
define amma = Character("Amma", color="#00ff00")
define nanna = Character("Nanna", color="#0000ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show samhita happy at truecenter

    # These display lines of dialogue.

    samhita "Hi Amma. Hi Nanna."
    hide samhita
    
    show amma focussed at truecenter
    amma "Hi buchuku."
    hide amma
    
    show nanna smiling at truecenter
    nanna "Hi Samhita."
    hide nanna

    show samhita happy at truecenter
    samhita "Amma!! I am hungry!!"
    hide samhita

    show amma focussed at truecenter
    amma "Okay. I will make you dosa. Please go and wash your face, hands and legs."
    hide amma

    show samhita happy at truecenter
    samhita "OK."

    samhita "Nanna!!! I want to play Dinosaur games."
    hide samhita

    show nanna smiling at truecenter
    nanna "Sure, But after you wash and eat your snack."
    hide nanna

    show samhita happy at truecenter
    samhita "OK."

    # This ends the game.

    return
