#492. Construct the Rectangle
#related topics
#math
def constructRectanlge(area):
    for l in range(int(area**0.5,0,-1)):
        if area %l==0:
            return [area//l,l]