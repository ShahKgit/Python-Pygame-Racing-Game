#setting up python
import os 
import random #importing random library so we can use random in our program
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
import pygame #importing pygame for the graphical interface.
pygame.init() #initializinge pygame
#defining colors
RED = (255, 0, 0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)

SIZE = (750, 500) #establishing screen dimensions
screen = pygame.display.set_mode(SIZE)
KEY_SPACE = False #this is a boolean which is true if the space key is pressed and vice versa
KEY_COMMA = False #I am setting up this variable for commas because commas can not be entered for the name of the user (because commas will mess up the formatting because commas are how we seperate data fields.)
KEY_PRESSED = False #this boolean is true when the user is pressing a key and vice versa
KEY_BACKSPACE = False #boolean for if the backspace is being pressed

healthX = 750 #x position of health power up
fireX = 700 #x position of fire obstacle
fireY = 0 #y position of the fire obstacle
healthY = random.choice([175,270,365]) #y position of health power up, picks random position between the three lanes
hitTime = 0 #variable that keeps track of time when player gets hit
#Defining the different fonts that I use throughout the game
myFont = pygame.font.SysFont("Times New Roman",20)
myFont2 = pygame.font.SysFont("Times New Roman", 100)
menuFont = pygame.font.SysFont("Roboto", 30)
titleFont = pygame.font.SysFont("Roboto", 50)
fireYList = [175,270,365] #List of positions that the fire could be at
count = 0 #x position of the player
countY = 0 #y position of the player
bulletsList = [] #bullets list is the list which contains all the bullets
stopwatch2 = 0 #stopwatch 2 is a variable that keeps track of how long the helicopter should be shown for 
greenObstacleX = 750 #x is the x value of the green obstacles
greenObstacleY = 300 #y is the y value of the green obstacles
greenObstacleFixed = False #greenObstacleFixed is a boolean that is being used for the green obstacles. I named it the way I did because I am fixing the position of the green obstacle so it doesnt constantly change its y position.
playerX = playerY = 0 #playeX is the x value of the player in the greenObstacle function and playerY is the y value of the player in the greenObstacle function
ewasteDestroyed = 0 #this is the counter that counts how much ewaste you have destroyed
instructionsY = 10 #this is the y position of the text when the instructions are being written through a for loop
instructionsX = 20 #this is the x position of the text when the instructions are beeing written through a for loop
recordVar = [] #this is the list that contains the record for the user when they complete the game. This record will be added to recordsList and thus the leaderboard
playedBool = False #playedBool is a boolean that is true when the user has completed the game and false when the user has not 
playedOnce = 0 #this is a variable that acts as a boolean to make sure that a certain action only acts once. It makes sure that the program only registers the player as having played the game once.
enter = 0 #enter is the variable that acts as a boolean. It is 1 when the enter key is pressed, and 0 when it is not pressed.
playerMode = "safe" #variable that changes its value from "safe" to "hit" depending on if the user is safe or has been hit by an object
lives = 5 #the user starts off with 5 lives
#the different pages
LOSEPAGE = 0  #page for when the user loses
GAMEPAGE = 1  #page for the general game
INFOMENU = 2 #menu
VICTORY = 3 #victory page
INSTRUCTIONS = 4 #instructions page
QUITCOMMAND = 5 #state that is called when the user presses the quit button
LEADERBOARD = 6 #leaderboard
LOGIN = 7 #login page
color = GREEN #color is a variable for the color of the health bar, since the health bar is full it is green
ewasteX = 750 #the x position of the ewaste
ewasteY = 200 #the y position of the ewaste
kilometers = 0 #the distance the player has travelled
myClock = pygame.time.Clock() #setting up the clock for frame rate
bulletX = count + 50 #x position of the users bullet
bulletY = countY + 70 #y position of the users bullet
bulletHit = False #boolean - True when bullet has hit ewaste and vice versa

xPos_textInput = 120 #x position of the text that user types in 
maximum = 10 #the maximum amount of characters that the user can type
textAllowed = True #boolean - true if the user can add text and vice versa

textDisplayList = [] #list that has all the characters that the player has typed into the interface
drawScreenOnce = True #boolean - makes sure that the screen is drawn only once, (so that the text does not be covered by the white background)

boolList = []  #list of booleans for all of the objects
#adding false to the list 5 times because all 5 booleans are false when the program starts
for i in range(5): #the 5 booleans being represented by this list are: ewasteBool, healthBool, helicopterBool, fireBool, greenObstacleBool
  boolList.append(False)

#two roads make up the full big road
backgroundX = 0  #x position of the first road
backgroundX2 = 980 #x position of the second road

ewasteVelocity = 1 #velocity of the e waste
hit = False #boolean - true if the user is hit - vice versa

name = "Anonymous" #name is the name of the player; since they have not yet entered their name it is anonymous

