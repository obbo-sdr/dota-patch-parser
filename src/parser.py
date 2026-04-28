from Changes import *
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def get_patch():
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Edge(options=options)
    changes = {"Patch" : Patch(),
               "General": GeneralChanges(),
               "NeutralCreeps": NeutralCreepsChanges(),
               "Items": ItemsChanges(),
               "NeutralItems": NeutralItemsChanges(),
               "Heroes": HeroesChanges()}

    try:
        url = "https://dota2.com/patches/7.41b"
        driver.get(url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "lxml")

        update_num = soup.find("div", class_="oyfUTD3R9D883pLDopRL4")
        changes["Patch"].insert_data(update_num.text)

        update = soup.find_all("div", class_="_3n8oLh1MQKLU3OvB6YYdRp rKsLhXLkYn4GGxF5S5hO9")

        for change in update:
            if "Общие изменения" in change.text:
                changes["General"].insert_data(change.get_text(separator='\n'))
            elif "Изменения нейтральных крипов" in change.text:
                changes["NeutralCreeps"].insert_data(change.get_text(separator='\n'))
            elif "Изменения предметов" in change.text:
                changes["Items"].insert_data(change.get_text(separator='\n'))
            elif "Изменения нейтральных предметов" in change.text:
                changes["NeutralItems"].insert_data(change.get_text(separator='\n'))
            elif "Изменения героев" in change.text:
                changes["Heroes"].insert_data(change.get_text(separator='\n'))

        return changes

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


def print_patch(patch):
    for change in patch:
        print(patch[change].get_text())
