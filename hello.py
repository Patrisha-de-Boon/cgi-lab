#!/usr/bin/env python3
import templates
import cgi
import secret
import os
# import json

# Print environment as json
# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

# Print query parameter data in html
# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ.get('QUERY_STRING')}</p>")

# Print browser data in html
# print("Content-Type: text/html")
# print()
# print(f"<p>HTTP_USER_AGENT={os.environ.get('HTTP_USER_AGENT')}</p>")

USER_COOKIE = "user=" + secret.username
PASS_COOKIE = "pass=" + secret.password

cookie_string = os.environ.get('HTTP_COOKIE')
if (cookie_string and USER_COOKIE in cookie_string and PASS_COOKIE in cookie_string):
    print(templates.secret_page(secret.username, secret.password))
else:
    fieldStorage = cgi.FieldStorage()
    if (fieldStorage and fieldStorage['username'] and fieldStorage['password']):
        username = fieldStorage['username'].value
        password = fieldStorage['password'].value
        print('Set-Cookie: user=' + username)
        print('Set-Cookie: pass=' + password)
        if (username == secret.username and password == secret.password):
            isLoggedIn = True
        else:
            print(templates.after_login_incorrect())
    else:
        print(templates.login_page())

print()