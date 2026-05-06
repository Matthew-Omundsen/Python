#Name: Matthew Omundsen
#Date: 11/15/24
#Program description: Great American Turtle Race

import turtle
import random

#Name: generateTurtles
#create a turtle for each color in the input list that is the color given and return a list of all those turtles
#input: a list with colors in it
#return value: a list with turtles in it

def generateTurtles(colors):
    turtles = []
    for x in colors:
        newTurtle = turtle.Turtle()
        newTurtle.shape('turtle')
        newTurtle.fillcolor(x)
        turtles.append(newTurtle)
    return turtles   


#Name: placeTurtles
#move all the turtles passed in the list to their start positions with the track seperation between each
#input: a list of turtles, the start line location, how far each should be seperated
#return value: no return	


def placeTurtles(turtles,start_loc,track_separation):
    for k in range(0,len(turtles)):
        turtles[k].penup()
        turtles[k].setposition(start_loc[0],start_loc[1]+k*track_separation)
        

#Name: startTurtles
#starts the race and moves each turtle one at a time until a winner reaches the finish line
#input: a list of turtles, the finish line location, a forward increment 
#return value: the color of the winning turtle

def startTurtles(turtles,finish_line,forward_incr):
    while True:
        for x in range(0,len(turtles)):
            turtles[x].forward(random.randint(1,6)*forward_incr)
            if turtles[x].xcor() >= finish_line:
                return x

#~~~~~~~~~~MAIN~~~~~~~~~~~


#Initialize the number of turtles
num_turtles = 10

#Set window size
turtle.setup(700,700)

#Get turtle window
window = turtle.Screen()

#Set window title
window.title('The Great American Turtle Race!')

#Initialize screen layout parameters
start_loc = (-240, -240)
finish_line = 240
track_separation = 60
forward_incr = 6

#Set turtle colors
colors = ['dark red', 'red','orange','yellow','chartreuse', 'green', 'turquoise', 'blue','violet', 'purple']

#Generate and initialize turtles
turtles = generateTurtles(colors)

#Place turtles at starting line
placeTurtles(turtles, start_loc, track_separation)

#Start turtles
winner = startTurtles(turtles, finish_line, forward_incr)

#Display winning turtle
print("The winner is the "+colors[winner]+" turtle!")

#Terminate program when close window
turtle.exitonclick()
