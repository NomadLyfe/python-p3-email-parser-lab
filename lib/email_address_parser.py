import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        regex = re.compile(r'[\s|\,]{1,2}')
        return [email for email in sorted(regex.split(self.email_addresses)) if '@' in email]
