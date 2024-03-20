import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image

from datasheets import ADMECH_DATASHEETS, ADMECH_DATASHEETS_BLACKSTONE_CAMPAIGN
from dommanipulation import *
from wahapedia import ADMECH_DETACHMENTS, Datasheet, generate_url

SCREENSHOT_DIRECTORY = "datasheets"
BLACKSTONE_SCREENSHOT_DIRECTORY = f"{SCREENSHOT_DIRECTORY}/blackstone"


def screenshot_element(element, filepath: str, driver: WebDriver):
    uncropped_filepath = "page_screenshot.png"
    location = element.location
    size = element.size

    driver.save_screenshot(uncropped_filepath)

    x = location["x"]
    y = location["y"]
    w = size["width"]
    h = size["height"]
    width = x + w
    height = y + h

    im = Image.open(uncropped_filepath)
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(filepath)


def screenshot_datasheet(
    datasheet: Datasheet, screenshot_directory: str, driver: WebDriver
):
    url = generate_url(datasheet)

    print(f"Getting datasheet for {datasheet.name} at url {url}")

    driver.get(url)

    # get rid of cookie bar
    try:
        accept_cookies_button = driver.find_element(By.ID, "ez-accept-all")
        accept_cookies_button.click()
    except:
        pass

    # select detatchment
    detachment = ADMECH_DETACHMENTS.EXPLORATOR_MANIPLE
    detachment_selector = Select(driver.find_element(By.CLASS_NAME, "FilterSelectAM"))
    detachment_selector.select_by_index(detachment.value)

    remove_dom_element_by_class(["ShowDatasheetFeatures"], driver)
    remove_dom_element_by_class(["dsIconsWide"], driver)
    remove_dom_header_element_and_following_abilities_elements(
        "UNIT COMPOSITION", driver
    )
    remove_dom_header_element_and_following_abilities_elements("LEADER", driver)
    remove_dom_header_element_and_following_abilities_elements(
        "SUPREME COMMANDER", driver
    )

    filename = datasheet.name

    if datasheet.nickname:
        set_nickname(datasheet.nickname, driver)
        filename += f" ({datasheet.nickname})"

    if datasheet.notes:
        add_notes(datasheet.notes, driver)

    if len(datasheet.weapon_amounts) > 0:
        add_amounts_to_weapon(datasheet.weapon_amounts, driver)

    if len(datasheet.weapon_amounts) > 0:
        add_amounts_to_wargear_abilities(datasheet.wargear_amounts, driver)

    if len(datasheet.weapon_amounts) > 0 and len(datasheet.weapon_amounts) > 0:
        remove_dom_header_element_and_following_elements("WARGEAR OPTIONS", driver)

    element = driver.find_element(By.ID, "wrapper").find_element(
        By.CLASS_NAME, "datasheet"
    )

    screenshot_element(element, f"{screenshot_directory}/{filename}.png", driver)


driver = webdriver.Chrome()

if not os.path.exists(SCREENSHOT_DIRECTORY):
    os.makedirs(SCREENSHOT_DIRECTORY)
if not os.path.exists(BLACKSTONE_SCREENSHOT_DIRECTORY):
    os.makedirs(BLACKSTONE_SCREENSHOT_DIRECTORY)

for datasheet in ADMECH_DATASHEETS_BLACKSTONE_CAMPAIGN:
    screenshot_datasheet(datasheet, BLACKSTONE_SCREENSHOT_DIRECTORY, driver)

for datasheet in ADMECH_DATASHEETS:
    screenshot_datasheet(datasheet, SCREENSHOT_DIRECTORY, driver)
