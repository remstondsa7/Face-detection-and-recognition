import os
from twilio.rest import Client
account_sid="ACd00a1fe6fe91e58aef029aa803d7e8bb"
auth_token="0d0e44dde69321d88ca901c8be4e587c"
client=Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+919372132643',
                        from_='+12058393604'
                    )

print(call.sid)
