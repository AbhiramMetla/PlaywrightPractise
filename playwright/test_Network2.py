from multiprocessing import context

from playwright.sync_api import Playwright, expect
import time
from utils.apiBase import APIUtils

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a64cd0b85b8849b490ce4f5")

def test_Network2(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("abhi123456789@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Naga@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="   ORDERS").click()
    page.get_by_role("button", name="View").first.click()

    message = page.locator(".blink_me").text_content()
    print(message)
    time.sleep(10)

def test_session_storage(playwright : Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{getToken}' )""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

