# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gui.text_size = 190
#define gui.text_box_height = 1000

#define narrator = nvl_narrator
#define menu = nvl_menu

# The game starts here.

init python:
    if renpy.windows:
        config.tts_voice = "Zira" # Mark, David
    elif renpy.macintosh:
        config.tts_voice = "Alex"
    elif renpy.linux:
        config.tts_voice = "english_rp"

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    menu:
        "Pre-K - Sight Word List 1":
            jump PreKWL1
           
        "Pre-K - Sight Word List 2":
            jump PreKWL2

        "Pre-K - Sight Word List 3":
            jump PreKWL3

        "Pre-K - Sight Word List 4":
            jump PreKWL4

        "Kindergarten - Sight Word List 1":
            jump KWL1

    # This ends the game.
    return
