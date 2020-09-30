from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import *
from pylab import ginput as ginp
import numpy as np
import random
import time

#variables
COM_RANGE =100 # communication range of 100m
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = 0
com_lines =[]
line1 = [] # the first line
line2 = [] # the second line
line3 = [] # the third line
line4 = [] # the fourth line
all_lines = [line1, line2, line3, line4]
all_points = [] # all points in the path
car = [] # list of properties of the car. Properties are: start points at each line, x_axis value, y_axis value, angle of line
rsus = []   # list of rsu positions
time_per_iteraiton = 100*math.pow(10,-3)
rsu_legend ='RSU'
positions = []
travelingTimes = []
numberOfcompletedTasks = []
#grpahs parameters
ax.set_ylim([0,1000])   # setting the grid length to 5 units (assume 1 unit = 1mile)
ax.set_xlim([0,1000])  # Generate 4 lanes with distance between each as 3 units
ax.set_xlabel('meters')
ax.set_ylabel('meters')

ax.grid(True)


number_of_rsus = int(input("Number of RSUs: "))


"""####################################################
Function name: get_line()
Description: Get all the points in a line
Input Parameters: void
Return parameters: list of points in the line
#######################################################"""
def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


"""####################################################
Function name: display_grid()
Description: Plot the path for the car and the RSUs
Input Parameters: void
Return parameters: void
#######################################################"""
def display_grid():
    #define global variables
    global all_points
    global all_lines
    global road_legend

    #get the first 2 points and draw the 1st line and plot it
    global line1
    points1 = ginp(2) # get the 2 end points of the first line
    all_points = points1
    x1= [x[0] for x in points1]
    y1=[x[1] for x in points1]
    points1 = get_line(int(x1[0]),int(y1[0]),int(x1[1]),int(y1[1])) # Get all the points in the line
    x1= [x[0] for x in points1]
    y1=[x[1] for x in points1]
    line1 = plt.Line2D(x1,y1) # Create a line object with the x y values of the points in a line
    plt.gca().add_line(line1)
    plt.draw()


    #get the 3rd point and plot the 2nd line
    global line2
    points2 = ginp(1)
    all_points.append(points2[0]) # get the 3rd point
    points2 = get_line(int(all_points[1][0]),int(all_points[1][1]),int(points2[0][0]),int(points2[0][1])) # Get all the points in the line
    x2= [x[0] for x in points2]
    y2= [x[1] for x in points2]
    line2 = plt.Line2D(x2,y2) # Create a line object with the x y values of the points in a line
    plt.gca().add_line(line2)
    plt.draw()

    #get the 4th point and plot the 3rd line
    global line3
    points3 = ginp(1)
    all_points.append(points3[0]) # get the 4th point
    points3 = get_line(int(all_points[2][0]),int(all_points[2][1]),int(points3[0][0]),int(points3[0][1])) # Get all the points in the line
    x3= [x[0] for x in points3]
    y3= [x[1] for x in points3]
    line3 = plt.Line2D(x3,y3) # Create a line object with the x y values of the points in a line
    plt.gca().add_line(line3)
    plt.draw()

    #get the 5th point and plot the 4th line
    global line4
    points4 = ginp(1)
    all_points.append(points4[0]) # get the 5th point
    points4 = get_line(int(all_points[3][0]),int(all_points[3][1]),int(points4[0][0]),int(points4[0][1])) # Get all the points in the line
    x4= [x[0] for x in points4]
    y4= [x[1] for x in points4]
    line4 = plt.Line2D(x4,y4,label='road') # Create a line object with the x y values of the points in a line
    road_legend = line4.get_label()
    plt.gca().add_line(line4)
    plt.draw()

    #get the 5th point and plot the th line
    global line5
    points5 = ginp(1)
    all_points.append(points5[0]) # get the 5th point
    points5 = get_line(int(all_points[4][0]),int(all_points[4][1]),int(points5[0][0]),int(points5[0][1])) # Get all the points in the line
    x5= [x[0] for x in points5]
    y5= [x[1] for x in points5]
    line5 = plt.Line2D(x5,y5,label='road') # Create a line object with the x y values of the points in a line
    road_legend = line5.get_label()
    plt.gca().add_line(line5)
    plt.draw()

    #get the 6th point and plot the 4th line
    global line6
    points6 = ginp(1)
    all_points.append(points6[0]) # get the 5th point
    points6 = get_line(int(all_points[5][0]),int(all_points[5][1]),int(points6[0][0]),int(points6[0][1])) # Get all the points in the line
    x6= [x[0] for x in points6]
    y6= [x[1] for x in points6]
    line6 = plt.Line2D(x6,y6,label='road') # Create a line object with the x y values of the points in a line
    road_legend = line6.get_label()
    plt.gca().add_line(line6)
    plt.draw()

    all_lines = [line1, line2, line3, line4, line5, line6] # List of all points in all the lines


    #get the rsu positions
    for i in range(number_of_rsus):
        rsus.append(ginp(1)[0])  # create a list of rsu positions
        rsu_x = rsus[i][0]  # x position of rsu
        rsu_y = rsus[i][1]  # y position of rsu
        scatter = plt.scatter(rsu_x, rsu_y,label = 'RSU') # Plot the rsu on the grid
        plt.annotate(rsu_legend, xy=(rsu_x,rsu_y), xytext = (rsu_x-50, rsu_y+30))    # label the rsu
        plt.draw()




