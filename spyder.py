
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import json


# In[2]:


SCROLL_PAUSE_TIME = 1
#SAMPLES_NEEDED = 500

search_item = "streets"


# In[3]:


url_gi = "https://www.google.ca/search?biw=1845&bih=897&tbm=isch&sa=1&q="+search_item+"&oq="+search_item+"&gs_l=psy-ab.3..0l4.1642224.1645357.0.1645692.19.13.2.0.0.0.320.1672.0j3j4j1.8.0....0...1.1.64.psy-ab..9.9.1453.0..0i5i30k1j0i10i24k1j0i24k1j0i67k1.5hdidGyV3JE"


# In[4]:


#url_gi = "https://www.google.ca/search?biw=1855&bih=966&tbm=isch&sa=1&q=show+booths&oq=show+booths&gs_l=psy-ab.3..0i67k1j0j0i7i30k1l2.12991.13491.0.14998.2.2.0.0.0.0.101.194.1j1.2.0....0...1.1.64.psy-ab..0.2.194.YPBV9Lq1crQ"


driver = webdriver.Chrome()
driver.get(url_gi)
img_count = 0

def scroll_n_times(n):
    global driver
    
    for i in range(n):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
    
    return
        
def show_more(n):
    global driver
    scroll_n_times(4)
    
    for i in range(n):    
        elem = driver.find_element_by_id("smb")
        elem.send_keys(Keys.RETURN)
        scroll_n_times(4)
    
    
    
    
while True:
    show_more(1)
    
    imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
        
    for img in imges:
        
        try:
            img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
            img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
        except:
            img_type = False
        
        if img_type == "jpg":
            try:
                urllib.urlretrieve(img_url, search_item+"_raw/img"+str(img_count)+".jpg")
                img_count += 1
            except:
                print "No image at "+img_url
        


# In[ ]:


print img_count


# In[ ]:





# In[ ]:




