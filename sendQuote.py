from twilio.rest import Client
import os, requests

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)

r = requests.get("http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote")
quote = r.json()['starWarsQuote']



message = client.messages.create(
         body=quote,
         from_=os.environ['TWILIO_PHONENUM'],
         to=os.environ['MY_PHONENUM']
     )