def greenObstacle(): #greenObstacle is a function that contains the code for the green obstacle
  global greenObstacleX,greenObstacleY,greenObstacleFixed,count,countY,playerX,playerY,boolList,menuTime
  shift = 300 #shift is y value at which the slope of the greenObstacle's movement is 0. This value is based off the middle of the road, because at the middle of the froad, the obstacle should be coming straight on instead of at an angle
  if greenObstacleFixed == False: #greenObstacleFixed is false when the program start because we have not fixed the  position of the green obstacle. greenObstacleFixed is being used and then set to true because I only want the indented code to run once. If it runs multiple times then the y position will always be changing
    playerY = countY + 62.5 #setting the y position of the player to the center of the player
    playerX = count  #setting the x position of the player to the x position
    #The reason I am making new variables is because I want them to be static and only take the value of the player and one instant and keep that value.
  greenObstacleFixed = True #the y position and x position of the player and that instant has been determined. the boolean greenObstacleFixed is now true because the positions have been fixed 
  greenObstacleY = ((shift-playerY)/400)*(greenObstacleX) + ((playerY) - (((shift-playerY)/400)*playerX))
  #greenObstacleY is the y value of the line which the green obstacle follows.It is in the form of y = mx + b, where greenObstacleX is the x position of the green obstacle. As x changes y will change, so that the green obstacle ends up going towards the player
  pygame.draw.rect(screen,GREEN,(greenObstacleX,greenObstacleY,100,20)) #drawing the green obstacle and values greenObstacleX and greenObstacleY (the x and y values of the line)
  #changing the speed of the green obstacle depending on how far into the game the player is
  if int((pygame.time.get_ticks()-menuTime)/1000) > 120:
    greenObstacleX-=15 #decreasing greenObstacle by 10 to get the new greenObstacleY value
  elif 90<int((pygame.time.get_ticks() - menuTime)/1000)<=120:
    greenObstacleX-=10 
  else:
    greenObstacleX-=5
    
  if greenObstacleX<0: #if the x position of the greenObstacle is less than 0
    greenObstacleX = 750 #reset the x position
    boolList[4] = False #set boolList[4], which represents the boolean for the greenObstacle, to False.
    greenObstacleFixed = False  #resetting greenObstacleFixed because its position is no longer fixed and it has to reset

def victory(currentState,mx,my): #victory screen
  global kilometers,recordVar,playedBool,playedOnce,ewasteDestroyed,score,name
  pygame.draw.rect(screen,BLUE,(0,0,750,500)) #drawing the background
  drawScene(trophy,375-(trophy.get_width()/2),50) #drawing the trophy image

  drawText(myFont,"You won!",325,20,RED) #drawing text
  drawText(myFont,"Ewaste Destroyed:%i, Distance:4km" %(ewasteDestroyed),200,325,RED) #drawing text that says how much e waste was destroyed, and the distance the player has travelled. Since the player has won the game their distance by defualt is 4 kilometers so I dont need to use the kilometers variable.
  kilometers = 4 #setting kilometers to 4 because if the player has won then they have travelled 4 kilometers
  score = round(kilometers*10 + (ewasteDestroyed),2) #the score is a combinatin of kilometers travelled and the amount of ewaste destroyed
  drawText(myFont,"Score:%.2f" %score,335,360,RED) #drawing the score
  recordVar = [name,"%.2f"%(ewasteDestroyed),"%.2f"%(kilometers),"%.2f"%(score)] #setting recordVar equal to the full record of the player. This will be added to the leaderboard

  if playedOnce == 0: #if playedOnce == 0 which it is when the program starts running
    playedBool = True #set playedBool to true because the program has beenplayed
  playedOnce = 1 #setting playedOnce to 1 because playedBool has already been set to true and I dont want it to be set to true repititvely
  updateData() #update the data 

def updateData():
  global playedBool,recordsList,recordVar
  if playedBool == True: #if the user have finished playing the game
    recordsList.append(recordVar) #add the users record (with their game information) to the list of all the records
    playedBool = False #set playedBool to false because the information has already been appended
  write("info.dat") #write the data to the file
 
def leaderboard(currentState,mx,my):
  pygame.draw.rect(screen,WHITE,(0,0,750,500)) #draw a background
  write("info.dat") #update the data, add the record to the list of records
  drawTable() #drawing the table/leaderboard (with all the records)
  return currentState

def instructions(currentState,mx,my): #this is the instructions page
  global instructionsX,instructionsY
  pygame.draw.rect(screen,YELLOW,(0,0,750,500)) #drawing a yellow background
  instructions = "You are a superhero trying to catch the evil villain, red x.The road is busy with other cars and red x has weapons prepared, so that you do not reach the end.If you reach the end,a total distance of 4 km, then you catch red x and win the game. Red x does not care for the environment and so he has made some of his weapons out of e waste, hoping that they will get rid of you and end up in a landfill. Shoot the e waste that comes towards you to get points. Get the blue rectangle to get all of your health back, but avoid all other obstacles. Your total score is a combination of the total distance you travel and the amount of ewaste you destroy. Can you beat the game?" #the instructions string has most of the instructions in one string

  drawText(menuFont,"Use your mouse to move the player and press the space bar to shoot",20,400,RED) #writing another piece of text. I made it seperate because I want it to be seperate from the first big chunk of text
  spaceCount = 0 #spaceCount is the amount of spaces 
  
  for i in range(len(instructions)): #going through the instructions string
    drawText(menuFont,instructions[i],instructionsX,instructionsY,RED) #drawing all of the letters individually
    instructionsX+=15 #increasing the x position so that we can move on to the next letter
    if instructions[i] == " ": #if the character is a space
      spaceCount+=1 #increase space count by 1, because we have found a space
    if spaceCount > 6: #if there are more than 5 spaces then that means that it is time for us to move to a new line
      spaceCount = 0 #there are 0 spaces on the new line
      instructionsY+=20 #increase the y position, because we are moving on to a new line
      instructionsX = 20 #reset the x position because we are moving on to a new line
  #set the variables back to normal
  spaceCount = 0 
  instructionsX = 20 
  instructionsY = 2
  return currentState
 
