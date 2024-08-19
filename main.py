from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os
from dotenv import load_dotenv
from pages import pages

# Random Category
def randomCategory():
    category = random.choice(list(pages.keys()))
    item = random.choice(pages[category])
    return item
randomItem = randomCategory()

# User information from .env file
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
link = os.getenv("LINK")

# Page options (close notifications)
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)

# Driver
driver = webdriver.Chrome(options=options)
driver.get(link)
driver.maximize_window()

# Scroll down func
def scroll_down(px):
    sleep(1)
    current_scroll_y = driver.execute_script("return window.scrollY;")
    new_scroll_y = current_scroll_y + px
    driver.execute_script(f"window.scrollTo(0, {new_scroll_y});")

# Scroll to element
def scrollElement(element):
    location = element.location
    y_location = location['y'] 
    current_scroll_position = driver.execute_script("return window.scrollY")
    scroll_down(y_location - current_scroll_position)

# Using slidebar and go footer func
def goFooter(): 
    footer = driver.find_element(By.CLASS_NAME, 'site-footer-grid')
    driver.execute_script("arguments[0].scrollIntoView(true)",footer)

# Go to any category
def goCategory(categoryLabel):
    element = driver.find_element(By.CSS_SELECTOR, categoryLabel)
    element.click()

# Pick any filter
def pickFilter():
    # Only 5 elements can be click, if there is more element we should use slidebar
    checkbox_elements = driver.find_elements(By.CSS_SELECTOR, ".js-facet-list-brand .facet__checkbox")
    valueList = []
    for checkbox in checkbox_elements:
        valueList.append(checkbox.get_attribute("value"))
    print(f"Filter List: \n{valueList}")
    rNumber = random.randint(0,len(checkbox_elements)-1)
    try:
        checkbox_elements[rNumber].click()
    except:
        try:
            slideBarElement = driver.find_element(By.CLASS_NAME, 'js-facet-group-content')
            driver.execute_script("arguments[0].scrollTop += arguments[0].offsetHeight;", slideBarElement)
            checkbox_elements[rNumber].click()
            sleep(1)
        except:
            print(f"{valueList[rNumber]} not working!")

# Pick any Product
def pickProduct(id):
    sleep(1)
    productList = driver.find_elements(By.CSS_SELECTOR, ".js-facet-product-list .prd a")
    productList[id+1].click()

# Go to product details
def goProductDetails():
    sleep(1)
    element = driver.find_element(By.CLASS_NAME, 'prd-detail-footer')
    scrollElement(element)
    sleep(1)
    element2 = driver.find_element(By.CLASS_NAME, 'catPagesContCenter')
    scrollElement(element2)
                
# Add product to favlist
def addFav():
    element = driver.find_element(By.XPATH,'//*[@id="catPageContent"]/main/div[3]/div[1]/div[2]/div/div[3]/div/div[1]/div/a')
    element.click()

# Login process
def login(email,password):
    scroll_down(100)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys(email)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys(password)
    sleep(1)
    sleep(15)
    driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()

# Add product to basket and go Basket
def buyProduct(): 
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'button.js-btn-detail-basket.js-add-basket').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'a.btn.basket-modal__btn-shipping.font-weight-600.p-10.text-center').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,'button.actionBtn.js-begin-checkout').click()

# Run functions
goFooter()
goCategory(f'[data-label="{randomItem}"]')
scroll_down(300)
pickFilter()
pickProduct(3)
goProductDetails()
addFav()
login(email=email,password=password)
buyProduct()