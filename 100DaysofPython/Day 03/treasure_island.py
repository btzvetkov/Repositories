print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision = input('''You are now on a mysterious island where old captain Flack 
Barrow shipwrecked the Track Furl and hid the crazy treasure.
Type whether you want to go "Left" or "Right":''').lower()

if decision == "right":
    print('''You chose to go right. You walk for a few meters and fall into a
          hole that was created by the captain to build a swimming pool.
                                                +---+
                                      |\   \
  +-----------------------------+     | +---+
   \                      +-----------+ |   |
    \                      \            |   |
     \                 |/   +-----------+   |
      \                (c_      |   \ | |   |
       \                \       |    \| |   |
        \                       |     | |   |
         \                      |     + |   |
          \                     |      \| DM|
           \--------------------+       +---+
            \                    \        \\
             \                    \        \\
              +-----------------------------+
          Game over.''')
elif decision == "Left" or decision == "left" or decision == 'LEFT':
    print('''You chose to go left. You walk for a few minutes and reach a lake.
          It looks muddy and suspicious but you don't see any boat around and 
          you are not sure how much time do you have before you get caught.''')
    decision = input('What will you do: "swim" or "wait"?').lower()
    if decision == 'swim':
        print('''You chose to swim. The water is heavy but you manage to go through
              you see the other shore in the far and attempt to reach it but you get stuck.
              A crocodile who hasn't had anything for breakfast comes buy and eats you like
              a popcorn.
                                  .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'

              Game over.''')
    elif decision == 'wait':
        print("""You decided to wait. As the minutes go by you actually notice a boat that was 
              hidden a few minutes ago as it was a bit foggy on the coast when you arrived.
              You take the boat and sail until you reach the other end of the lake.
              Once you get there you see a wooden structure that has three doors:
              Red, yellow and blue. What would you do? """)
        decision = input ('''To open a door enter the color: 
                          "Red", "Yellow" or "Blue". 
                          To do something else, type: "else".
                          So what's your decision? ''').lower()
        if decision == "red":
            print('''You chose to open the red door. As soon as you do that 100 kg of TNT
                  blow up and you are consumed by the explosion.
  +----------------------------------------------------------------------+
 |                                                                      |
 |         ______________________________       . \  | / .              |
 |        /                            / \        \ \ / /               |
 |        |       Chris Young          |{========= >- -<                |
 |        \____________________________\_/        / / \ \               |
 |                                              . /  | \ .              |
 |                                                                      |
 +----------------------------------------------------------------------+
 
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  Game over.''')
        elif decision == "yellow":
            print('''You chose to open the yellow door. It is a very narrow door. However,
                  you manage to go through it. You enter a small room and there is a chest.
                  You open it and there is the treasure. You come back happy buy a house and
                  a Tesla, then live happily ever after with the love of your life!
                .---------------.
              /       oLo       \\
            O/_____/________/____\O
            /__________+__________\\
           /    (#############)    \\
           |[**](#############)[**]|
           \_______________________/
            |_""__|_,-----,_|__""_|
            | |     '-----'     | |  APC'97
            '-'                 '-'
            
                  ,--.
     //^\\\   ,;;;,                        .                  
    ((-_-))) (-_- ;                       /_\                  
     )))(((   >..'.    .:.     .--.      |SSt|                  
    ((_._ )  /.   .|  :-_-;   /-_-))                  
    _))A ((_//| S ||  ,`-'.   ))-((                  
    `(    )`' |___|),;, C \\_/,`I ))                  
      \  /    | | |`' |___(/-'|___()  ,-.                  
       )(     | | |   | | |   | | |  (-_-)    _____                  
      /__\    |_|_|   |_|_|   |_|_|  (\I/\.__|A|R|T|                  
      `''     `-'-'   `-'-'   `-'-'  `'-`'   `o' `o'                  
                  You win!''')
        elif decision == "blue":
            print('''You chose to open the blue door. You enter a garden, looks suspicious 
                  but anyway you move on - you have decided to not look back. Then you
                  get swallowed and eaten up by a hoard of beasts.
            |
   \`-. _.._| 
    |_,'  __`. 
    (.\ _/.| _  |
   ,'      __ \ |
 ,'     __/||\  |
(Y8P  ,/|||||/  |
   `-'_----    /
      /`-._.-'/
      `-.__.-' jg
                  Game over!''')
        elif decision == "else":
            print('''You are wondering what to do, then suddenly you realise you are 
                  late for your dentist appointment.
            /-----|
         \-'      |
           Q      |
      )C ~\/\     |
       \\_   \    |
        \_77 |\   |
ejm 96   |`` \ \  |
        """  ~ ~ ===
                  Game over.''')
        else:
            decision = 'typomonster'
    else:
        decision = 'typomonster'
else:
    decision = 'typomonster'

if decision == 'typomonster':    
    print('''The typist monster eats you because you typed your answer wrong.
          
        .         __      '        .       '       .
  *            _-~  ~-_      .         '      .
 .   .        /___  ___\  '             .             .
             / (O)  (o) \         *         ___    *  .
   __,-~-~-,/    -..-    \  .-~~-.   __..-~~   ~~-.._
.-~  `V~V~V'`\ -v----v-   \/     /.-~  //..  \   \.  `~-._
  //.     \.' `\..___..---/    /''    .    '   .   ..
                     ''/ \\..'  \'   V~V~V'  //  /  ' .  ' /  \ . '  \\\ \ \\
.    ' / .                   / '    .    /  <> \  '.  . ' .
 / ../ '  ( Hey mate!)  // ' ../  <> / .'\ \'  ''.\ \\
/.  //. \ ( You thought I )       ________________
           (  cannot read, ) //' /  __   _  _____ \ ..' \ \\
 './   \'\   ( did you?  )        | |__  /_\   |   |
 ..         \         \\    //' . | |__ /   \  |   | '.  \..
___...---..._____..--~~\\..____..-\________________/..__
                        \\               ||  .    .
   .           .      .  ` ______________||_________.  .
                            |_____________________|  '
      .       ~             |    |    |     |  |  |  .
  .       .           ..    |____|____|_____|==|__|
                            |____|____|_____|__|__|   jro
                  __________________________________
'        .       /                                 /
     .     ~    /                                 /

0000000000000000000000000000000000000000000000000000000000000
          
          Game over.''')