size(500,500)
def clearRed(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = 0 
        g = green(pixels[i])
        b = blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()
   
def clearGreen(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i]) 
        g = 0 
        b = blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()

def clearBlue(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i]) 
        g = green(pixels[i])
        b = 0
        pixels[i] = color(r,g,b)
    updatePixels()

def makeRed(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i]) 
        g = 0
        b = 0
        pixels[i] = color(r,g,b)
    updatePixels()

def makeGreen(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = 0 
        g = green(pixels[i])
        b = 0
        pixels[i] = color(r,g,b)
    updatePixels()

def makeBlue(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = 0 
        g = 0
        b = blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()
    
def reduceRed(Picture,x): #use decimals
    img = loadImage(str(Picture))
    image(img,0,0)
    x = float(x)
    loadPixels()
    for i in range(0,len(pixels)):
        r = x*red(pixels[i])
        g = green(pixels[i])
        b = blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()

def reduceGreen(Picture,x): #use decimals
    img = loadImage(str(Picture))
    image(img,0,0)
    x = float(x)
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i])
        g = x*green(pixels[i])
        b = blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()    
    
def reduceBlue(Picture,x): #use decimals
    img = loadImage(str(Picture))
    image(img,0,0)
    
    x = float(x)
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i])
        g = green(pixels[i])
        b = x*blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()    

def makeGray(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i])
        g = green(pixels[i])
        b = blue(pixels[i])
        gray =(r+g+b)/3
        pixels[i] = color(gray)
    updatePixels() 

def makeNegative(Picture):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = 255 - red(pixels[i])
        g = 255 - green(pixels[i])
        b = 255 - blue(pixels[i])
        pixels[i] = color(r,g,b)
    updatePixels()
    
def makeSunset(Picture,x,y):
    img = loadImage(str(Picture))
    image(img,0,0)
    
    x = float(x)
    y = float(y)
    loadPixels()
    for i in range(0,len(pixels)):
        r = red(pixels[i])
        g = 94
        b = 83
        pixels[i] = color(r,g,b)
    updatePixels()

def myChoice(Picture): #Negative Grayscale 
    img = loadImage(str(Picture))
    image(img,0,0)
    
    loadPixels()
    for i in range(0,len(pixels)):
        r = 255 - red(pixels[i])
        g = 255 - green(pixels[i])
        b = 255 - blue(pixels[i])
        gray = (r+g+b)/3
        pixels[i] = color(gray)
    updatePixels()

makeGray("beach.jpg")
