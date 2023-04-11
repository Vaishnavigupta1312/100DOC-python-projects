print('''
                                 A
                                / \
                               /   \
              A               <_____>
             / \            _ _|_Y_|_ _
            /   \           ]=I=I=I=I=[
           <_____>           \-|-|-|-/
         _ _|_Y_|_ _          |     |
         ]=I=I=I=I=[         _|_ _  |            A
          \-|-|-|-/          ]=I=[  |      A    / \
           |     |    A       \|/   |     / \  /   \
           |     |   / \      |Y    |    /   \<_____>
           | /^\ |  /   \     |     |   <_____>|   |
           | | | | <_____>    | []  | _ _|_Y_|_|   |
           | |_| |  |   |     |     | ]=I=I=I=I|   |
           |     | _|_Y_|_ _  |     |  \-|-|_ _|_Y_|_ _
           |     |=I=I=I=I=[  |  [] |       ]=I=I=I=I=[
        _ _|_ _ _|_-_-|-|-/_ _|_ _ _|_ /^\   \-|-|-|-/
        ]=I=I=I=I=I=[    | ]=I=I=I=I=I=|O|    |     |
         \-|-|-|-|-/     |  \-\-|-|-/-/ \|    | /^\ |
          |    [] | _ _ _|_ _|  _____|_ |     | | | |
          | []    |=I=I=I=I=[| /vvvvvvv\|     | === |
       _ _|_ _ _ _|_-_-|-|-/ |/vvvvvvvvv\     |     |
       ]=I=I=I=I=I=I=[    |  <===========> _ _|_ _ _|_ _
        \-\--|-|--/-/     |  || []   [] |  ]=I=I=I=I=I=[
         |         | _ _ _|_ ||_ _ _ _ _|_ _\--|-|-|--/
         |         |=I=I=I=I=I=I=I=I=I=I=I=I=|       |
         | []      |-=-=-=-=-=-=-=-=-=-=-=-=-|     []|
         |         |           ___           |       |
         |         |          /   \          |       |
         |         |         |     |         |       |
       _/|         |\_       |     |       _/|       |\_


''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
turn = input("In search of treasure you want to head 'left' or 'right'? \n").lower()
if turn == "right":
  print ("You fell in the hole.Game Over")
else :
    print ("You are in the middle of a sea.")
    wait= input("Would like to 'wait' for the boat or will 'swim' till the shore? \n").lower()
    if wait == "swim":
      print('''You got eaten by a crocodile.
            Game Over''')
    else :
      print("Boat took you to the castle, there are three doors.")
      door = input("Which would you like to open, 'Red', 'Blue' or 'Yellow' ? \n").lower()
      if door=="yellow":
        print("You found the treasure. You won!!!")
      else :
        print("Starving Lion inside the door ate you.")

