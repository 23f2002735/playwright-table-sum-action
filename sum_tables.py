from playwright.sync_api import sync_playwright

seeds = range(35, 45)

def get_total():
    total = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for s in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={s}"
            page.goto(url)
            nums = page.locator("td").all_inner_texts()
            total += sum(int(x) for x in nums)

        browser.close()
    return total

if __name__ == "__main__":
    print(get_total())
