
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapping import Scrapping
import time

scrapping=Scrapping()

total=scrapping.get_details()
price=total[0]
adress=total[1]
room=total[2]



chrome_driver="C:/Users/PRIYA KESHRI/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdBUiPUvY6AYx5qEPUcjXm4neaZP66IHQylRgbtP4JkSwE1BQ/viewform?usp=sf_link")
time.sleep(2)

for n in range(len(adress)-1):
    name = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    name.click()
    time.sleep(2)
    name.send_keys(adress[n])
    time.sleep(2)
    rent=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    rent.click()
    time.sleep(2)
    rent.send_keys(price[n])
    time.sleep(2)
    rooms=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    rooms.click()
    time.sleep(2)
    rooms.send_keys(room[n])
    submit=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit.click()
    time.sleep(5)
    submit_another_response=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submit_another_response.click()
    time.sleep(2)


