from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


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


def change_css_class_width(classes: list[str], width: int, driver: WebDriver):
    for class_name in classes:
        driver.execute_script(
            f"Array.from(document.getElementsByClassName('{class_name}')).forEach(function(element) {{ element.style.width = '{width}px'; }});"
        )


def change_element_width_by_ids(ids: list[str], width: int, driver: WebDriver):
    for id in ids:
        driver.execute_script(
            f"document.getElementById('{id}').style.width = '{width}px';"
        )


def remove_dom_header_element_and_following_elements(
    header_content: str, driver: WebDriver
):
    js_script = f"""
    let headers = Array.from(document.querySelectorAll('.dsHeader'));
    let targetHeader = headers.find(header => header.textContent.includes("{header_content}"));
    if(!targetHeader) {{
        return;
    }}
    let sibling = targetHeader.nextElementSibling;
    while(sibling && !sibling.classList.contains('dsHeader')) {{
        nextSibling = sibling.nextElementSibling;
        sibling.remove();
        sibling = nextSibling;
    }}
    targetHeader.remove();
    """

    driver.execute_script(js_script)


def remove_dom_header_element_and_following_abilities_elements(
    header_content: str, driver: WebDriver
):
    js_script = f"""
    let headers = Array.from(document.querySelectorAll('.dsHeader'));
    let targetHeader = headers.find(header => header.textContent.includes("{header_content}"));
    if(!targetHeader) {{
        return;
    }}
    let sibling = targetHeader.nextElementSibling;
    while(sibling && !sibling.classList.contains('dsHeader')) {{
        nextSibling = sibling.nextElementSibling;
        if(sibling.classList.contains('dsAbility')) {{
            sibling.remove();
        }}
        sibling = nextSibling;
    }}
    targetHeader.remove();
    """

    driver.execute_script(js_script)


def add_amounts_to_wargear_abilities(
    wargear_amounts: dict[str, int], driver: WebDriver
):

    abilities = driver.find_elements(By.CLASS_NAME, "dsAbility")

    for ability in abilities:

        for wargear, amount in wargear_amounts.items():
            if wargear in ability.text:
                if amount == 0:
                    driver.execute_script("arguments[0].remove()", ability)
                else:
                    driver.execute_script(
                        "arguments[0].innerHTML = arguments[1] + arguments[0].innerHTML;",
                        ability,
                        f'<small><sup><pre style="display: inline">[{amount}x] </pre></sup></small>',
                    )


def add_amounts_to_weapon(weapon_amounts: dict[str, int], driver: WebDriver):
    weapon_row_class = "wTable2_short"

    weapon_rows = driver.find_elements(By.CLASS_NAME, weapon_row_class)

    for weapon_row in weapon_rows:

        is_parent_first_sibling = driver.execute_script(
            """
            return arguments[0].parentElement.previousElementSibling !== null && 
                   arguments[0].parentElement.previousElementSibling.previousElementSibling === null;
        """,
            weapon_row,
        )

        if not is_parent_first_sibling:
            continue

        # For each table, find all span elements within
        span = weapon_row.find_element(By.TAG_NAME, "span")

        span_text = span.text
        # Check if the span's text matches any key in the weapon_amounts dict
        for weapon, amount in weapon_amounts.items():
            if weapon in span_text:

                if amount == 0:
                    driver.execute_script(
                        "arguments[0].parentElement.remove()", weapon_row
                    )
                else:
                    driver.execute_script(
                        "arguments[0].previousElementSibling.innerHTML = arguments[1];",
                        weapon_row,
                        f"<small><sup><pre> [{amount}x]</pre></sup></small>",
                    )


def add_notes(notes: str, driver: WebDriver):
    weapon_table_class = "wTable"
    table_headericon_class = "dsRangedIcon"
    table_header_class = "wTable_WEAPON"

    weapon_table = driver.find_element(By.CLASS_NAME, weapon_table_class)

    js_script = f"""
    var table = arguments[0];
    var notesText = arguments[1];
    
    // Duplicate the first child
    var firstChildClone = table.children[0].cloneNode(true);

    var dsIcon = firstChildClone.querySelector('.{table_headericon_class}');
    if (dsIcon) {{
        dsIcon.remove();
    }}
    var dsHeader = firstChildClone.querySelector('.{table_header_class}');
    if (dsHeader) {{
        dsHeader.children[0].textContent = notesText;
    }}

    // Remove rest of header
    [_, _, ...rest] = firstChildClone.children[0].children;
    rest.forEach(element => element.children[0].innerHTML="&nbsp;");
    
    // Duplicate the third child
    // var thirdChildClone = table.children[2].cloneNode(true);
    notes_row = document.createElement("tr")
    notes_row.appendChild(document.createElement("td"));
    notes_body = document.createElement("td")
    notes_body.colSpan = 6;
    notes_body.innerText = "{notes}";
    notes_row.appendChild(notes_body);

    // Append the modified clones to the table
    firstChildClone.appendChild(notes_row);
    table.appendChild(firstChildClone);
    """

    # Execute the JavaScript with the weapon_table and notes as arguments
    driver.execute_script(js_script, weapon_table, "NOTES")


def set_nickname(nickname: str, driver: WebDriver):
    div_to_copy_class = "dsModelBase2"

    div_to_copy = driver.find_element(By.CLASS_NAME, div_to_copy_class)

    js_script = f"""
    var clone = arguments[0].cloneNode(true);
    clone.innerText = arguments[1];

    arguments[0].parentElement.append(clone);
    """

    driver.execute_script(js_script, div_to_copy, nickname)
