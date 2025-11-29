import asyncio
from utils import get_username, get_verification_code
import time
from browser_manager import AsyncBrowserManager


async def sign_up(page, username, password):
    await page.goto("https://www.youporn.com/", wait_until="networkidle")

    try:
        age_button = page.locator("#accessButton")
        await age_button.click()
    except:
        print("Age confirmation button not found or already handled.")

    await page.wait_for_selector("#cookie_consent_wrapper", timeout=10000)
    print("Cookie wrapper detected.")

    await page.evaluate(
        """
        document.querySelectorAll('*').forEach(el => {
            if (getComputedStyle(el).zIndex > 1000) {
                el.style.pointerEvents = 'none'
            }
        })
    """
    )
    print("Overlay click-blockers disabled.")

    await page.evaluate(
        """
        const btn = document.querySelector('#consent_accept_all')
        if (btn) {
            btn.click()
        } else {
            console.log("Cookie button not found")
        }
    """
    )
    print("Cookie consent accepted via JS.")

    await page.goto("https://www.youporn.com/register")

    email_input = page.locator("#registration_email")
    await email_input.wait_for(state="visible")
    await email_input.fill(username)

    password_input = page.locator("#registration_password")
    await password_input.wait_for(state="visible")
    await password_input.fill(password)

    # signup_btn = page.locator(".btnSignup")
    # await signup_btn.click()

    # await page.wait_for_load_state("networkidle")

    # try:
    #     tos_button = page.locator("#tos_got_it_btn")
    #     await tos_button.wait_for(state="visible", timeout=10000)
    #     await tos_button.click()
    #     print("TOS accepted!")
    # except Exception:
    #     print("TOS button not found or already accepted.")

    # verification_wrapper = page.locator(".email-verification-form")
    # try:
    #     await verification_wrapper.wait_for(state="visible", timeout=15000)

    #     await page.evaluate("""
    #         const overlay = document.querySelector('#emailVerificationBg');
    #         if (overlay) {
    #             overlay.style.pointerEvents = 'none';
    #         }
    #     """)
    #     print("Email verification overlay disabled.")

    #     code = await get_verification_code(username.split("@")[0])
    #     print(f"Verification code received: {code}")

    #     await page.evaluate(f"""
    #     (() => {{
    #         const code = '{code}';
    #         for (let i = 0; i < code.length; i++) {{
    #             const input = document.querySelector('#emailCode_' + (i+1));
    #             if (input) {{
    #                 input.value = code[i];
    #                 // Dispatch input & change events so JS validator sees it
    #                 input.dispatchEvent(new Event('input', {{ bubbles: true }}));
    #                 input.dispatchEvent(new Event('change', {{ bubbles: true }}));
    #             }}
    #         }}
    #     }})()
    #     """)

    #     await page.wait_for_load_state("networkidle")
    #     print("Account verified successfully.")

    #     return username
    # except Exception as e:
    #     print("Verification step failed or not required.", e)

    # input("Press ENTER to close...")


async def sign_in(page, username, password):
    await page.goto("https://www.youporn.com/", wait_until="networkidle")

    try:
        age_button = page.locator("#accessButton")
        await age_button.click()
    except:
        print("Age confirmation button not found or already handled.")

    await page.wait_for_selector("#cookie_consent_wrapper", timeout=10000)
    print("Cookie wrapper detected.")

    await page.evaluate(
        """
        document.querySelectorAll('*').forEach(el => {
            if (getComputedStyle(el).zIndex > 1000) {
                el.style.pointerEvents = 'none'
            }
        })
    """
    )
    print("Overlay click-blockers disabled.")

    await page.evaluate(
        """
        const btn = document.querySelector('#consent_accept_all')
        if (btn) {
            btn.click()
        } else {
            console.log("Cookie button not found")
        }
    """
    )
    print("Cookie consent accepted via JS.")

    await page.goto("https://www.youporn.com/login")

    email_input = page.locator("#js_username_input")
    await email_input.type(username, delay=100)

    password_input = page.locator("#js_password_input")
    await password_input.type(password, delay=100)

    signup_btn = page.locator("#js_login_btn")
    await signup_btn.click()

    await page.wait_for_load_state("networkidle")

    try:
        tos_button = page.locator("#tos_got_it_btn")
        await tos_button.wait_for(state="visible", timeout=10000)
        await tos_button.click()
        print("TOS accepted!")
    except Exception:
        print("TOS button not found or already accepted.")

    profile_btn = page.locator("#header_user_avatar")
    await profile_btn.click()

    await page.wait_for_load_state("networkidle")


async def main():
    username = await get_username()
    password = "SecretPassword123!"
    async with AsyncBrowserManager(headless=False) as page:
        username = await sign_up(page, username, password)
        if not username:
            print("Sign-up failed, skipping further actions.")
            username = f"None_{int(time.time())}"
            time.sleep(5)
        print(f"Account created: {username} | {password}")

        # async with AsyncBrowserManager(headless=False) as page:
        #     await sign_in(page, username, password)

        screenshot_path = f"screenshots/{username}_screenshot.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")


async def runner():
    await main()


if __name__ == "__main__":
    asyncio.run(runner())
