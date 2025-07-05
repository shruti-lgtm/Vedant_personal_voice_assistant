from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By  

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(
            r"C:\Users\Shrut\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
        ))

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

        # ✅ FIXED LINES BELOW
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')  
        input("Press ENTER to exit...")


