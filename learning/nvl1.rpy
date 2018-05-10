# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define samhita = Character("Samhita", kind=nvl)
define swetha = Character("Amma", kind=nvl)

define narrator = nvl_narrator
define menu = nvl_menu

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    ##

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    ##

    # These display lines of dialogue.
    
    "I'll ask her..."

    samhita "Um... will you..."
    samhita "Will you buy me a bicycle amma?"

    nvl clear

    "Silence."
    "She is thinking deeply, and then..."

    swetha "Sure, we will buy it this weekend!"

    samhita "Yayayayaaya!"

    nvl clear

    swetha "Samhita, which color bicycle do you want?"

    menu:
        "Blue":
            jump BLUE
        "Red":
            jump RED

    label BLUE:
        swetha "Ok, Blue color bicylce it is"
        jump start
    label RED:
        swetha "Ok, Red color bicycle it is"
        jump start

    # This ends the game.

    return