'''#################################################################
Function name: display_car()
Description: display the car that will traverse the path.
Input Parameters: void
Return parameters: void
####################################################################'''

def display_car(line):
    #define global variables
    global scatter
    global car
    global car_legend
    
    #temporal variable to hold values of car
    points = []
    
    line_props = line_properties(line)

    #add all the properties to the car
    car.append(line_props[0][0]) # first_point x_axis
    car.append(line_props[0][1]) # first_point y_axis
    car.append(line_props[1])  # x_min
    car.append(line_props[2])  # x_max
    car.append(line_props[3])  # angle of the line

    #add scatter
    points.append(line_props[0][0])
    points.append(line_props[0][1])
    
    #plot the cars
    scatter = plt.scatter(points[0],points[1], color = 'red', marker = 's',label ='car')

    #put legend to the graph
    plt.legend(handles=[line4,scatter],loc='upper center', shadow=True)
    plt.draw()
   



'''#################################################################
Function name: simulate_car_movement()
Description: Simulate the car movement in the given path.
             Highlight the path where the car gets coverage from a RSU.
Input Parameters: list of line properties and boolean to indicate if end of line is reached
Return parameters: scatter, com_lines and boolean to indicate if end of line is reached
####################################################################'''
def simulate_car_movement(scatter,com_lines,line_props, eol):

    global car
    coverage = [[],[]]  # x,y values to highlight the coverage on the path.
    #temporal variables
    points= [[],[]]
    scatter.remove()
    
    
   

    while com_lines:
        com_lines[0].remove()
        del(com_lines[0])

    #get all the properties of the car
    velocity = round(np.random.uniform(10,20))
    position_x = car[0]
    position_y = car[1]
    angle = car[4]
    start_point = position_x
    print("The position of the car at the current call is:")
    print(position_x)
   
    print(position_y)
    #calculate new position of the car
    position_x =position_x + velocity*cos(angle)*time_per_iteraiton
    position_y = position_y + velocity*sin(angle)*time_per_iteraiton
    #check if car gets out of the line
    # no need to check for y coordinates as car follows the line
    if position_x < car[2] or position_x > car[3]:
        eol = True # end of this line is reached.
        plt.draw()
        scatter = plt.scatter(points[0],points[1])
        print("We have reached the end of the line")
        print("The distance that the car has traveled is:")
        print(positions[len(positions)-1]-positions[0])
        return [scatter,com_lines, eol] # return from here as end of line is reached.

    # end of line is not reached yet. Hence keep updating the x and y values according to the velocity.
    car[0]=position_x
    car[1]=position_y
    points[0].append(position_x)
    points[1].append(position_y)

    #check if the car is communicating with any of the RSUs
    for rsu_pos in rsus:
        #compute to see if vehicle is in range of any RSU
        inside = math.pow((rsu_pos[0]-position_x),2) + math.pow((rsu_pos[1]-position_y),2) # The distance between the vehicle and an RSU
        if (inside <= math.pow(COM_RANGE,2)):
            # The car is in the communication range of the RSU.
            line = plt.Line2D([position_x,rsu_pos[0]],[position_y,rsu_pos[1]],color='green') # the line to depict communication
            com_lines.append(line)
            coverage[0].append(position_x)
            coverage[1].append(position_y)
            positions.append(position_x)
            end_point = position_x
            distance = end_point - start_point
            time = distance/velocity
            travelingTimes.append(time)
            plt.scatter(coverage[0], coverage[1], color='green')  # highlight the path till the communication range is exceeded. 
            plt.gca().add_line(line)  # Plot the line to depict communication   
            
                
            

    #update the scatter and plot
    scatter = plt.scatter(points[0],points[1], color = 'red', s=20, marker = 's')
    plt.draw()
    print("The distance that the car has traveled is:")
    print(positions[len(positions)-1]-positions[0])
    print("We have spend time of: ")
    print(sum(travelingTimes))
    return [scatter,com_lines, eol]


