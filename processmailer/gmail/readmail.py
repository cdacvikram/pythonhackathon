# Read email subject and body.

import logging
from imaplib import IMAP4_SSL
from imaplib import IMAP4

import yaml  # To load saved login credentials from a yaml file

log = logging.getLogger(__name__)

class Gmail:
    def _read_credentials(self, file_name='credentials.yml') -> yaml:
        with open(file_name) as f:
            content = f.read()

        # from credentials.yml import user name and password
        return yaml.load(content, Loader=yaml.FullLoader)

        
    def __init__(self) -> None:
        log.debug("load credentials")
        credentials = self._read_credentials()
        # Load the user name and passwd from yaml file
        self.user = credentials["user"]
        self.password = credentials["password"]
        # URL for IMAP connection
        imap_url = 'imap.gmail.com'

        # Connection with GMAIL using SSL
        self.mail = IMAP4_SSL(imap_url)


    def login(self):
        # Log in using your credentials
        try:
            self.mail.login(self.user, self.password)
            log.debug("Login successful")
        except IMAP4.error as e:
            log.error("Error while logging in %s", e)
            raise e

    def logout(self):
        # Log in using your credentials
        try:
            self.mail.logout()
            log.debug("Logged out successfuly.")
        except IMAP4.error as e:
            log.error("Error while logging in %s", e)
            pass


    def read(self, mailbox='Inbox'):
        # Select the Inbox to fetch messages
        self.login()
        self.mail.select(mailbox, readonly=True)

        _, data = self.mail.search(None, 'UnSeen')  # Search for unred emails
        log.debug("read msgs")
        mail_id_list = data[0].split()  # IDs of all emails that we want to fetch
        log.debug("Total new msgs %s", len(mail_id_list))
        msgs = []  # empty list to capture all messages
        try:
            # Iterate through messages and extract data into the msgs list
            for num in mail_id_list:
                typ, data = self.mail.fetch(num, '(RFC822)')
                msgs.append(data)

        except Exception as e:
            log.error("Error while reading msg %s", e)
            self.logout()
            raise e
        self.logout()
        return msgs

