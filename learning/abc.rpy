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

    show apple 1 at truecenter
    "A" 'is for Apple'
    hide apple

    show ball 1 at truecenter
    "B" 'is for Ball'
    hide ball

    show cat 1 at truecenter
    "C" 'is for Cat'
    hide cat

    # This ends the game.

    return