def bullets(): #function for bullets being shot from character
  global KEY_SPACE,bulletsList,count,countY,ewasteX,ewasteY,bulletHit,ewasteDestroyed
  if KEY_SPACE == True: #if the user is pressing space
    bulletsList.append([count+50,countY+70]) #add a bullet to bulletsList, a bullet consists of an x position and y position. When a bullet is initialized its x and y positions are the same as that of the player
    KEY_SPACE = False #make KEY_SPACE false because the action has been complete
    
  for i in range(len(bulletsList)): #going through bullets List
    bulletsList[i][0]+=10 #increasing the x value of the bullet by 10
    bulletX = bulletsList[i][0] #bulletX is the x value of the bullet
    bulletY = bulletsList[i][1] #bulletY is the y value of the bullet
    #we used new variables above because we want them to hold the values of bulletsList[i][0] or bulletsList[i][1] at the instant the user shoots the bullet. In other words we dont want the y value of the bullet to change as it moves through the air
    pygame.draw.rect(screen,RED,(bulletX,bulletY,50,20)) #draw the bullet at its x position and y position
    if bulletX>750: #if the bullet is off screen
      del bulletsList[i] #delete that bullet from the list because it is no longer in action
      break #break out of the loop because we are going through a loop but we have just deleted one bullet from it so the program will crash. If we break the program will come back to this for loop but it wont crash because the whole loop will have restarted without that deleted bullet
  if bulletsList!=[]: #if the bullet is not empty
    for i in range(len(bulletsList)): #go through the bullet
      if (ewasteX<bulletsList[i][0]<ewasteX+100) and (ewasteY<bulletsList[i][1]<ewasteY+50): #if the bullet is colliding with the ewaste
        bulletHit = True #set bullet hit to true because the bullet has hit the ewaste
        ewasteDestroyed +=1 #increase ewasteDestroyed because the user has just destroyed ewaste
        break

def movingRestrictions(): #function that restricts the movement of the user
  if mx<375: #if they are in an appropriate range then the player should move to the mouse position of the user
    count = mx - 100
  else:
    count = 275 #otherwise the player should go to the maximum position that the player can be at
  if my>200: #if the y position is in the  appropriate range
    countY = my - 100 #allow them to go to wherever the mouse is
  else:
    countY = 100 #otherwise the player should go to the minimum position that the player can be at
  return count,countY #return the position of the player so that we can store it in the global count and countY variables
  
def livesCheck(currentState): #checks for lives
  global playedOnce
  #goes through different cases depending on the number of lives and changes the color of the health bar
  if lives == 5: 
    color = GREEN
  elif 3<=lives<=4:
    color = ORANGE
  elif 0<lives<=2:
    color = RED
  elif lives == 0: #if the user has 0 lives
    color = RED
    playedOnce = 0  #set playedOnce to be 0 because if playedOnce is 0 then playedBool becomes true and we want it to be true because the player has just finished playing the game
    currentState = LOSEPAGE #go to the lose page because the user has lost
  return color,currentState #returns the currentstate and the color of the health bar
  
def loadImage(imageLocation,widthFactor,heightFactor): #function to load an image
  variable = pygame.image.load(imageLocation).convert_alpha() #loads image and uses convert_alpha (I found online that convert_alpha improves the speed of your program)
  variable = pygame.transform.scale(variable,(variable.get_width()*widthFactor, variable.get_height()*heightFactor)) #scale the image by a certain factor
  return variable #return the variable which can be stored in a global variable depending on the image being loaded ex. tree = loadImage("tree.png",1.2,1.2)
  
def checkLane(): #checking the lane that the user is in, we do this because the fire obstacles always go on the lane that the user is on, this makes it more challenging because the user always has to move out of the way
  global countY
  #checking the y position of the player and determing what lane they are in
  if 153<=countY + 62.5<248: 
    lane = 0
  elif 248<=countY+62.5<343:
    lane = 1
  else:
    lane = 2
  return lane #returning the lane number

def losePage(currentState,mx,my): #page for when the player loses
  global ewasteDestroyed,kilometers,playedBool,score,playedOnce,name,recordVar
  pygame.draw.rect(screen,WHITE,(0,0,1000,700)) #draw white background
  drawText(myFont,"Ewaste Destroyed:%i, Distance:%fkm" %(ewasteDestroyed,kilometers),150,325,BLACK) #display the amount of e waste that the user has destroyed and the total distance they have travelled
  
  score = round(kilometers*10 + (ewasteDestroyed), 2) #calculate the score of the user
  drawText(myFont,"Score:%.2f" %score,335,360,BLACK) #display the score
  loseText = myFont2.render("YOU LOSE", 1, (255,0,0))  #display the losing message 
  screen.blit(loseText,(100,100,200,50))  #blit the message

  recordVar = [name,"%.2f"%(ewasteDestroyed),"%.2f"%(kilometers),"%.2f"%(score)] #creating the record with the users information
  if playedOnce == 0: #if playedOnce = 0 which means that the user has not already played the game
    playedBool = True #set playedBool to true
  playedOnce = 1 #set playedOnce to 1 because the user has already played the game and we do not want the boolean playedBool to constantly be set to true
  updateData() #update the data
  return currentState 
  
def drawText(font,text,xPos,yPos,color): #function to draw text
  text = font.render(text, 1, color)
  screen.blit(text,(xPos,yPos+10,150,50)) #display text

def drawBoxes(box_xPos,xPos,yPos,text): #function to draw the boxes
  #parameters (listed in order) are the x position of the box, the x position of the text, the y position of the text and box (they are both the same) and the string (the actual text)
  pygame.draw.rect(screen, BLACK, (box_xPos,yPos,150,50)) #draw the box with the parameters; customizable x position of box and y position of box
  drawText(menuFont,text,xPos,yPos,YELLOW)

def quitCommand(currentState,mx,my): #function to quit
  pygame.quit() #quits the game
  return currentState

