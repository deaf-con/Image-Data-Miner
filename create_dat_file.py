
# coding: utf-8

# In[1]:


import cv2
import os.path

obj = 'pedestrian'
obj_neg = ['oilfield','pumpjack','sky_raw','trees_raw','conference_raw']

MAX_N = 10000


running_sum = 0.0
counter = 0


# In[2]:


for i in range(MAX_N):
    try:
        if os.path.isfile(obj+"/obj"+str(i)+".jpg"):
            img = cv2.imread(obj+"/obj"+str(i)+".jpg",0)
            h, w = img.shape[:2]
            try:
                with open('info_pedestrian_v4.dat','a') as file:
                    file.write(obj+"/obj"+str(i)+".jpg 1 0 0 "+str(w)+" "+str(h)+'\n')

                #running_sum = running_sum + (w + 0.0)/(h + 0.0)
                #counter = counter + 1

            except:
                pass
                        
    except:
        pass

#print (running_sum+ 0.0)/(counter+ 0.0)
    
    


# In[3]:


for k in range(len(obj_neg)):
    for j in range(MAX_N):
        try:
            
            if os.path.isfile (obj_neg[k]+"/obj"+str(j)+".jpg"):
            #img = cv2.imread(obj_neg[k]+"/obj"+str(i)+".jpg",0)
                with open('bg_pv4.txt','a') as file:
                    file.write(obj_neg[k]+'/obj'+str(j)+".jpg\n")
            elif os.path.isfile (obj_neg[k]+"/img"+str(j)+".jpg"):
                with open('bg_pv4.txt','a') as file:
                    file.write(obj_neg[k]+'/img'+str(j)+".jpg\n")
        except:
            pass


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




