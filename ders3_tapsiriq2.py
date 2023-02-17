from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime as dt

def get_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver_path= "C:\\Users\\isgen\\Downloads\\python_otomasyon\\chromedriver.exe"
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(40)
    driver.maximize_window()
    url = "http://automated.pythonanywhere.com"
    driver.get(url)
    return driver

def clean_text(teaxt):
    axir = float(teaxt.split(": ")[1])
    return axir

def write_file(text):
    filename= F"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    while True:
        sleep(10)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)

print(main())