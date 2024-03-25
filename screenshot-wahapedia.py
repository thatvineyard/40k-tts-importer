import os
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image
from Screenshot.Screenshot import Screenshot

from datasheets import ADMECH_DATASHEETS, ADMECH_DATASHEETS_BLACKSTONE_CAMPAIGN, NECRON_DATASHEETS_BLACKSTONE_CAMPAIGN
from dommanipulation import *
from wahapedia import ADMECH_DETACHMENTS, FACTIONS, Datasheet, generate_url

SCREENSHOT_DIRECTORY = "datasheets"
BLACKSTONE_SCREENSHOT_DIRECTORY = f"{SCREENSHOT_DIRECTORY}/blackstone"
MAX_WIDTH=3000
ZOOM=1

Screenshotter=Screenshot()

def screenshot_element(element: WebElement, zoom: float, filepath: str, driver: WebDriver):
    uncropped_filepath = "page_screenshot.png"
    
    location = element.location
    size = element.size

    Screenshotter.full_screenshot(driver, save_path=r'.', image_name=uncropped_filepath)

    x = location["x"] 
    y = location["y"] 
    w = size["width"] * zoom
    h = size["height"] * zoom
    
    left = int(x)
    top  = int(y)
    right = int(x + w)
    bottom = int(y + h)

    im = Image.open(uncropped_filepath)
    im = im.crop((left, top, right, bottom))
    im.save(filepath)
    im = im.rotate(90, expand=True)
    im.save(f"{filepath.split(".")[0]}-rot.png")


def screenshot_datasheet(
    datasheet: Datasheet, zoom: float, screenshot_directory: str, driver: WebDriver
):
    url = generate_url(datasheet)

    print(f"Getting datasheet for {datasheet.name} at url {url}")

    driver.get(url)

    # get rid of cookie bar
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ez-accept-all"))
        )
        accept_cookies_button = driver.find_element(By.ID, "ez-accept-all")
        accept_cookies_button.click()
    except:
        pass

    # select detatchment
    if datasheet.faction == FACTIONS.ADMECH:
        detachment = ADMECH_DETACHMENTS.EXPLORATOR_MANIPLE.value
        detachment_selector = Select(driver.find_element(By.CLASS_NAME, "FilterSelectAM"))

    if datasheet.faction == FACTIONS.NECRON:
        detachment = 1
        detachment_selector = Select(driver.find_element(By.CLASS_NAME, "FilterSelectNE"))

    detachment_selector.select_by_index(detachment)

    # remove strategemens, detatchment ability and enhancements, icons and unit composition 
    remove_dom_element_by_class(["ShowDatasheetFeatures"], driver)
    remove_dom_element_by_class(["dsIconsWide"], driver)
    remove_dom_header_element_and_following_abilities_elements(
        "UNIT COMPOSITION", driver
    )
    remove_dom_header_element_and_following_abilities_elements("LEADER", driver)
    remove_dom_header_element_and_following_abilities_elements(
        "SUPREME COMMANDER", driver
    )

    # Add new things
    if datasheet.nickname:
        set_nickname(datasheet.nickname, driver)

    if datasheet.notes:
        add_notes(datasheet.notes, driver)

    if len(datasheet.weapon_amounts) > 0:
        add_amounts_to_weapon(datasheet.weapon_amounts, driver)

    if len(datasheet.weapon_amounts) > 0:
        add_amounts_to_wargear_abilities(datasheet.wargear_amounts, driver)

    if len(datasheet.weapon_amounts) > 0 and len(datasheet.weapon_amounts) > 0:
        remove_dom_header_element_and_following_elements("WARGEAR OPTIONS", driver)
    

    # Remove ads and popups
    wait_and_remove_element((By.ID, "ezmobfooter"), driver, timeout=5)
    wait_and_remove_element((By.TAG_NAME, "ins"), driver, timeout=5)

    # Zoom in 
    # driver.execute_script("document.body.style.width = document.body.style.width * arguments[0]", zoom)
    driver.execute_script("document.body.style.zoom = arguments[0]", zoom)

    # Take screenshot
    element = driver.find_element(By.ID, "wrapper").find_element(
        By.CLASS_NAME, "datasheet"
    )

    filename = datasheet.name
    if datasheet.nickname:
        filename += f" ({datasheet.nickname})"

    screenshot_element(element, zoom, f"{screenshot_directory}/{filename}.png", driver)

def screenshot_stratagem(screenshot_directory: str, driver: WebDriver):
    pass

options = ChromeOptions()
options.add_argument(f"--window-size={MAX_WIDTH},1440")
# options.add_argument(f"--force-device-scale-factor={ZOOM}")
# options.add_argument("--kiosk")

driver = Chrome(options=options)

driver.set_window_position(0,0)

if not os.path.exists(SCREENSHOT_DIRECTORY):
    os.makedirs(SCREENSHOT_DIRECTORY)
if not os.path.exists(BLACKSTONE_SCREENSHOT_DIRECTORY):
    os.makedirs(BLACKSTONE_SCREENSHOT_DIRECTORY)

# for detatchment in ADMECH_DETACHMENTS:
#     print(detatchment)

for datasheet in ADMECH_DATASHEETS_BLACKSTONE_CAMPAIGN:
    screenshot_datasheet(datasheet, ZOOM, BLACKSTONE_SCREENSHOT_DIRECTORY, driver)

# for datasheet in ADMECH_DATASHEETS:
#     screenshot_datasheet(datasheet, ZOOM, SCREENSHOT_DIRECTORY, driver)

# for datasheet in NECRON_DATASHEETS_BLACKSTONE_CAMPAIGN:
#     screenshot_datasheet(datasheet, ZOOM, BLACKSTONE_SCREENSHOT_DIRECTORY, driver)
