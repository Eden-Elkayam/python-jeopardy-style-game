#"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department.”


questions= [
           ["Hogwarts Houses", 100, "Which Hogwarts house values intelligence and wit?", "*Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin"],
           ["Hogwarts Houses", 100, "Luna Lovegood is the member of which house?", "Gryffindor", "Slytherin", "*Ravenclaw", "Hufflepuff"],
           ["Hogwarts Houses", 200, "What is the common room entrance to Griffindor House guarded by?", "*a portrait of The Fat Lady", "The Grey Lady", "The Bloody Baron", "Nearly Headed Nick"],
           ["Hogwarts Houses", 200, "Who is the ghost of Ravenclaw house?", "Nearly Headless Nick", "*The Grey Lady", "The Fat Friar", "The Bloody Baron"],
           ["Hogwarts Houses", 300, "In which house does the Sorting Hat almost place Harry?", "*Slytherin", "Ravenclaw", "Hufflepuff", "Gryffindor"],
           ["Hogwarts Houses", 300, "Which house ghost is known for being the only one who can pass through walls?", "* Nearly Headless Nick", "The Grey Lady", "The Fat Friar", "The Bloody Baron"],
           ["Hogwarts Houses", 400, "The emblematic animal of Gryffindor House is the:", "*Lion", "Eagle", "Snake", "Badger"],
           ["Hogwarts Houses", 400, "The Hufflepuff common room is accessed through a secret entrance near the", "*Kitchen", "Great Hall", "Owlery", "Whomping Willow"],
           ["Hogwarts Houses", 500, "Which professor becomes the head of Gryffindor house after Professor McGonagall?", "*Neville Longbottom", "Professor Flitwick", "Professor Slughorn", "Professor Sprout"],
           ["Hogwarts Houses", 500, "The Fat Friar used to be a member of which Hogwarts house", "*Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor"],

           ["Magical Creatures", 100, "What is the name of Hagrid's three-headed dog?", "Buckbeak", "*Fluffy", "Fang", "*Norbert"],
           ["Magical Creatures", 100, "What is the main habitat of The Blast-Ended Skrewt?", "*Forbidden Forest", "Hagrid's Hut", "Black Lake", "Quidditch Pitch"],
           ["Magical Creatures", 200, "Which magical creature transform into a person's worst fear?", "Hippogriff", "Chimera", "*Boggart", "Kelpie"],
           ["Magical Creatures", 200, "Which magical creature is known to guard banks, including Gringotts?", "Niffler", "*Goblins", "Acromantula", "Occamy"],
           ["Magical Creatures", 300, "What is the name of the magical creature that is a mix of lion and eagle?", "*Hippogriff", "Thestral", "Bowtruckle", "Chimera"],
           ["Magical Creatures", 300, "Which magical creature is visible only to those who have witnessed death?", "*Thestral", "Hippogriff", "Blast-Ended Skrewt", "Bowtruckle"],
           ["Magical Creatures", 400, "Thestral tail hair is a core ingredient in the making of which magical object?", "Invisibility Cloak", "Time-Turner", "*Elder Wand", "Deluminator"],
           ["Magical Creatures", 400, "What is the name of the small, mischievous creature that loves shiny objects?", "Badger", "*Niffler", "Thestral", "Blast-Ended Skrewt"],
           ["Magical Creatures", 500, "How do Kelpies typically disguise themselves to attract unwary victims?", "*Horse", "Mirror", "Well", "Cat"],
           ["Magical Creatures", 500, "What is the key characteristic of a Bowtruckle?", "Winged", "*Twig-like body", "Fire-breathing", "Aquatic"],
           
           
    
           ["At the Dursleys", 100, "What is the name of Harry Potter's aunt at the Dursleys?", "*Petunia Dursley", "Marge Dursley", "Dudley Dursley", "Vernon Dursley"],
           ["At the Dursleys", 100, "What is the address of the Dursley family?", "12 Grimmauld Place", "Spinner's End", "*Number 4, Privet Drive", "The Burrow"],
           ["At the Dursleys", 200, "What is the name of Dudley Dursley's gang of friends?", "The Marauders", "*The Dudders", "The Inquisitors", "The Knights of Walpurgis"],
           ["At the Dursleys", 200, "What does Harry receive from Mrs. Weasley during his stay at the Dursleys in the first book?", "A broomstick", "*A hand-knit sweater", "A magical potion", "A howler"],
           ["At the Dursleys", 300, "What is the name of the neighbor who spies on the Dursleys and reports to Mrs. Figg?", "Mrs. Norris", "Mr. Filch", "*Mrs. Figg", "Mr. Diggory"], 
           ["At the Dursleys", 300, "What does Harry do to Aunt Marge when she insults his parents?", "*Inflates her like a balloon", "Turns her into a frog", "Casts a spell to silence her", "Leaves the room calmly"],   
           ["At the Dursleys", 400, "What birthday present does Harry receive from the Dursleys in the first book?", "A dusty old book", "A small bag of galleons", "A new set of clothes", "*a pair of old socks"],
           ["At the Dursleys", 400, "Where did Harry first hear about Hogwarts?", "*On a small island", "In the cupboard under the stairs ", "In the backyard", "In the car on the way to the zoo"],
           ["At the Dursleys", 500, "What does Uncle Vernon do for a living?", "*Director of a  drilling firm", "Insurance Adjuster", "Banker", "Car Salesman"],
           ["At the Dursleys", 500, "How did Aunt Petunia know what Dementors were?", "She overheard James Potter", "*She overheard Severus Snape", "Harry told her about them", "Dumbledore wrote about them in his letter"],
           

           ["You-Know-Who", 100, "What is the real name of Lord Voldemort?", "*Tom Riddle", "Salazar Slytherin", "Albus Dumbledore", "Gellert Grindelwald"],
           ["You-Know-Who", 100, "What is the name of Lord Voldemort's loyal snake?", "Basilisk", "*Nagini", "Niffler", "Fawkes"],
           ["You-Know-Who", 200, "Which dark wizard was considered a close ally of Lord Voldemort during the First Wizarding War?", "Bellatrix Lestrange", "*Lucius Malfoy", "Severus Snape", "Peter Pettigrew"],
           ["You-Know-Who", 200, "What is the name of the curse that Voldemort casts on Harry in the Forbidden Forest?", "Cruciatus Curse", "*Avada Kedavra", "Imperius Curse", "Incarcerous Spell"],
           ["You-Know-Who", 300, "What family does Lord Voldemort belong to by blood?", "The Potters", "The Malfoys", "*The Gaunts", "The Blacks"],
           ["You-Know-Who", 300, "what dark secret about Voldemort's family is revealed in the Pensieve memories?", "*His father was a Muggle", "His mother was a muggle", "He was adopted", "He killed his own father"],
           ["You-Know-Who", 400, "Which of the following objects was not used as a Horcrux by Voldemort?", "*The Resurrection Stone", "Tom Riddle’s Diary", "Salazar Slytherin’s Locket", "Helga Hufflepuff’s Cup"],    
           ["You-Know-Who", 400, "Who provides information to Voldemort about the creation of Horcruxes?", "Albus Dumbledore", "The Diadem of Ravenclaw", "Nagini", "*The Elder Wand"],
           ["You-Know-Who", 500, "What magical object did Voldemort unknowingly turn into a Horcrux during his time at Hogwarts?", "The Resurrection Stone", "The Diadem of Ravenclaw", "Hufflepuff's Cup", "*Tom Riddle's Diary"],
           ["You-Know-Who", 500, "What is the name of the cave where Voldemort hides one of his Horcruxes?", "Cavern of Shadows", "*Crystal Cave", "Cave of the Inferi", "Cave of Desolation"],
           
           ["Spells and Potions", 100, "What does the spell 'Lumos' do?", "*Produces light from the caster's wand", "Creates a protective shield", "Transforms objects into birds", "Invisibility"],  
           ["Spells and Potions", 100, "What spell is used to repel Dementors?", "Accio", "*Expecto Patronum", "Expelliarmus", "Stupefy"],
           ["Spells and Potions", 200, "Which spell is used to summon objects to the caster?", "*Accio", "Stupefy", "Obliviate", "Protego"],
           ["Spells and Potions", 200, "Which potion causes the drinker to become lucky for a period of time?", "Amortentia", "Polyjuice Potion", "*Felix Felicis", "Wolfsbane Potion"],
           ["Spells and Potions", 300, "What spell is used to disarm an opponent?", "*Expelliarmus", "Stupefy", "Alohomora", "Lumos"],
           ["Spells and Potions", 300, "What does the dark spell Harry learns from the Half-Blood Prince's potion book do?", "Causes the target to levitate uncontrollably", "Summons a snake to attack the target", "*Inflicts lacerations on the target's body", "Induces a temporary death-like state in the target"],
           ["Spells and Potions", 400, "What spell is used to unlock doors and windows?", "Expelliarmus", "Stupefy", "*Alohomora", "Lumos"],
           ["Spells and Potions", 400, "What is the spell to make objects levitate?", "*Wingardium Leviosa", "Levioso", "Accio", "Alohomora"],
           ["Spells and Potions", 500, "What potion is used to heal minor injuries?", "Essence of Dittany", "Pepperup Potion", "*Wiggenweld Potion", "Amortentia"],
           ["Spells and Potions", 500, "What potion is used to neutralize the effects of the Draught of Living Death?", "Revival Draught", "Elixir of Wakefulness", "Veritaserum", "*Wiggenweld Potion"]
           ]
                  
