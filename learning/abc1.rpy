# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## 

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    ## ...

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    ## ...

    # These display lines of dialogue.

    "A" 'is for ...'
    show apple 1 at truecenter
    pause 1
    "A" 'is for Apple'

    hide apple

    "B" 'is for ...'
    show ball 1 at truecenter
    with dissolve
    pause 2
    "B" 'is for Ball'

    hide ball

    "C" 'is for ...'
    show cat 1 at truecenter
    with fade
    pause 3
    "C" 'is for Cat'

    hide cat

    # This ends the game.

    return
