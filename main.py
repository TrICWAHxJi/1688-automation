import re
import pandas as pd
import asyncio
from playwright.async_api import async_playwright, expect, Page
import random


# Configure the script
chrome_user_data_dir = (
    "C:\\Users\\<Windows user name>\\AppData\\Local\\Google\\Chrome\\User Data"
)
username = "banar_test"
message_frequency_milliseconds = 3000
find_element_timeout_milliseconds = 15000
data_file_path = "products.xlsx"

def get_data_from_xlsx(file_path):
    df = pd.read_excel(file_path, usecols=["Link", "Message"])
    return df


data = get_data_from_xlsx(data_file_path)

processed_links = set()
try:
    with open("processed_links.txt", "r") as f:
        processed_links.update(line.strip() for line in f)
except FileNotFoundError:
    pass


async def process_row(page: Page, row):
    link = row["Link"]
    message = row["Message"]

    if link in processed_links:
        print("Link already processed:", link)
        return

    await page.wait_for_timeout(random.randint(1000, 3000))

    await page.goto(link, wait_until="domcontentloaded")

    async with page.expect_popup() as shop_page_info:
        await page.locator("#shopNavigation").get_by_text("客服").first.click()
    shop_page = await shop_page_info.value

    iframe = shop_page.locator("#ice-container iframe").content_frame

    chat_target = iframe.locator("div.conversation-list div.conversation-item.active")
    await expect(chat_target).to_be_visible(timeout=find_element_timeout_milliseconds)

    input_area = (
        iframe.locator("div")
        .filter(
            has_text=re.compile(
                r"^截图快捷短语0 / 500请输入消息，按Enter键 或 点击发送按钮发送$"
            )
        )
        .locator("pre")
    )
    await input_area.click()
    await input_area.type(message)

    await (
        iframe.locator("div")
        .filter(has_text=re.compile(rf"^{re.escape(message)}$"))
        .locator("pre")
        .press("Enter")
    )

    await shop_page.wait_for_timeout(1000)

    await shop_page.close()

    processed_links.add(link)

    print("Processed link:", link)

    await page.wait_for_timeout(
        message_frequency_milliseconds + random.randint(-1000, 1000)
    )


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            channel="chrome",
            user_data_dir=chrome_user_data_dir,
            headless=False,
            args=["--start-maximized", "--new-window", "--disable-extensions"],
            no_viewport=True,
        )

        page = await browser.new_page()

        await page.goto("https://1688.com", wait_until="domcontentloaded")
        await expect(
            page.get_by_text(username).first, "User not logged in"
        ).to_be_visible(timeout=find_element_timeout_milliseconds)

        print("User logged in")

        for _, row in data.iterrows():
            await process_row(page, row)

        await page.close()

        await browser.close()


async def main():
    try:
        await run()
    except Exception as e:
        print(e)
    finally:
        with open("processed_links.txt", "w") as f:
            f.write("\n".join(processed_links))


if __name__ == "__main__":
    asyncio.run(main())