'''#################################################################
Function name: line_properties()
Description: Get the properties of the car.
Properties are: start points at each line, min x_axis value, max x_axis value, angle of line
Input Parameters: line for which the properties are required
Return parameters: list of properties of line.
####################################################################'''
def line_properties(line):
    line_data= line.get_data() # Get the x and y values of the points in the line
    xdiff = line_data[0][-1]-line_data[0][0]
    ydiff = line_data[1][-1]-line_data[1][0]
    ang = atan2(ydiff,xdiff)
    first_point = list(line.get_xydata()[0]) #first point in the graph

    #get the minimum and maximums of the line to include as a car property
    x_min = min(line_data[0])
    x_max = max(line_data[0])

    return [first_point, x_min, x_max, ang]
    


processingTime = []
for i in range(number_of_rsus):
    processingTime.append(np.random.normal(13,2,1))

display_grid()
display_car(line1) # display the starting point of the car.
display_car(line1)
display_car(line2)
display_car(line3)
display_car(line4)
display_car(line5)
display_car(line6)
line_props = [] # list to store properties of line

print(len(all_lines))
loads = []
line_props = line_properties(all_lines[0])
print("The first point is :")
print(line_props[0])
print("The x-min is :")
print(line_props[1])
print("The x-max is :")
print(line_props[2])
print("The ang is :")
print(line_props[3])
eol = False
com_lines =[]

car = [] # create an empty list to store property of car for every line of the path.
display_car(all_lines[0]) # Display the car at the start of each line of the path. 
load = np.random.normal(13,2,1)
print("The load of the first RSU is:")
print(processingTime[1])
print("========================")
if(processingTime[0]<=9):
    while eol == False:
        [scatter,com_lines,eol] = simulate_car_movement(scatter,com_lines,line_props,eol)
    loads.append(processingTime[0])
    print("We offload at the first:")
elif(processingTime[1]<=10):
    line_props = line_properties(all_lines[1])
    eol = False
    com_lines =[]
    car = [] # create an empty list to store property of car for every line of the path.
    display_car(all_lines[1]) # Display the car at the start of each line of the path. 
    while eol == False:
        [scatter,com_lines,eol] = simulate_car_movement(scatter,com_lines,line_props,eol)
    loads.append(processingTime[1])
    print("We offload at the second:")
elif(processingTime[2]<=10):
    line_props = line_properties(all_lines[2])
    eol = False
    com_lines =[]
    car = [] # create an empty list to store property of car for every line of the path.
    display_car(all_lines[2]) # Display the car at the start of each line of the path. 
    while eol == False:
        [scatter,com_lines,eol] = simulate_car_movement(scatter,com_lines,line_props,eol)
    loads.append(processingTime[2])
    print("We offload at the third:")
elif(processingTime[3]<=11):
    line_props = line_properties(all_lines[3])
    eol = False
    com_lines =[]
    car = [] # create an empty list to store property of car for every line of the path.
    display_car(all_lines[3]) # Display the car at the start of each line of the path. 
    while eol == False:
        [scatter,com_lines,eol] = simulate_car_movement(scatter,com_lines,line_props,eol)
    loads.append(processingTime[3])
    print("We offload at the 4th:")
else:
    line_props = line_properties(all_lines[4])
    eol = False
    com_lines =[]
    car = [] # create an empty list to store property of car for every line of the path.
    display_car(all_lines[4]) # Display the car at the start of each line of the path. 
    while eol == False:
        [scatter,com_lines,eol] = simulate_car_movement(scatter,com_lines,line_props,eol)
    loads.append(processingTime[4])
    print("We offload at the fifth:")


print(mean(loads))
print(sum(travelingTimes))
print(loads)
if(mean(loads)<=sum(travelingTimes)):
        print("that's a good indication")




plt.draw()
plt.show() 


