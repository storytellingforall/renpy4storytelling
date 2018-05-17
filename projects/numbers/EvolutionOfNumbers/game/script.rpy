#@+leo-ver=5-thin
#@+node:satishgoda.20180516220254.2: * @file script.rpy
# The script of the game goes in this file.

#@+<<defines>>
#@+node:satishgoda.20180516220726.1: ** <<defines>>
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Teacher")
define s = Character("Student")
#@-<<defines>>

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #@+<<dialogue>>
    #@+node:satishgoda.20180516220557.1: ** <<dialogue>>
    # These display lines of dialogue.

    #@+<<part 1>>
    #@+node:satishgoda.20180517150118.1: *3* <<part 1>>
    t "Are you ready to learn about the story of Numbers?"
    s "Yes, I am ready."

    s "Teacher, how were numbers born?"
    t "The origin of numbers is cloaked in mystery."
    t "As civilizations advanced, numbers advanced with it."
    t "Civilizations could not have advanced without numbers."
    s "Wow, so interesting. I want to learn more about numbers."
    #@-<<part 1>>
    #@-<<dialogue>>

    # This ends the game.

    return
#@-leo