import random
import Draw
import time

# This function takes the catagory name as a parameter and returns a list of 5 questions from
# that category, one for each level, in a random order. 
def get5Questions(category):
    answer=[]
    
    # This list will keep track of the levels of the questions already appended to 'answer'
    levels=[]
    while len(answer)<5:
        randomQ=random.choice(questions)
        
        # Making sure the random question that was chosen is of the desired catagory and that it
        # is not from the same level of another question already in the list before appending it 
        # to the 'answer' list.
        if randomQ[0]==category and randomQ[1] not in levels:
            answer+=[randomQ]
            
            # adding the level of the appended question before looping again so we only get 
            # one question of each level in 'answer'
            levels+=[randomQ[1]]
    return answer

# This function takes the empty grid, the category, and the number of column you want that category to go into. 
def fillColumn(grid, n, category):
    
    # Empty list that would be the new list of the grid once full
    row=[]
    
    # a New list containing 5 questions of the chosen category, but not in order
    unorganized=get5Questions(category)
    
    # The outer loop indicats the level of the question that will be appended to the new list
    for i in range(1,(len(unorganized)+1)):
        
        # In each of the outer loops, loop through the list to find a question in the appropriate level 
        for j in range(0,(len(unorganized))):
            
            # Finding the desired level by multiplying i by 100 
            if unorganized[j][1]==i*100:
                row+=[unorganized[j]]
                
    # Replace the appopriate row with the new row 
    grid[n]=row
    
    return grid

