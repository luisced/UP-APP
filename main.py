from login import login
from chrome import ChromeBrowser


if __name__ == "__main__":
    browser = ChromeBrowser().buildBrowser()
    browser.get("https://up4u.up.edu.mx/user/auth/login")
    print(login(browser))
    browser.close()

    # copy the page source to horario.html
    with open("horario.html", "w") as f:
        f.write(browser.page_source)
