import calc2,turtle
a1=turtle.Turtle()
#q1
def draw_s1(t,n,degree):
    """raw 60 squares, turning right 5 degrees after each square."""
    for i in range (n):
        calc2.square(a1,200)
        a1.rt(degree)

# draw_s(a1,60,5)

#q2
def draw_s2(t,n,degree,X):
    for i in range(n):
        """Write an appropriately general set of functions that can draw shapes as below. Tips: draw 60 squares, turning 5 degrees 
        after each square and making each successive square bigger. 
        Start at a length of 30 and increment 4 units every square."""
        calc2.square(a1,30+X)
        X=X+4
        a1.rt(degree)
        
# draw_s2(a1,60,5,4)

#q3 I think I have some identicattion issue on this problem about the picture ( Math problem!)which kind of shape should we start with?
import math
def triangle(t,a,x):
    t.bk(a)
    t.lt(90)
    t.bk(a)
    t.rt(45)
    t.fd(a+x)

    
def draw_s3(t,n,a,x,degree):
    for i in range(n):
        triangle(t,a,x)
        a=a+4
        x=x+4
        a1.rt(degree)

# draw_s3(a1,70,90,95,2)

#q4 Get helped from the internet and other websites

def draw_s4(t,a,b,degree,n):
    for i in range (n*360):
        r=a+b*degree
        x=r*math.cos(math.radians(degree))
        y=r*math.sin(math.radians(degree))
        turtle.goto(x,y)
        degree=degree+1

draw_s4(a1,2,2,0,10)
        


 

# triangle(a1,60,90,40,120,90)
# def draw_s3(t,n)
#     for i in range(n):
#         triangle    



# triangle(a1,10,90,(10*math.sqrt(3)),90,20,30)
turtle.mainloop



