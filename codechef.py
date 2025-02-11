from playwright.sync_api import sync_playwright

# leetcode_url = "https://leetcode.com/contest"  #Future-use
codechef_url = "https://codechef.com/contests"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  
    page = browser.new_page()
    
    page.goto(codechef_url, wait_until="networkidle")

    with open("codechef.html", "a", encoding="utf-8") as f:
        f.write(page.content())

    browser.close()
