import time

from playwright.sync_api import Page, Playwright, expect
import re
def test_practiceplaywright(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication", exact = True).click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()
    page.locator(".secondary").click()
    expect(page.get_by_text("Login Page")).to_be_visible()

# checkboxes
def test_practice2(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Checkboxes", exact = True).click()
    checkboxes = page.get_by_role("checkbox")
    checkboxes.nth(0).check()
    checkboxes.nth(1).uncheck()
    expect(checkboxes.nth(0)).to_be_checked()
    expect(checkboxes.nth(1)).not_to_be_checked()

# firefox browser
def test_firefoxbrowser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.google.com")


def test_uivalidationscript(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractice/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button", name="Add").click()
    nokiaedge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaedge.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_practice3(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractice/")

    # handle child pages
    with page.expect_popup() as new_page:
        page.locator(".blinkingText").nth(0).click()
        child_page=new_page.value
        text = child_page.locator(".red").text_content()

        #email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text).group()
        #assert email == "mentor@rahulshettyacademy.com"

        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        print(email)
        assert email == 'mentor@rahulshettyacademy.com'

def test_practice4(playwright:Playwright):
    # hide/display , Placeholder
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="hide").click()
    expect(page.get_by_text("Hide Example")).to_be_hidden()

    #handle alerts
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name = "Confirm").click()
    time.sleep(4)

    # hover
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Top").click()



    #handle Frames
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    # table
    page.goto("https://rahulshettyacademy.com/seleniumPractice/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index
            print(f"Price Column Value is : {priceColValue}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(priceColValue)).to_have_text("37")

































