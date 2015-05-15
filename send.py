from twilio.rest import TwilioRestClient
from twilio.exceptions import TwilioException
import os, sys

class GroupText:
    # Constructing an instance of GroupText.
    def __init__(self, client, from_num, numbers):
        self.from_num = from_num
        self.client = client
        self.numbers = numbers

    # In an ideal world, were this connected to a web app, would
    # pass a status_callback URL to retrieve status of each text.
    def send_text(self, msg, to_num):
        to_num = "+%s" % to_num
        try: 
            msg_handler = self.client.messages.create(
                to=to_num, from_=self.from_num, 
                body=msg
            )
        except Exception:
            print 'Error sending %s to %s' % (msg, to_num)
        print "Sending \"%s\" to %s" % (msg, to_num)

    # Prompt forever!
    def prompt_msg(self):
        print "Type in a line and we'll send it to everyone on your list!"
        print "Press ENTER to stop texting."
        line = raw_input("> ")
        while line.strip():
            self.group_send(line)
            line = raw_input("> ")

    # Send to a list of phone numbers. TODO: synchro with queues
    def group_send(self, msg):
        for number in self.numbers: self.send_text(msg, number)

def main():
    phone_env_var = 'TWILIO_PHONE_NUMBER'

    # Usage checks
    if len(sys.argv) is not 2: 
        print "Usage: python send.py [numbers.csv]"
        return 1

    phone_no = os.environ.get('TWILIO_PHONE_NUMBER')
    if not phone_no:
        print "Please set %s environment variable:" % phone_env_var
        print "\t$ export %s=\"+15555555555\"" % phone_env_var
        return 1

    try: # read phone numbers file
        with open(sys.argv[1]) as f:
            numbers = f.read().splitlines()
    except Exception as err:
        print err
        return 1

    try: # init Twilio client
        client = TwilioRestClient()
    except TwilioException as err:
        print err # Set environment variables!
        return 1

    instance = GroupText(client, phone_no, numbers)
    instance.prompt_msg()
    return 0

if __name__ == "__main__":
    sys.exit(main())
