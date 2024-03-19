from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from PIL import Image

from wahapedia import ADMECH_DATASHEETS, ADMECH_DETACHMENTS, Datasheet, generate_url

def screenshot_element(element, filepath: str, driver: WebDriver):
    uncropped_filepath = "page_screenshot.png"
    location = element.location
    size = element.size

    driver.save_screenshot(uncropped_filepath)

    x = location['x']
    y = location['y']
    w = size['width']
    h = size['height']
    width = x + w
    height = y + h

    im = Image.open(uncropped_filepath)
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(filepath)

def remove_dom_element_by_class(classes: list[str], driver: WebDriver):
    classes = map(lambda x: f"'{x}'", classes)
    js_script = f"""
    const classesToRemove = [{", ".join(classes)}];
    classesToRemove.forEach(cls => {{
        const elementsToRemove = document.querySelectorAll('.' + cls);
        elementsToRemove.forEach(el => el.remove());
    }});
    """
    driver.execute_script(js_script)

def screenshot_datasheet(datasheet: Datasheet, driver: WebDriver):
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

    element = driver.find_element(By.ID, "wrapper").find_element(By.CLASS_NAME, "datasheet")


    screenshot_element(element, f"{datasheet.path}.png", driver)



driver = webdriver.Chrome()

for datasheet in ADMECH_DATASHEETS:
    screenshot_datasheet(datasheet, driver)