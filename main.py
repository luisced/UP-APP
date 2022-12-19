
import requests
import time
from bs4 import BeautifulSoup


# Set the login URL and method
response = ''
while response == '':
    try:
        response = requests.get("https://up4u.up.edu.mx/user/auth/login")
        # change the terminal color to green and then reset it
        print("\033[92mConnection established ✅ \033[0m")
        time.sleep(2)
        break
    except:
        print("Connection refused by the server..\nLet me sleep for 5 seconds\nZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue
# Parse the HTML of the login response
soup = BeautifulSoup(response.text, 'html.parser')

# Find the login form
login_form = soup.find('form', {'id': 'account-login-form'})
if login_form is not None:
    print("Login form found ✅")
    # change the terminal color to blue and then reset it
    # Find the username and password form fields
    username_field = login_form.find('input', {'name': 'Login[username]'})
    password_field = login_form.find('input', {'name': 'Login[password]'})
    if username_field and password_field:
        print("Username and password fields found ✅")
        # Fill in the login credentials
        username_field['value'] = '0250009'
        password_field['value'] = 'Lu5571967146#'
        # change the terminal color to red and then reset it with loggin in
        print("\033[91mLogging in...\033[0m")
        # Find the submit button
        submit_button = login_form.find(
            'button', {'type': 'submit', 'id': 'login-button'})
        # print the content of the submit button
        if submit_button is not None:
            print("Submit button found ✅")
            print(submit_button)
            # Simulate a click on the submit button
            submit_button.click()
        else:
            print("Submit button not found ❌")
    else:
        print("Username and password fields not found ❌")
else:
    print("Login form not found ❌")
