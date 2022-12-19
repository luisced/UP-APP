from chrome import ChromeBrowser
from login import login
from menu import findScheduleLink


if __name__ == "__main__":
    browser = ChromeBrowser().buildBrowser()
    browser.get("https://up4u.up.edu.mx/user/auth/login")
    print(login(browser))
    print(findScheduleLink(browser))

    # copy the page source to horario.html
    with open("horario.html", "w") as f:
        f.write(browser.page_source)
