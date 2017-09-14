
# coding: utf-8

# In[1]:


import cv2
import os
import numpy as np


# In[2]:


obj_str = 'conference'
alt_folder = 'conference_ppl'
cropping = False
measuring = False
blanking = False
_x = 0
_y = 0
font = cv2.FONT_HERSHEY_SIMPLEX


# In[3]:


obj_counter = 0

#img_counter = 0

img_counter = 2012


# In[4]:


width = 480
height = 360
resize_tf = 1
scale = 1


# In[5]:


imgs = [im.replace("img","") for im in os.listdir(obj_str+"_raw")]
imgs = [int(im.replace(".jpg","")) for im in imgs]
max_index = max(imgs)


# In[6]:


def nothing(x):
    pass


def resize_img(n):
    global img, tru_og, width, height, scale
    
    if n == 1:
        width = 480 * scale
        height = 360 * scale
        img = cv2.resize(img,(width,height))
    elif n == 0:
        img = tru_og.copy()
        height, width, channels = img.shape
        
                
def get_img(n):
    global img, og, tru_og
    try:
        img = cv2.imread(obj_str+'_raw/img'+str(n)+'.jpg',1)
        tru_og = img.copy()

        resize_img(cv2.getTrackbarPos('resize', 'img'))
            
    except:
        no_img(n)
        
    og = img.copy()
    
    
def no_img(n):
    global img, tru_og, height, width
    
    img = np.zeros((height,width,3), np.uint8)
    cv2.putText(img,"img"+str(n)+'.jpg was not found',((width-250-len(str(n))*14)/2,(height-10)/2),font,0.7,(255,255,255),2)
    cv2.putText(img,"img"+str(n)+'.jpg was not found',((width-250-len(str(n))*14)/2,(height-10)/2),font,0.7,(0,0,0),1)
    tru_og = img.copy()        

    
def move_img(og_fld, nu_fld, n):
    #global img
    try:
        img_mi = cv2.imread(og_fld+'/img'+str(n)+'.jpg',1)
        os.remove(og_fld+"/img"+str(n)+".jpg")
        cv2.imwrite(nu_fld+"/img"+str(n)+".jpg",img_mi)
        print "Moved img"+str(n)+".jpg to "+ nu_fld
    except:
        print "Could not move img"+str(n)+".jpg to "+ nu_fld

def scale_img(n):
    global width, height, img, scale
    
    if n == 0:
        scale = 0.5
    else:
        scale = n
        
    width = int(width * scale)
    height = int(height * scale)
    
    img = cv2.resize(img,(width,height))


# In[7]:


def crop_img(event,x,y,flags,param):
    global _x, _y, cropping, blanking, measuring, img, og, obj, obj_counter, obj_str
    
##################################################################################
##################################################################################   

    if event == cv2.EVENT_LBUTTONDOWN:
        if cropping == False:
            cropping = True
            _x,_y = x,y              
        
    elif event == cv2.EVENT_LBUTTONUP:
        if cropping == True:                
            if x <= 0 or y <= 0:
                cropping = False
            else:            
                cv2.rectangle (img, (_x,_y), (x,y),(255,0,0),2)
                obj = og[min(_y,y):max(_y,y),min(_x,x):max(_x,x)]

                cv2.imshow('obj',obj)
                
                cropping = False
                cv2.imwrite(obj_str+"/obj"+str(obj_counter)+".jpg",obj)
                obj_counter += 1
                
##################################################################################

    elif event == cv2.EVENT_RBUTTONDOWN:
        if blanking == False:
            blanking = True
            _x,_y = x,y

    elif event == cv2.EVENT_RBUTTONUP:
        if blanking == True:                     
            if x <= 0 or y <= 0:
                blanking = False
            else:            
                cv2.rectangle (img, (_x,_y), (x,y),(0,0,0),-1)
                og = img.copy()
                blanking = False

##################################################################################
        
    elif event == cv2.EVENT_MBUTTONDOWN:
        if measuring == False:
            measuring = True
            _x,_y = x,y

    elif event == cv2.EVENT_MBUTTONUP:
        if measuring == True:                     
            if x <= 0 or y <= 0:
                measuring = False
            else:            
                cv2.rectangle (img, (_x,_y), (x,y),(255,255,255),1)
                #og = img.copy()
                print "Width: "+str(abs(_x-x))
                print "Height: "+str(abs(_y-y))
                measuring = False
                
#########################################    global img#########################################                
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            img = og.copy()
            cv2.rectangle(img, (_x,_y), (x,y),(0,255,0),2)
        
        elif blanking == True:
            img = og.copy()
            cv2.rectangle(img, (_x,_y), (x,y),(0,0,0),2)
            
        elif measuring == True:
            img = og.copy()
            cv2.rectangle(img, (_x,_y), (x,y),(255,255,255),1)

##################################################################################
##################################################################################
                           


# In[ ]:


try:
    img = cv2.imread(obj_str+'_raw/img'+str(img_counter)+'.jpg',1)
    tru_og = img.copy()
    resize_img(resize_tf)

except:
    no_img(img_counter)
    
obj = img.copy()
og = img.copy()


# In[ ]:


cv2.namedWindow('img')

cv2.createTrackbar('resize','img', 1, 1, resize_img)
cv2.createTrackbar('scale','img', 1, 2, scale_img)
cv2.createTrackbar('image no:','img', img_counter, max_index, get_img)

cv2.setMouseCallback('img', crop_img)

while(1):
    
    img_cnt = cv2.getTrackbarPos('image no:', 'img')
    
    try:
        cv2.imshow('img', img)
    except:
        pass 
        
    
    wait_on_key = cv2.waitKey(10)
    
    
    if wait_on_key == ord('q'):
        break

    elif wait_on_key == ord('m'):
        move_img(obj_str+"_raw",alt_folder+"_raw",img_cnt)
        
    elif wait_on_key == ord('u'):
        move_img(alt_folder+"_raw",obj_str+"_raw",img_cnt)
    
    
cv2.destroyAllWindows()
    
    


# In[ ]:


print img.width


# In[ ]:




