# print('''
#                                                    ,--,  ,.-.
#                      ,                   \,       '-,-`,'-.' | ._
#                     /|           \    ,   |\         }  )/  / `-,',
#                     [ '          |\  /|   | |        /  \|  |/`  ,`
#                     | |       ,.`  `,` `, | |  _,...(   (      _',
#         -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
#          -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
#                       \  '  `  ,_ _`_,-,<._.<        /         /
#                        ', `>.,`  `  `   ,., |_      |         /
#                          \/`  `,   `   ,`  | /__,.-`    _,   `\
#                      -,-..\  _  \  `  /  ,  / `._) _,-\`       \
#                       \_,,.) /\    ` /  / ) (-,, ``    ,        |
#                      ,` )  | \_\       '-`  |  `(               \
#                     /  /```(   , --, ,' \   |`<`    ,            |
#                    /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
#              ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
#             (-, \           ) \ ('_.-._)/ /,`    /
#             | /  `          `/ \\ V   V, /`     /
#          ,--\(        ,     <_/`\\     ||      /
#         (   ,``-     \/|         \-A.A-`|     /
#        ,>,_ )_,..(    )\          -,,_-`  _--`
#       (_ \|`   _,/_  /  \_            ,--`
#        \( `   <.,../`     `-.._   _,-`
#         `                      ```
#
#
# ''')
print("Welcome to Treasure Island.")
print("Your mission is run away from the monster and find the treasure.")

# Write your code
# Left or right
fork = input("You're running away from the monster. You see a fork in the road. Do you go left or right?\n")

if fork == "left":
    print("You escaped into the woods and found a body of water.")
    # Swim or wait
    swim_or_wait = input("The monster found you by scent. Do you swim or wait?\n").lower()
    if swim_or_wait == "wait":
        print("Multiple doors teleported in front of you.")
        # Pick a  colored door
        door = input("You see three doors. Do you choose the red, blue, or yellow door?\n").lower()
        if door == "red":
            print("You were burned by fire. Game over.")
        if door == "blue":
            print("You were eaten by beasts. Game over.")
        if door == "yellow":
            print("You escaped the monster and found the treasure. You win!")

    else:
        print("A giant snapping turtle bit off your legs. Game over.")
else:
    print("You've fallen into a trap and the monster has killed you. Game Over.")
          
          
          
          
          




