#832. Flipping an Image
#related topics
#array


image = [[1,1,0],[1,0,1],[0,0,0]]
image2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

    
#First solution
def flipAnfInvertImage(image):
    

    for i,n in enumerate(image):
        for j in range(len(n)):
            image[i][j]=1 if image[i][j]==0 else 0
    for lst in image:
        lst.reverse()
    return image

print(flipAnfInvertImage(image))
print(flipAnfInvertImage(image2))


#second solution 
def flipAnfInvertImage2(image):
    return [[1-i for i in rwo[::-1]] for rwo in image]

print(flipAnfInvertImage2(image))
print(flipAnfInvertImage2(image2))