import logging
import email
import re
from src.processmailer.gmail.readmail import Gmail

log = logging.getLogger(__name__)

class ProcessMessages:
    def __init__(self):
        self.mailboxes = {
            'gmail': {
                'mail_client': Gmail(),
                'msgs': ''
                }
            }
    def _get_messages(self):
        log.debug("Reading messages")
        for mlbox in self.mailboxes:
            ml_client=self.mailboxes[mlbox]['mail_client']
            msgs = ml_client.read()
            self.mailboxes[mlbox]['msgs'] = msgs
            
            
    def processMessages(self):
        self._get_messages()
        for mlbox in self.mailboxes:
            #try:
            file_path = "parameters.txt"
            # Read the contents of the file
            with open(file_path, "r") as file:
                content = file.read()
            # Process the parameters
            parameters = content.split()

            for msg in self.mailboxes[mlbox]['msgs'][::-1]:
                log.debug("Processing msg %s", msg[0][0])
                for response_part in msg:
                    if type(response_part) is tuple:
                        my_msg = email.message_from_bytes((response_part[1]))
                        print("_________________________________________")
                        print("subj:", my_msg['subject'])
                        print("from:", my_msg['from'])
                        print("body:")
                        for part in my_msg.walk():
                            if part.get_content_type() == 'text/html':
                                emailBody = str(part.get_payload())
                                for parameter in parameters:
                                    if(re.search(parameter, emailBody)):
                                        print(parameter + " found in email body")
                                    else:
                                        print(parameter + " not found in email body")
                                print(emailBody)
        return self.mailboxes
