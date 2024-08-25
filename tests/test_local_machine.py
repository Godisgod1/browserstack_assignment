import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys

# Function to perform the required tasks on flipkart.com
def run_test(driver):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    # Search for the product
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//a[@class="hEjLuS WyLc0s"]'))).click()
    
    
    time.sleep(3)
    # Click on "samsung"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//div[text()="SAMSUNG"]'))).click()

    #Click on assured
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH,'//div[@class="SwtzWS"]'))).click()
    
    # high ---> low
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH,"//div[text()='Price -- High to Low']"))).click()
    

    #data of each product on page 1
    product_names = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
    display_prices = driver.find_elements(By.CLASS_NAME, "hl05eU")
    product_links = driver.find_elements(By.CLASS_NAME, "CGtC98")

    # Create and print the list
    results_list = []
    for i in range(len(product_names)):
        results_list.append({
            "Product Name": product_names[i].text,
            "Display Price": display_prices[i].text,
            "Link to Product Details Page": product_links[i].get_attribute("href")
        })

    for result in results_list:
        print(result)
    driver.quit()


try:
    for i in range(1):  # Number of parallels
        driver = webdriver.Chrome()
        run_test(driver)
except Exception as e:
    print(f"Error: {e}")





#http://localhost:8080/