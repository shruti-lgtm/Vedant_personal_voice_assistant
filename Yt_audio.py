from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(
            r"C:\Users\Shrut\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
        ))

    def play(self_, query):
        self_.query = query
        self_.driver.get("https://www.youtube.com/results?search_query=" + query)
        time.sleep(2)
        video = self_.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        input("Press ENTER to exit...")


