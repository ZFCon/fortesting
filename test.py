from mailjet_rest import Client
import os
api_key = '8dd32ce420e0ab0d45ae5c9d1129d5cb'
api_secret = '75679e436a7c18f1ec0e71ac287e0fb0'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "admin@bigtheory.xyz",
        "Name": "Admin"
      },
      "To": [
        {
          "Email": "lofonil258@oppamail.com",
          "Name": "Ziad"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you! gg",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
