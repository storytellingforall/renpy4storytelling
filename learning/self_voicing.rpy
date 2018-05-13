# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


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
   
    sv "Hello!!! welcome to the Dolch Words game. I hope you enjoy playing this fun and instructive game."
 
    "Funny"

    "To"

    "Felicitous"

    "But"

    "Sanctimonious"

    "The End." with vpunch

    # This ends the game.

    return
