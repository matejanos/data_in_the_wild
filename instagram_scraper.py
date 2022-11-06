import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

#Set up the driver
driver = webdriver.Chrome('C:\\Users\\Jani\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.instagram.com")

#Log in to the application
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
allow_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'))).click()
username.clear()
password.clear()
username.send_keys("data_in_the_wild")
password.send_keys("Datainthewild1")
log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button"))).click()

#Reject the cookies
not_now = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button"))).click()
not_now2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))).click()

#Search for a person
#TODO should make a list of people
search_input_words = ['bulldogs', 'bullterriers']
for i in search_input_words:
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/a"))).click()
    search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/input")))
    search_box.clear()
    keyword = i
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    clicking_profile = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a"))).click()
    clicking_posts = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/div[2]/a[1]"))).click()

    #How many picture we would like to get
    driver.execute_script("window.scrollTo(0,5000);")

    #create the directory
    path = os.getcwd()
    path = os.path.join(path, keyword)
    os.mkdir(path)

    #Save the images
    images = driver.find_elements(By.TAG_NAME, 'img')
    counter = 1
    for i in images:
        imgURL = (i.get_attribute('src'))
        filename = f"{counter}.jpg"
        urllib.request.urlretrieve(imgURL, f"{path}/{filename}")
        counter += 1
    driver.get("https://www.instagram.com")