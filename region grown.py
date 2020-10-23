import cv2, cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def on_mouse(event, l, r, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print ('Start Mouse Position: ' + str(x) + ', ' + str(y))
        s_box = (l, r)
        boxes.append(s_box)




def region_growing(img, seed, trs):
     x , y = seed
     #to_get_neighbours = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
     neighbours = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
     h , w = img . shape
     out = np.zeros_like(img)
     out[x,y] = 255
     for i in neighbours:
         if ((abs(img[x,y]-img[i[0],i[1]])) > trs):
             out[i[0],i[1]] = 255
             p = neighbours . pop(i)
             p_neighbours = [(int(p[0])-1,int(p[1])-1),(int(p[0]),int(p[1])-1),(int(p[0])+1,int(p[1])-1),(int(p[0])-1,int(p[1])),(int(p[0])+1,int(p[1])),(int(p[0])-1,int(p[1])+1),(int(p[0]),int(p[1])+1),(int(p[0])+1,int(p[1])+1)]
             for point in p_neighbours:
                 if (point not in neighbours):
                     neighbours.append(point)
         else:
             continue
     return out
                       








boxes = []
img = cv2.imread('madara.jpg', 0)
cv2.namedWindow('input')
cv2.imshow('input', img)
cv2.setMouseCallback('input', on_mouse, 0,)
seed = boxes
cv2.imshow('input', region_growing(img, seed,10))
cv2.waitKey()
cv2.destroyAllWindows()