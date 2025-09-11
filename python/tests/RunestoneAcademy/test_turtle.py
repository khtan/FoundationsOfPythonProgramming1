#imports
import sys
import logging
import turtle
import pytest
# region globals
pytest.skip("skipping turtle tests", allow_module_level=True) # Turtle tests require interactvely closing the turtle window
logger = logging.getLogger(__name__)

# endregion globals
# pure functions
# region impure
def draw_polygon(tx, numsides: int, distance: int, color: str):
   turnangle = 360 / numsides
   tx.color(color)
   for _ in range(numsides):
      tx.forward(distance)
      tx.left(turnangle)

# endregion impure
# region tests
def test_clock_face():
   wn = turtle.Screen()
   tt = turtle.Turtle()
   tt.shape("turtle")
   tt.color("blue")
   tt.up()
   tt.stamp()
   distance = 100
   for _ in range(12):
      tt.forward(distance)
      tt.stamp()
      tt.backward(distance)
      tt.left(30)
   wn.exitonclick()

# last line is the horizontal
def test_star2():
   wn = turtle.Screen()
   tt = turtle.Turtle()
   tt.color("blue")
   distance = 100
   numlines = 5
   turnangle = 180+36
   for _ in range(numlines):
      tt.left(turnangle)
      tt.forward(distance)      
   wn.exitonclick()

# last line is the oblique
def test_star():
   wn = turtle.Screen()
   tt = turtle.Turtle()
   tt.color("blue")
   distance = 100
   numlines = 5
   turnangle = 144
   tt.right(90+18)
   for _ in range(numlines):
      tt.left(turnangle)
      tt.forward(distance)      
   wn.exitonclick()

# This is for pasting in Runstone that does not recognise def
def test_5_polygons_unravelled():
   wn = turtle.Screen()
   tt = turtle.Turtle()

   # draw_polygon(tt, 3, 100, "red")
   numsides=3
   distance=100
   color="red"
   turnangle = 360 / numsides
   tt.color(color)
   for _ in range(numsides):
      tt.forward(distance)
      tt.left(turnangle)

   # draw_polygon(tt, 4, 120, "blue")
   numsides=4
   distance=120
   color="blue"
   turnangle = 360 / numsides
   tt.color(color)
   for _ in range(numsides):
      tt.forward(distance)
      tt.left(turnangle)

   # draw_polygon(tt, 6, 160, "blue")
   numsides=6
   distance=140
   color="red"
   turnangle = 360 / numsides
   tt.color(color)
   for _ in range(numsides):
      tt.forward(distance)
      tt.left(turnangle)

   # draw_polygon(tt, 8, 160, "red")
   numsides=8
   distance=160
   color="blue"
   turnangle = 360 / numsides
   tt.color(color)
   for _ in range(numsides):
      tt.forward(distance)
      tt.left(turnangle)
      
   wn.exitonclick()

@pytest.mark.serial
def test_5_polygons():
   wn = turtle.Screen()
   tt = turtle.Turtle()

   draw_polygon(tt, 3, 100, "red")
   draw_polygon(tt, 4, 120, "blue")
   draw_polygon(tt, 5, 140, "red")
   draw_polygon(tt, 6, 160, "blue")
   draw_polygon(tt, 8, 160, "red")
   wn.exitonclick()

@pytest.mark.serial
def test_3_spiral():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.color("blue")
    tess.shape("turtle")

    dist = 5
    tess.up()
    for _ in range(30):
        tess.stamp()
        tess.forward(dist)
        tess.right(24)
        dist = dist + 2
    tess.color("red")
    wn.exitonclick()

@pytest.mark.serial
def test_2_circle():
    wn = turtle.Screen()    
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.penup()
    for size in range(10):
        tess.forward(50)
        tess.stamp()
        tess.forward(-50)        
        tess.right(36)
    wn.exitonclick()

@pytest.mark.serial
def test_1_goeast():
    wn = turtle.Screen()    
    nikea = turtle.Turtle()
    nikea.shape("turtle")
    nikea.penup()            
    for size in range(3):
        nikea.forward(50)
        nikea.stamp()
    wn.exitonclick()
# endregion tests

