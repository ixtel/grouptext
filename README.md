GROUPTEXT
---
Simple group-messaging utility written in Python! Synchronous texting to be available in an imminent update. Install the twilio modules for python with `pip install twilio`. Make sure to also set the following environment variables:
```
$ export TWILIO_ACCOUNT_SID=XXXX...
$ export TWILIO_AUTH_TOKEN=XXXX...
$ export TWILIO_PHONE_NUMBER=+15555555555
```
And assuming a well-formatted numbers.csv (a phone number per line), you can run
```
$ python send.py numbers.csv
```

