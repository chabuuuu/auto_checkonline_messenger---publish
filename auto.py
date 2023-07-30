from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json


#Project by chabuuuu

with open('setting.json', 'r') as f:
  data = json.load(f)


#Lấy username và password của account bot
username = data["username"]
password = data["password"]
#Set giờ bắt đầu và kết thúc
hourStart = data["hourStart"]
hourEnd = data["hourEnd"]
#Set thông tin về account muốn check online: Cần có link dẫn đến messenger của account đó.
userLink1 = data["userLink1"]
userLink2 = data["userLink2"]
#Set tên acc Facebook or tên bạn muốn con bot gọi người kia
personName1 = data["personName1"]
personName2 = data["personName2"]
#Set link messenger của group hoặc account mà bạn muốn bot nhắn vào để thông báo
groupLink = data["groupLink"]


options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/')

#Đăng nhập

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(username)

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(password)

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

#Khai báo các biến
isTrueHour = True
firstStart = True

#Hàm send tin nhắn
def sendMessage(send):
    print("sending message...")
    driver.get('https://www.facebook.com/messages/t/6567795873287046')
    time.sleep(5)
    #Gửi tin nhắn
    message = driver.find_element(By.CLASS_NAME, 'xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x1iyjqo2.x1gh3ibb.xisnujt.xeuugli.x1odjw0f.notranslate')
    message.send_keys(send)
    message.send_keys(Keys.RETURN)   

#Hàm thông báo không check online
def Hour(isTrueHour, firstStart):
    if (isTrueHour == True):
        print("Chưa đến giờ")
        if (firstStart == False):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            send = "Chào buổi sáng, chúc bạn một ngày tốt lành. Kết thúc check online vào lúc: "+current_time
            sendMessage(send)
        
#Hàm thông báo đến giờ check online
def thongBaoDenGio(isTrueHour):
    if (isTrueHour == False):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        send = "Đã đến giờ đi ngủ! Bắt đầu kiểm tra từ: "+current_time
        sendMessage(send)
    

while(True):
   
    
    #Kiểm tra đã đến giờ hay chưa
    now = datetime.now()
    current_hour = now.hour
    if (current_hour >= hourStart and current_hour <= (hourEnd - 1)):
        thongBaoDenGio(isTrueHour)
        
        
        isTrueHour = True
        print("Checking...")
    
        
        
        #Khai báo
        firstPerOnline = False
        secondPerOnline = False
        
        #Vào check mess của person1
        time.sleep(3)
        driver.get(userLink1)

        time.sleep(10)

        #Kiểm tra xem thông tin về trạng thái hoạt động có đang được hiển thị hay không, nếu không thì báo "Không có trạng thái"
        status = driver
        try:
            status = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x3x7a5m.x1nxh6w3.x1sibtaa.x1fcty0u.xi81zsa.x2b8uid'))
            )
            status = status.text
            
            
            
            
            
        except:
            print("Không có trạng thái")
        
       
        #Chỗ này nếu facebook của bạn đang để tiếng anh thì hãy đổi thành "Online" hoặc tương tự với các ngôn ngữ khác
        if (status == "Đang hoạt động"):
            firstPerOnline = True
        else:
            firstPerOnline = False

        if (firstPerOnline == True):
            thongBao = personName1+" is online"
            print(thongBao)
            driver.get(groupLink)
            time.sleep(5)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            send = "Phát hiện "+personName1+" online vào "+current_time
            #Gửi tin nhắn
            message = driver.find_element(By.CLASS_NAME, 'xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x1iyjqo2.x1gh3ibb.xisnujt.xeuugli.x1odjw0f.notranslate')
            message.send_keys(send)
            message.send_keys(Keys.RETURN)
            
        #Chuyển sang check account 2
        time.sleep(3)
        driver.get(userLink2)

        time.sleep(10)
        


        status = driver
        try:
            status = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x3x7a5m.x1nxh6w3.x1sibtaa.x1fcty0u.xi81zsa.x2b8uid'))
            )
            status = status.text
            
            
            
            
            
        except:
            print("Không có trạng thái")
        
       

        if (status == "Đang hoạt động"):
            secondPerOnline = True
        else:
            secondPerOnline = False

        if (secondPerOnline == True):
            thongBao = personName2+" is online"
            print(thongBao)
            driver.get(groupLink)
            time.sleep(5)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            send = "Đề nghị đi ngủ ngay! Phát hiện "+personName2+" online vào "+current_time
            #Gửi tin nhắn
            message = driver.find_element(By.CLASS_NAME, 'xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x1iyjqo2.x1gh3ibb.xisnujt.xeuugli.x1odjw0f.notranslate')
            message.send_keys(send)
            message.send_keys(Keys.RETURN)
            
        time.sleep(5)
        
    else:
          Hour(isTrueHour, firstStart)
          isTrueHour = False
    firstStart = False
          
        
        
  
            
       
            
    
        
    

        
        
        

