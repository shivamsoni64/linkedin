import unittest                     
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tracemalloc
from selenium.webdriver.support.ui import Select
tracemalloc.start()
from selenium.common.exceptions import NoSuchElementException

user = "linkedinid"
passs = "linkedinpassword"
sreach = "hr indore it companies"


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\TechInfini\Downloads\chromedriver_win32\chromedriver")
        self.driver.get("https://www.linkedin.com/login")
        
    def test_valid_credentials(self):
        #self.driver.maximize_window()
        time.sleep(1)
        username_input = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        password_input = self.driver.find_element(By.XPATH,'//*[@id="password"]')     
        time.sleep(1)
        username_input.send_keys(user)
        self.driver.execute_script("window.scrollTo(0, 200)")
        password_input.send_keys(passs)
        time.sleep(2)
        submit_button =self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[1]/form/div[3]/button')
        submit_button.click()
        
        
        wait = WebDriverWait(self.driver, 10)             #This creates a WebDriverWait object that waits for a maximum of 10 seconds for an element to become visible on the web page. 
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/header/div/div/div/div[1]/input")))     # The EC.visibility_of_element_located method returns the located WebElement once it is visible,
        element.send_keys(sreach)
        
        time.sleep(5)
        self.driver.find_element(By.XPATH,'/html/body/div[5]/header/div/div/div/div[1]/input').send_keys(Keys.RETURN)   #Keys.RETURN represents the "Enter" key.
        
        

        time.sleep(5)
        people_button =self.driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[2]/div/div[1]/div/div/div/section/ul/li[1]/button')
        people_button.click()

        time.sleep(4)

        #dropdown = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button/span')
        #select = Select(dropdown)
        #select.select_by_index(3)

     
        
        viewall_button =self.driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/a')
        viewall_button.click()                            
        time.sleep(10)
        

        for y in range(1, 100):                
            for x in range(1, 10):
                profile_xpath = f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[3]/div/ul/li[{x}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]'
                                 
                if self.driver.find_element(By.XPATH, profile_xpath):
                   self.driver.find_element(By.XPATH, profile_xpath).click()
                   time.sleep(2)
                   try:
                        self.driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span').click()
                        time.sleep(1)
                   except NoSuchElementException:
                        pass  
                         
                   try:
                        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]/span').click()
                        time.sleep(1)
                   except NoSuchElementException:
                     print(f"Profile {x} not found on the page")

                   self.driver.back()
                   time.sleep(2)
            pagenumber_xpath = f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[6]/div/div/button[2]/span'  
            self.driver.find_element(By.XPATH, pagenumber_xpath).click()

if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        print(f"An error occurred: {e}")
