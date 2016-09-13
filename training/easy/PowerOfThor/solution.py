import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]

deltaX = LX - TX
deltaY = LY - TY

posX = TX
posY = TY

# game loop
while 1:
    E = int(input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    #print(inp, file=sys.stderr)
    
    command = ""
    
    if (posY > LY):
        command = command + "N"
        posY -= 1
    elif (posY < LY):
        command = command + "S"
        posY += 1
    
    
    if (posX < LX):
        command = command + "E"
        posX += 1
    elif (posX > LX):
        command = command + "W"
        posX -= 1
        
    
    print(command) # A single line providing the move to be made: N NE E SE S SW W or NW

