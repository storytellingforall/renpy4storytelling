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

    label PreKWL1:
        "and"
        "for"
        "a"
        "can"
        "make"
        "me"
        "my"
        "not"
        "red"
        "run"
        #nvl clear 
        jump start
    
    label PreKWL2:
        "here"
        "little"
        "it"
        "jump"
        "is"
        "funny"
        "in"
        "go"
        "help"
        "I" 
        #nvl clear
        jump start

    label PreKWL3:
        "blue"
        "come"
        "big"
        "down"
        "away"
        "find"
        "play"
        "look"
        "one"
        "said"
        #nvl clear
        jump start

    label PreKWL4:
        "see"
        "the"
        "three"
        "to"
        "two"
        "up"
        "we"
        "where"
        "yellow"
        "you"
        #nvl clear
        jump start

    # This ends the game.

    return
