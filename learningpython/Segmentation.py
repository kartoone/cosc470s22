
from PIL import Image
im = Image.open("digits.png","r")
pixels = list(im.getdata())
print(pixels)
print(im.size)


# solving the segmenation problem ... general approach: look for the "separation" between the digits
# step 1: turn our 1d list of pixels back into a 2d list of pixels
# step 1a: determine size of original image (width x height)
# step 1b: nested loop that grabs each pixel and puts it into the correct row
pixels2d = []
width, height = im.size
pi = 0 # pixel index ... index into our 1d list of pixels
for _ in range(height):
  row = []
  flag = False
  for _ in range(width):
    # convert the pixel to a standard black/white pixel before stuffing it into the row
    if pixels[pi][0] > 200:
      row.append(1)
    else:
      row.append(0)
      flag = True
    pi = pi + 1
  if flag:
    pixels2d.append(row)

for row in pixels2d:
  for p in row:
    print(p,end='')
  print()


# now go through the image again - column by column storing the start/end of each digit
xcoords = []
mode = 0 # in mode 0, we are looking for the start of the next digit
         # in mode 1, we are looking for the start of the separation
         # mode 2, is just temporary so we can break out of the loop early from mode 0
         # and safely transition to mode 1 without appending the "x" from that iteration
for x in range(width):
  flag = True    # we need this flag variable when we are in mode 1 b/c we have to make it through the ENTIRE nested loop below without ever seeing a black pixel (which causes us to set the flag to false meaning that we haven't hit the separation column yet)
  for row in pixels2d:
    if mode==0 and row[x] == 0:
      xcoords.append(x-1) # account for having gone one "too far" by the time we hit the digit
      mode=2 # transition mode - optimization I thought up when commenting the code so that we can go ahead and break out as soon as we see a black pixel (b/c that means we successfully found the start of the digit)
      break
    elif mode==1 and row[x] == 0:
      flag=False
      break
  if mode==2:
    mode=1  # we really wanted to transition straight to mode 1, but by first transitioning to mode 2 that keeps us from hitting the elseif and appending the x coord accidentally
            # so now we can safely transition to mode 1 to start the next loop iteration
            # this solves the 1 pixel edge case perfectly ... and makes it run a bit faster too
  elif mode==1 and flag:
    xcoords.append(x)
    mode = 0
print(xcoords)

    

# insert hashtag to replace all the 1s in the "separation" columns stored in xcoords
for x in xcoords:  
  for row in pixels2d:
      row[x] = '#'

# display the updated pixel2d list with the special hashtag separators
for row in pixels2d:
  for p in row:
    print(p,end='')
  print()