def keyInput(): #variable to display the key that the user has entered
    global xPos_textInput,textAllowed,KEY_BACKSPACE,textDisplayList,K_LSHIFT,K_RSHIFT,evnt,KEY_COMMA,KEY_PRESSED
    if textAllowed == True: #if the user is allowed to enter text  #textAllowed
      yPos = 250 #y position variable
      if KEY_BACKSPACE == True: #if backspace is pressed
        if xPos_textInput >= 135: #if the x position of the text is greater than 135 than backspace can happen, otherwise that means that you are already at the leftmost you can be at the box, because 135 is the leftmost position. Thus, you can not go back more and should not be allowed to.
          pygame.draw.rect(screen,WHITE,(xPos_textInput-15,yPos,40,50)) #draw a rectangle to cover up the text. Draw the rectangle at the y position of the text, and 15 to the left from the position of the character (because the character has a width)
          xPos_textInput-=15 #decrease the x position by 15, because the next character drawn will be be before the character that was deleted
          KEY_BACKSPACE = False #the backspace has just been pressed so it is not being pressed anymore
          del textDisplayList[-1] #delete the last element from the list of the characters that the user has inputted in the program because it has been deleted (that is the function of a backspace) 
        KEY_BACKSPACE = False #the user has already pressed the backspace so make it false now
      if KEY_PRESSED == True: #if a key is being pressed
        if (evnt.unicode!="\x08" and evnt.unicode!="\r"):  #if the character entered is not enter or backspace than execute the following code. the user can not enter those because those are special keys that we have seperate code for   
          if KEY_COMMA == False:
            drawText(myFont,evnt.unicode,xPos_textInput,yPos,BLACK) #draw the character that the user has typed in at xPos_textInput 
          if evnt.key!=pygame.K_LSHIFT and evnt.key!=pygame.K_RSHIFT and evnt.key!=pygame.K_COMMA: #if the key pressed is not shift or comma (because for those keys we dont want to increase the x position)
            xPos_textInput+=15 #increase the x position becasue we are moving on to a new character
            textDisplayList.append(evnt.unicode) #add the key that they entered to a list of the current keys they have entered (the text that is displayed on the screen)
          KEY_PRESSED = False #make KEY_pressed false because they have just pressed it
        
def loginPage(currentState,mx,my): #page for the user to log in
  global drawScreenOnce,enter,name,xPos_textInput,textDisplayList
  drawText(myFont,"Enter the name you want to be associated with your score.",40,70,BLACK)
  drawText(myFont,"Your name must be 10 characters or less.",40,150,BLACK)
  
  if drawScreenOnce == True: #drawScreenOnce is a boolean that we use to make sure that the background if only drawn once. If it is drawn multiple times it will cover the text. Therefore, if drawScreenOnce is true, meaning if this is the first time that we are drawing this screen then draw the background.
    pygame.draw.rect(screen,WHITE,(0,0,750,500)) #draw the background
  drawScreenOnce = False #set drawScreenOnce to false because the background has 
  pygame.draw.rect(screen,BLACK,(115,250,170,40),3) #draw the textbox
  if enter == 1: #if enter has been pressed
    name = "" #set name to an empty string so that we can have a blank sheet to add our new information to
    for i in range(len(textDisplayList)): #going through the list of the characters that the user has inputted
      name+=textDisplayList[i] #adding those characters to the variable name
    if name == "": #if name is empty by default we want to set it to Anonymous
      name = "Anonymous"
    enter = 0 #setting enter to 0 because the enter key has been pressed and its function has been complete. It is no longer being pressed.
    textDisplayList = [] #setting textDisplayList to empty, because we have already gotten the information we need from it and we need to reset it so that the user can change their name later on if they wish 
    xPos_textInput = 120 #reset the x position of the text for the next time the character wants to type their name into the textbox
    currentState = INFOMENU #forcing the program to go back to the menu because the user has completed their login.
  return currentState
  
def infoMenu(currentState,mx,my): #menu page
  global button,menuTime,lives,color,ewasteDestroyed,score,boolList,bulletsList,hit,playerMode,kilometers
  global drawScreenOnce,name,playedOnce,bulletX,bulletY,bulletHit,playedBool,ewasteX,xPos_textInput
  global textDisplayList,KEY_SPACE,carX,healthX,fireX,greenObstacleX
  pygame.draw.rect(screen,(255,50,50),(0,0,800,600)) #draws background
  #drawing buttons
  drawBoxes(300,350,100,"Play") 
  drawBoxes(300,320,175,"Instructions")
  drawBoxes(300,315,250,"Leaderboard")
  drawBoxes(300,340,325,"Log In")
  drawBoxes(625,665,25,"END")
  text = titleFont.render("Destination Impossible", 1, YELLOW)  #displaying title
  screen.blit(text,(185,25,25,10)) #blitting title
  if button == 1: #if the user is pressing down
     #checking the mouse coordinates of the user when mouse is down
    if 300<mx<450 and 100<my<150:  #if the first button is being pressed - PLAY
      #reset variables
      ewasteX = 750 #reset position of e waste
      carX = 750 #reset car position
      healthX = 750 #reset health powerup position
      greenObstacleX = 750 #reset green obstacle position
      fireX = 700 #reset fire position
      button = 0  #set button to 0 because the user is no longer pressing a button
      kilometers = 0 #set kilometers to 0 because the user is going to play a new game and we are resetting everything
      currentState = GAMEPAGE #set the state to game page because the user has pressed play
      lives = 5 #reset the lives
      score = 0 #reset the score to 0
      color = GREEN #reset the color of the health bar to green because it is full
      bulletX = count + 50 #reset x position of the users bullet
      bulletY = countY + 70 #reset y position of the users bullet
      for i in range(len(boolList)): #going through boolList
        boolList[i] = False #setting all booleans to false
      playedBool = False #setting playedBool to false because the user has not finised playing the game they are just starting it
      KEY_SPACE = False
      hit = False #set to hit to false because the user cant be hit when they start the game
      playerMode = "safe" #set playerMode to safe because the player is safe when the game starts, they should not be hitting anything
      bulletHit = False #set bulletHit to false because a bullet is not hitting e waste
      playedOnce = 0 #set playedOnce back to 0 because we want playedBool to be able to be true if the player finishes the game again
      bulletsList = [] #empty the list of bullets
      ewasteDestroyed = 0 #resetting ewasteDestroyed
      menuTime = pygame.time.get_ticks() #this variable menuTime is very important. We set it to the current time right before the game so that we can subtract menuTime from the system run time. This is so that we can start the game at 0 seconds. If we didnt do this then the time spent on the menu and in other states would part as part of the game time as well because pygame.time.get_ticks gets the system run time ever since the player presses run
    elif 300<mx<450 and 175<my<225: #if the user is pressing the instructions button go to the instructions page
      button = 0
      currentState = INSTRUCTIONS
    elif 300<mx<450 and 250<my<300: #leaderboard button
      button = 0
      currentState = LEADERBOARD
    elif 300<mx<450 and 325<my<375: #login button
      #reset some variables
      button = 0
      textDisplayList = []
      xPos_textInput = 120
      currentState = LOGIN
      drawScreenOnce = True #setting drawScreenOnce to true because we are opening the login page for the first time and we want the white background to be drawn once
    elif 625<mx<775 and 25<my<75: #end button
      button = 0
      currentState = QUITCOMMAND 
  drawText(myFont,"Name: %s"%name,100,400,BLACK) #displaying the players name in the bottom left corner of the screen. By default their name is "Anonymous"
  return currentState 

