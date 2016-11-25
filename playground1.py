from twilio.rest import TwilioRestClient

account_sid = "AC73bba1b06c86bc729411ba072a203f2f"
auth_token = "d94f0b9fcb3905e41e8ba37414e41dd6"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to = "+13232441030",
    from_ = "+18722216797")

print(message.sid)