# This function returns the grid list, full of questions in all the categories
def setupBoard():
    
    # Create an empty grid that the 'fillColumn' function uses then to replace each row
    grid=[[0 for i in range(6)] for j in range(5)]
    fillColumn(grid, 0, "Hogwarts Houses")
    fillColumn(grid, 1, "Magical Creatures")
    fillColumn(grid, 2, "At the Dursleys")
    fillColumn(grid, 3, "You-Know-Who")
    fillColumn(grid, 4, "Spells and Potions")
    return grid

# This function draws the game board so it's ready to play
def drawBoard(grid,height,width,score, background):
    
    # the picture that is used as background throughout the entire game
    Draw.picture(background, 0, 0)
    
    #Insert each image in the appripriate location
    Draw.picture("Hogwarts Houses.gif",0, 0)
    Draw.picture("Magical Creatures.gif", (width/5*1), 0)
    Draw.picture("At the Dursleys.gif", (width/5*2), 0)
    Draw.picture("You-Know-Who.gif", (width/5*3), 0)
    Draw.picture("Spells and Potions.gif", (width/5*4), 0)
    
    # Set the desired font charachteristics
    Draw.setFontSize(24)
    Draw.setColor(Draw.BLACK)
    Draw.setFontFamily("Times New Roman")

    # For each category and question, draw the worth of the question on the canvas
    for category in range(len(grid)):
        # for each level in the topic
        for level in range(len(grid[category])):
            # find the x and y coordinates for each cell
            levelX = width/5*category + width/12
            levelY = height/6*(level+1) + height/14
            
            # Parameter for the questions' worth
            worth=grid[category][level][1]
            
            # if the worth is 0, it means the question was anwsered incorrectely.
            if worth==0:
                
                # importing and placing an image of an X mark in the middle of the cell
                Draw.picture("Wrong.gif", levelX-15, levelY-25)
            
            # worth of 1 means the question was answered correctely 
            elif worth==1:
                
                # Importing and placing an image of a check mark 
                Draw.picture("Right.gif", levelX-15, levelY-25)
            
            # The other questions were not answered yet so their worth should be drawed.
            else:
                Draw.string("$" + str(worth), levelX, levelY)
    
    # Draw the lines of the grid using the size of the canvas
    for i in range(1,6):
        Draw.line((width/5)*i, 0, (width/5)*i, height)
        Draw.line(0,(height/6)*i, width, (height/6)*i)
        
    # draw the score at the top left of the screen
    Draw.string("Score: $" +str(score), 0,0)
    
    Draw.show()

             
