import re


REGEX = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9]{1,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/=]*)'


class Scanner:

    def __init__(self):
        self.regex_link = REGEX

    def find_all_links(self, text):
        
        matches = []

        for iterator in re.finditer(self.regex_link, text):
            matches.append(iterator.group())

        return matches
