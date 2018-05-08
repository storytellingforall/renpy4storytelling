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

    menu:
        "A":
            jump A
        "B":
            jump B
        "C":
            jump C


    label A:
        "A" 'is for ...'
    menu:
        "Apple": 
            jump apple
        "Antelope":
            jump antelope 
    label apple:
        show apple at truecenter
        "A" 'is for Apple'
        hide apple
        jump start
    label antelope:
        show antelope at truecenter
        "A" 'is for Antelope'
        hide antelope
        jump start

        
    label B:
        "B" 'is for ...'
    menu:
        "Ball":
            jump ball
        "Baloon":
            jump baloon
    label ball:
        show ball at truecenter
        "B" 'is for Ball'
        hide ball
        jump start
    label baloon:
        show baloon at truecenter
        "B" 'is for Balloon'
        hide baloon
        jump start 
    

    label C:
        "C" 'is for ...'
    menu:
        "Cat":
            jump cat
        "Carrot":
            jump carrot
    label cat:
        show cat at truecenter
        "C" 'is for Cat'
        hide cat
        jump start
    label carrot:
        show carrot at truecenter
        "C" 'is for Carrot'
        hide carrot
        jump start

    # This ends the game.

    return