# Function that presents the chosen quiestion and returns True if the user
# clicked the right answer, returns False if the user clicked a wrong answer. 
def askQuestion(grid,width,height,question,score,background):
    Draw.clear()
    # Add background
    Draw.picture(background,0,0)
    
    # set a font and size for the text
    Draw.setColor(Draw.BLACK)
    Draw.setFontFamily("Times New Roman")
    Draw.setFontSize(30) 
    
    # draw the score
    Draw.string("Score: $" +str(score), 0,0)
    
    # draw the question at the top box
    Draw.string(question[2], (width/2)-(len(question[2])*6), height/10)
    
    # shuffle the answers: create a temporary parameter for the slice with the answers
    temp=question[3:]
    # shuffle the answers so they come in a random order
    random.shuffle(temp)
    # insert the answers back in the list 
    question[3:]=temp
    
    #loop through the answers to draw the answers on the canvas, along with 
    # the outline of the grid
    for i in range(1,5):
        
        # begin by drawing all the lines
        Draw.line(0,(height/5)*i, width, (height/5)*i)
        
        # go over the answers by their new order
        currentAns=question[2+i]
        
        # if there is an * in the anwer, it needs to be drawed without it 
        if "*" in currentAns:
            Draw.string(currentAns[1:], width/2-(len(currentAns[1:])*6), height/5*i+height/10)
            
       # for the other question, sraw normally
        else:
            Draw.string(currentAns, width/2-(len(currentAns)*6), height/5*i+height/10)
        Draw.show()  
        
    # waiting for users response  
    while True:
        if Draw.mousePressed():
            
            # get the y coordinate
            y = Draw.mouseY()
            clickedCell= int(y//(height/5))
            
            # clickedCell will be 0 if the user clicks on the question
            if clickedCell>0:
                
                # convert the cell into the chosen question
                chosenAns= question[2+clickedCell]
                ans= ("*" in chosenAns)
                if ans:
                    
                    # indicate the answer is correct before returning
                    Draw.setFontSize(200)
                    Draw.setColor(Draw.GREEN)
                    Draw.string("CORRECT!", width/2-450 ,height/2-100)
                    Draw.show()
                    time.sleep(0.3)
                else:
                    
                    # indicate the answer is incorrect before returning
                    Draw.setFontSize(200)
                    Draw.setColor(Draw.RED)
                    Draw.string("INCORRECT", width/2-550 ,height/2-100)
                    Draw.show()
                    time.sleep(1.5)                    
                Draw.clear()
                
                # return the answer. if ans is True, it means there was an "*" in the
                # answer, so it is correct. 
                return ans

# function returns the number of unanswered questions in the grid
def unansweredQuestions(grid):
    unanswered=0
    
    # loop through the grid looking for unanswered questions
    for category in range(len(grid)):
        for question in range(len(grid[category])):
            
            # if the question is unanswered, its worth will be bigger than 1. 
            if grid[category][question][1]>1:
                unanswered+=1
    return unanswered

# function that responsible for playing the game until the user looses or wins
def playGame(grid,height,width,background):
    
    score=0
    
    # as long as you have money and there are still unanswered questions in the grid
    while score >=0 and unansweredQuestions(grid)>0:
        
        # so the board is drawed faster (without this the board is drawed slowly)
        Draw.show()
        
        # invoke drawBoard to draw the board
        drawBoard(grid,height,width,score,background)  
        
        # wait for the user to click, if hey clicked, take the x and y coordinates of the click
        if Draw.mousePressed():
            y = Draw.mouseY()
            x = Draw.mouseX()
            
            # converting the click's y value to the level, which is the row on the board,
            #corresponding to worth in $. since the first row of the board presents the 
            # category, we need to substract 1
            level=int(y//(height/6)-1)
            
            # converting the click's x value to category, which is the column on the board,
            # corresponding to the chosen category.
            category=int(x//(width/5))
            
            # find the question corresponding to the clicking location. 
            question=grid[category][level]
            
            # if the level is more than 0 - the user clicked on a specific question rather than the headers row
            # and the worth of the question is more than 1 - the question was not invoked yet.
            if level>=0 and question[1]>1:
                
                # if the question was answered correctely
                if askQuestion(grid,width,height,question,score,background):
                    
                    # add the worth of the question to your score and change worth to 1
                    score+=int(question[1])
                    question[1]=1
                    
                # if question was answered incorrectley
                else:
                    
                    # substract the worth of the question from the score and zero the worth
                    score-=int(question[1])
                    question[1]=0
                    
    # if the score is negative it means the user lost
    if score<0:
        
        # clear the canvas, and draw the game over board
        Draw.clear()
        Draw.picture("Game Over.gif", 0,0)
        Draw.show()
    
    # If we've fallen out of the loop and the score isn't bellow 0, it means all of the 
    # questions were answered, so the user wins
    elif unansweredQuestions(grid)==0:
        
        # Clear the canvas and draw the winning board
        Draw.clear()
        Draw.picture("win.gif", 0, 0)
        
        # Set the font charachteristics for drawing the score
        Draw.setColor(Draw.BLACK)
        Draw.setFontSize(50)
        
        # the text that will be drawed on screen, in a variable so its length
        # could be found and used to locate the text in the middle of the screen
        scoreEnd="Your Score: %2d" % (score)
        Draw.string(scoreEnd, width/2-len(scoreEnd)*10, 400)
        Draw.show()    

def displayInstructions():
    #Draw.clear()
    Draw.picture("Instructions.gif",0,0)
    
    # add the picture for the start button
    Draw.picture("Start.gif", 930,580)
    
    # waiting for the user to click
    while True:
        
        # if hey clicked, take the x and y coordinates of the click
        if Draw.mousePressed():
            y = Draw.mouseY()
            x = Draw.mouseX()
            
            # if the user clicked on the 'start' button, exit the function.
            # the dimentions of the button is 340x79.
            if x>=827 and x<=(930+340) and y>=562 and y<=(580+79):
                return
                                  
def main():
    
    # set the size of the canvas for further reference
    width=1400
    height=750
    
    # import the picture for the background
    background= "Background.gif"
    
    # set up the grid itself
    grid = setupBoard()
    
    Draw.setCanvasSize(width,height) 
    
    # show the instructions page
    displayInstructions()
    
    # play the game 
    playGame(grid,height,width,background)
    
main()