def read(dataFile): #reading the file
  global fileInformation 
  file = open(dataFile, "r") #Opening the data file as a read only, the variable dataFile is a local variable which we will replace with the file name when we call the function.
  fileInformation = [] #creating a list to store data in
  while True:
      text = file.readline() #reads each line of data file
      text = text.rstrip("\n") #removes the backslash n
      if text=="": #if there is nothing on the line, than that means that there is no more data to be read, so break out of the loop. We are done reading the file
          break
      values = text.split(",") #make a list with the different fields of the records as seperate elements, by using the split method, which splits the data fields through the commas that are seperating them
      for i in range(len(values)):
        fileInformation.append(values[i]) #go through all of the individual fields of our data and append them to our list
  file.close() #closing the file; 
  
def formattedList(): #creating our formatted multidimensional lsit
  global recordsList
  recordsList = [] #the multidimensional list is called recordsList
  count = 4 #we have a variable count which is 4 because we have 4 fields
  for i in range(len(fileInformation)//4): #going through the length of the unformattedList//4
    record = [] #1  #setting an empty list for record which represents the information in one record
    for j in range(count-4,count): #going through 4 elements in the unformatted list and putting them into one record
      record.append(fileInformation[j]) #appending that record to the variable record
    count+=4 #increasing count so that we can go through the next 4
    recordsList.append(record) #adding that record to our multi dimensional list
  return recordsList #returning our final recordsList, which a list containing all the records

def drawTable():#function to draw the table  
  #NOTE: Alot of the databse/leaderboard code and commenting is taken from my database project, but some parts were slightly altered. For example, the feature of sorting the leaderboard list was not present in the original version. I added it in this version.
  global textDisplayVar,recordsList
  pygame.draw.rect(screen, WHITE, (0,0,800,500)) #draw a white background that takes up the whole screen
  xPosText = 20 #this is the xPosition of the text
  yPosText = 50#this is the y position of the text
  #draw the titles
  drawText(myFont,"Name              Ewaste Destroyed       Distance     Score",20,10,BLACK) 
  orderedList = [] #ordered list is a list that will contain all of the scores 
  for i in range(len(recordsList)):  #going through recordsList
    orderedList.append(float(recordsList[i][3])) #adding the score in every record to orderedList. We have to make it a float because in recordsList it is a string and we need to sort orderedList, so we need numbers not strings.
  orderedList.sort() #sorting orderedList
  orderedList.reverse() #reversing orderedList so that it goes in descending order because we want it from highest to lowest score
  orderedRecordsList = [] #orderedRecordsList is a new list 
  for i in range(len(orderedList)): #going through orderedList
    for j in range(len(recordsList)): #going through recordsList
      if float(recordsList[j][3]) == orderedList[i]: #if the score value for the record is equal to the score value in orderedList 
        orderedRecordsList.append(recordsList[j]) #append the whole record to orderedRecordsList
        
        recordsList.append(recordsList[j]) #apped the record to the back now so that if two records have the same score value we dont keep on repeating the same record (because the other fields may be different)
        del recordsList[j] #delete it from the front of the list
        break
  #what the code above is doing is finding all the records which match with the scores from highest to lowest so now we have our leaderboard
  recordsList = orderedRecordsList #setting recordsList to orderedRecordsList, because orderedRecordsList is a new sorted recordsList so we want to apply those changes to recordsList
  for i in range(len(recordsList)): #going through the first ten records in recordsList because 
    if i>=10: #if we are at the 11th record or further then break because the leaderboard only needs to show the top 10
      del recordsList[10:] #we have no need for the users data, it will just take up space so we delete it from recordsList. the only data we want to keep is the top 10 scores because that is what we display on the leaderboard.
      break
      
    drawText(myFont,recordsList[i][0],xPosText,yPosText,BLACK) #draw the first field of the first record
    xPosText+=150 #increase xPosText by 50 so we can have enough spacing between the first field and the second field
    drawText(myFont,recordsList[i][1],xPosText,yPosText,BLACK)
    xPosText+=220
    #the amount we increase xPosText by depends on the maximum character length of each field
    drawText(myFont,recordsList[i][2],xPosText,yPosText,BLACK)
    xPosText+=115
    drawText(myFont,recordsList[i][3],xPosText,yPosText,BLACK)

    yPosText+=40 #move on to the next line (new record)
    xPosText = 20 #reset the x value

def displayInfo():
  global fileInformation
  global recordsList
  read("info.dat") #reading the data
  recordsList = formattedList() #putting file information into the variable recordsList

def gamePage(currentState,mx,my):
  global hitTime,count,countY,stopwatch2,color,lives,KEY_SPACE,backgroundX2,backgroundX,background
  global ewasteX,ewasteY,ewasteVelocity,hit,bullletX,bulletY,carX,carY,playerMode,healthX,healthY,fireYList
  global fireY,fireX,bulletHit,greenObstacleX,greenObstacleY,kilometers,menuTime,boolList,playedOnce
  global ewasteDestroyed,bulletsList
  if kilometers >= 4: #if the user has travelled more than 4 kilometers then they have won
    currentState = VICTORY #go to the victory pgae
    playedOnce = 0 #set playedOnce back to 0 so that playedBool can be true because the user has just finished playing the game
  pygame.draw.rect(screen,WHITE,(0,0,1000,1000)) #draw the background
  #I am using two blocks of road to give the illusion that there is one big road constantly moving to the left
  drawScene(background,backgroundX,150) #draw the first block of road
  drawScene(background,backgroundX2,150) #draw the second block of road
  if backgroundX <(0 - (background.get_width())): #resetting the position of the road back to the right side of the screen if it goes past the left side
    backgroundX  =  (backgroundX2+ background.get_width()) -25
  elif backgroundX2<(0 - (background.get_width())): #doing the same thing except for the second chunk of road
    backgroundX2 = (backgroundX+background.get_width()) - 25
  backgroundX-=10 #changing the x value of the road so that it is moving
  backgroundX2-=10 #changing the x value of the second road so that it is moving
  if KEY_SPACE == True or bulletsList!=[]: #if the space key is being pressed or if the list of bullets is not empty. We do this because if the space key is being pressed the user is releasing a bullet and if the list is not empty then that means that there are bullets and we need to constantly be updating their position through the bullets function
    bullets()
  count, countY = movingRestrictions() #establishing the x and y coordnates of the player
  #getting objects to appear at certain time intervals
  if int((pygame.time.get_ticks() - menuTime)/1000)%6==0 and ewasteX == 750: #if the total game run time - the time spent on the menu (to make the time when the gme starts 0) is divisible by 6 and the ewaste is already not in motion then put the ewaste into action. In otherwords make the e waste appear every 6 seconds. The reason I am dividng by 1000 is to convert it from milliseconds to seconds and I make it an integer because the division results in a decimal number
    ewasteY = random.choice([175,270,365]) #pick a random lane for the y position of the e waste
    ewasteX = 750 #set the e waste position to be at the right most point on the screen
    boolList[0] = True #the 0th eleent in boolList represents the ewaste boolean so set it to true because the ewaste is in action
    ewasteVelocity = 1 #set the velocity to 1
  if int((pygame.time.get_ticks()-menuTime)/1000)%20==0 and healthX == 750:
    healthY = random.choice([175,270,365]) #set the health y position to a random lane
    healthX = 750 #set the x position of the health powerup
    boolList[1] = True #boolList[1] is the health boolean so set it to true because the health power up is in action
  if boolList[1] == True: #if the health power up is in action
    healthX -=5 #move the health power up to the left
    pygame.draw.rect(screen,BLUE,(healthX,healthY,50,30)) #draw the health power up
    if healthX < 0:  #if it is off screen
      boolList[1] = False #set the bolean to false because it is no logner in action
      healthX = 750 #reset the x position
  carX-=5 #change the x position of the car
  if carX < -200: #reset car position if off screen
    carX = 850
    carY = random.choice([155,250,345]) #pick random lane
  displayCar = (carX,carY,car.get_width(),car.get_height()) #display the car
  screen.blit(car,displayCar)
  if boolList[0] == True: #if the ewaste is true
    pygame.draw.rect(screen,RED,(ewasteX,ewasteY,100,50)) #draw the ewaste
    drawScene(ewaste,ewasteX,ewasteY)
    #change the velocity of the e waste depending on how far into the game the user is
    if int((pygame.time.get_ticks() - menuTime)/1000) > 60:
      ewasteVelocity*=1.05
    elif int((pygame.time.get_ticks()-menuTime)/1000) > 30 and int((pygame.time.get_ticks()-menuTime)/1000) <=60:
      ewasteVelocity*=1.04
    else:
      ewasteVelocity*=1.03
    ewasteX -=ewasteVelocity #change the x position by ewasteVelocity
    if ewasteX<-50 or bulletHit == True: #if the ewaste is off screen or it has been hit by a bullet
      #reset the variables
      ewasteVelocity = 1
      boolList[0] = False
      bulletHit = False
      ewasteX = 750
  if hit == True: #if the user has been hit
      lives-=1 #decrease lives
      color,currentState = livesCheck(currentState) #change the color of the health bar accordingly
      hit = False #reset variable hit
  if playerMode == "safe": #if the user is safe (not hit)
    drawPlayer(character) #draw the player normally
    if (count+15<ewasteX + 50<count+165) and (ewasteY<countY+20<ewasteY+50 or ewasteY<countY+100<ewasteY+50 or ewasteY<countY + 70<ewasteY+50): #if the user is in the range of the e waste
      hit = True #set hit to true
      playerMode = "hit" #change player mode to hit because the user has been hit
      hitTime = 1 #set hitTime to 1. hitTime acts like a boolean, setting hitTime to 1 triggers it to inrement. It will increment to a certain value. During that period of it incrementing the user will be invincible because they have just been hit and they get some recovery time
    if count+15<fireX + 10<count+165 and ((countY+25<fireY + 5<countY+100) or (countY+25<fireY + 45<countY+100)): #if the user is in the range of the fire
      #recognize that user has been hit
      playerMode = "hit"
      hitTime = 1 
      hit = True
    #checking to see if the player is touching the car (note there is some leniancy in the hitbox for this. As long as the player is not touching the center of the car it will not count as a hit. This leniancy makes it a  bit easier so it is not too hard and it looks somewhat natural when the player is riding along with the car even when they are touching it slightly so I dont want that to count as a hit)
    if (count+15<(carX + car.get_width()/2)<count+165)  and (countY+20<(carY + car.get_height()/2)<countY+100):
      playerMode = "hit"
      hitTime = 1
      hit = True
    #checking if the player is touching the green obstacle (x and y are the x and y coordinates of the green obstacle)
    if ((count+15<greenObstacleX<count+165) or (count+15<greenObstacleX+100<count+165)) and ((countY+25<greenObstacleY<countY+100) or (countY+25<greenObstacleY+20<countY+100)):
      #reset the variables
      playerMode = "hit"
      hitTime = 1
      hit = True
      boolList[4] = False #boolList[4] represents the boolean for the green obstacle
      greenObstacleX = 750 
    # pygame.draw.rect(screen,BLACK,(count + 15,countY + 25,150,75)) hitbox
  else:
    drawPlayer(character_hit) #if the player is hit than draw the ghost like version of the player instead of the normal one
  if (count + 15<healthX<count+165 or count + 15<healthX + 50<count + 165) and (countY+25<healthY<countY+100 or countY+25<healthY+30<countY+100): #if the player is in the range of the health powerup
    #reset variables
    boolList[1] = False
    healthX = 750
    lives = 5 #set lives to 5 because health powerup revives lives
    color = GREEN #set color to green because a full health bar is green
  # pygame.draw.rect(screen,BLACK,(count + 15,countY + 25,150,75)) hitbox
 
  if hitTime>0: #if hitTime is greater than 0. Hit time is set to 1 when the user is hit and so hitTime will start incrementing
    hitTime+=1 #increment hit time by 1
    if hitTime>100: #if hit time is greater than 100
      hitTime = 0 #reset hitTime
      playerMode = "safe" #put playerMode back to safe because the user has already had a few seconds of invincibility 
  #health bar
  pygame.draw.rect(screen,BLACK,(550,30,180,20),5) #drawing outline
  pygame.draw.rect(screen,color,(552,32,175*(lives/5),15)) #drawing the inside colored part depending on how many lives the player has
  
  if int((pygame.time.get_ticks() - menuTime)/1000) > 30: #if over 30 seconds has passed
    if int((pygame.time.get_ticks() - menuTime)/1000)%20==0: #if the time is divisible by 20 (every 20 seconds)
      boolList[2] = True #set the helicopter boolean to true (the helicopter is shooting the fire) - helicopter boolean is represented by boolList[2]
    if boolList[2] == True: #if the helicopter bool is true
        stopwatch2+=1   #increase the variable stopwatch2 by 1; stopwatch2 is used to count how long the helicopter is visible for                                          
        lane = checkLane() #check the lane that the user is in and store it in the variable "lane"
        drawScene(helicopter,600,0) #draw the helicopter
        if stopwatch2>400: #if stopwatch2 is greater than 400
          #reset variables - the helicopter is now gone and since the helicopter shoots the fire the fire is also gone (fire boolean is represented by boolList[3])
          boolList[2] = False
          boolList[3] = False
          fireX = 700
          stopwatch2 = 0
        if boolList[3] == False: #checking to see if the fire boolean is false
          if int((pygame.time.get_ticks() - menuTime)/1000)%3: #if the helicopter bool is true (from the previous larger if statement) and the time is divisible by 3 (every 3 seconds)
            fireY = fireYList[lane] #set fireY to a y position depending on the lane. If lane is 0, then it will find the 0th index of the lane list which is the y position of the first lane
            boolList[3] = True #set the fire boolean to true because the fire should now appear
        if boolList[3] == True: #if the fire bool is true
          drawScene(fire,fireX,fireY) #draw the fire
          fireX-=7 #decrease the x position of the fire by 7
          if fireX<0: #if the fire is off screen 
            #reset the variables
            boolList[3] = False
            fireX = 700

  if int((pygame.time.get_ticks() - menuTime)/1000)>60: #if the time is greater than 60 seconds
    if int((pygame.time.get_ticks()-menuTime)/1000)%5 == 0: #if the time is divisible by 5
      boolList[4] = True #set the green obstacle boolean (represented by boolList[4]) to true
  if boolList[4] == True: #if boolList[4] is true then call the greenObstacle function. The greenObstacle function is for the green obstacle.
    greenObstacle()

  text = myFont.render("Ewaste Destroyed:%i"%ewasteDestroyed,1,(255,0,0)) #display the amount of e waste that the player has destroyed
  screen.blit(text,(50,25,25,10))
  kilometers = (pygame.time.get_ticks() - menuTime)/35714.2857143 #the amount of kilometers is determined by how long the game has been running for. 
  distance = myFont.render("Distance:%f km"%(kilometers),1,(255,0,0))  #display the distance that the player has travelled
  screen.blit(distance,(50,50,25,10))
  pygame.draw.circle(screen,RED,((kilometers/4)*200 + 50,100),10) #draw the circle that will change its position depending on how far the player has travelled
  pygame.draw.line(screen,BLACK,(50,100), (250,100)) #draw the line on which the circle moves along
  return currentState

def write(dataFile): #writing our final formatted list back to the file
  global recordsList
  file = open(dataFile, "w") #opening the file once again except as a write
  count = 0 #creating a variable
  for i in range(len(recordsList)): #going through each record in the table
    for j in range(len(recordsList[i])): #going through each field in each record
      if j > 0: #if the field number is any field besides the first than add a comma, becasue we want a comma before every field, except for the first one
        file.write(",") #writing a comma to the data file so that we have something that we can identify in order to split our information into individuals fields when reading the data
      file.write((recordsList[i])[j]) #writing each individual field to the file with the raw data until we have finished writing one record
    file.write("\n") #adding a back slash so that we move to a new line and start on the second record
  file.close() #closing the file, we are done writing

def drawPlayer(picture): #this function is used to draw the player
  global count
  global countY
  if playerMode == "safe": #if the player is safe
    pose = (count,countY,picture.get_width(),picture.get_height()) #draw the player at its x and y position
  else:
    pose = (count + 12,countY + 14,picture.get_width(),picture.get_height()) #otherwise the player has been hit so draw the player in invicible mode at its x and y position (which are altered slightly because the invincible image is positioned a bit differently)
  screen.blit(picture,pose) #display the character to the screen
def drawScene(picture,x,y): #this function is used to display images
  displayPicture = (x,y,picture.get_width(),picture.get_height())
  screen.blit(picture,displayPicture)

#loading all of the images used using the loadImage function 
ewaste = pygame.image.load("ewaste.png").convert_alpha()
ewaste = pygame.transform.scale(ewaste,(ewaste.get_width()*(100/ewaste.get_width()),ewaste.get_height()*(50/ewaste.get_height())))
trophy = loadImage("trophy.png",0.5,0.5)
background = loadImage("background.png",1.5,1.5)
character = loadImage("character.png",0.,1)
character_hit = loadImage("character_hit.png",0.57,0.57)
character = loadImage("character.png",0.3,0.3)
car = loadImage("car.png",0.1,0.1)
city = loadImage("city.png",2,1)
helicopter = loadImage("helicopter.png",1,1)
fire = loadImage("fire.png",0.2,0.2)
carX = 850
carY = random.choice([155,250,345])

#calling displayInfo to read the data and set up recordsList
displayInfo() 
running  = True 
currentState = INFOMENU #start the game at the menu
mx = my = button = 0 #initilaizing mouse position and button as 0
while running: #this loop will constantly run and redirect the program to different states
  KEY_BACKSPACE = False #set key backspace to false because it is generally false unless is it sp||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||l  y pressed`````
  button = 0 #setting button to 0 for the same reason as the line above (it was glitching if I didnt set it to 0 in this loop, so Mr Van Rooyen proposed this solution)
  for evnt in pygame.event.get(): #going through the different user inputs
    if evnt.type == pygame.QUIT:
      running = False
    if evnt.type == pygame.MOUSEBUTTONDOWN: #if the user presses than set button to 1 and get the mouse position
      button = 1
      mx, my = evnt.pos 
    if evnt.type == pygame.MOUSEMOTION: #get the position of the users mouse because that corresponds to the players position in the game. Button is 0 because the user is not pressing they are just moving their mouse.
      mx, my = evnt.pos
      button = 0
    if evnt.type == pygame.KEYDOWN: #if the user is pressing down
      if evnt.key == pygame.K_SPACE: #if the user is pressing space
        KEY_SPACE = True #set KEY_SPACE to true
      if evnt.key == pygame.K_BACKSPACE:
        KEY_BACKSPACE = True
      if evnt.key == pygame.K_COMMA: #again, I am setting a variable for comma because I want to make sure that the user does not enter commas. If they enter commas then it could mess up the database/leaderboard feature, because the values in the file are seperated by commas
        KEY_COMMA = True
      if textAllowed == True:  #if the user is allowed to press text
        if evnt.key == pygame.K_RETURN: #if the enter/return key is pressed
          enter = 1 #set enter to 1, because that signifies that enter has been pressed
        if xPos_textInput<(120 + (15*maximum)): #if the text is less than a certain amount (depending on maximum) than it will draw the character. Otherwise, it meanst that the character length has been exceeded so the program should not draw any text
          KEY_PRESSED = True #the key has been pressed and it is valid
      if currentState == LOGIN: #if the state is login constantly check for keys
        keyInput()
    elif evnt.type == pygame.KEYUP: #if the key is up
      KEY_PRESSED = False #that means that no keys are being pressed

      if evnt.key == pygame.K_BACKSPACE: #if the key is backspace 
        KEY_BACKSPACE = False #set it to false because they key is now up
      if evnt.key == pygame.K_COMMA:
        KEY_COMMA = False

  #checking the value of currentState and redirecting to the appripriate screens
  if currentState == LOSEPAGE:
    currentState = losePage(currentState,mx,my)
  elif currentState == GAMEPAGE:
    currentState = gamePage(currentState,mx,my)
  elif currentState == INFOMENU:
    currentState = infoMenu(currentState,mx,my)
  elif currentState == VICTORY:
    currentState = victory(currentState,mx,my)
  elif currentState == INSTRUCTIONS:
    currentState = instructions(currentState,mx,my)
  elif currentState == QUITCOMMAND:
    currentState = quitCommand(currentState,mx,my)
  elif currentState == LEADERBOARD:
    currentState = leaderboard(currentState,mx,my)
  elif currentState == LOGIN:
    currentState = loginPage(currentState,mx,my)
  if currentState!=GAMEPAGE and currentState!=INFOMENU: #if the state is not the gamepage and is not the information menu then the back button should be drawn (you cant go back during the game or if you are on the menu)
    drawBoxes(600,650,20,"BACK") #draw the back button
    if button == 1: #if the button is prssed 
      if 600<=mx<=750 and 20<=my<=70: #if it is in the range of the back button
        currentState = INFOMENU #go back to the menu
        button = 0 #reset button
  if xPos_textInput>(120 + (15*maximum)): #if the position of the text is at the right most point of the textbox then the user can no longer add text
    textAllowed = False
  
  myClock.tick(60)  #run the program at 60 frames per second
  pygame.display.flip() #display everything to the screen
pygame.quit()


