import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxb84c63ed74e641ae9958418c948494ac.mailgun.org/messages",
        auth=("api", "68e2f5c9345ae1c1a942acba05462ec7-ed4dc7c4-dd823f29"),
        data={"from": "Excited User <mailgun@sandboxb84c63ed74e641ae9958418c948494ac.mailgun.org>",
              "to": ["jonathanlee.2018@business.smu.edu.sg"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

send_simple_message()
print(send_simple_message())