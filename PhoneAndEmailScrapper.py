import re, pyperclip

def createPhoneRegex():
    phoneRegex = re.compile(r'''
    # possible combination: 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    (
    ((\d\d\d) | (\(\d\d\d\)))?  #area code (optional)
    (\s|\-)                     #first separator
    \d\d\d                      #first 3 digits
    -                           #separator
    \d\d\d\d                    #last 4 digits
    (((ext(\.)?\s)|x)           #extension number-part (optional)
    (\d{2,5}))?                 #extention (optional)
    )
    ''', re.VERBOSE)            #verbose mode allow us to put in comments, new line and spaces

    return phoneRegex

def createEmailRegex():
    emailRegex = re.compile(r'''
    #possible combination some.+thing@something.com
    [a-zA-Z0-9_.+]+     #possible character appear in name part. a to z, A to Z, 0 to 9, _.+
    @                   # alias symbol
    [a-zA-Z0-9_.+]+     #domain name part
    ''', re.VERBOSE)

    return emailRegex

#3.Get the text off the clipboard. CTRL+C the whole pdf, content is now in the clipboard
#text_Pyper = pyperclip.paste()
#Extract the email/phone from this text
class extraction:
    # def __init__(self, userEntryPath):
    #     self.userEntryPath = ''
    #     self.saveResults = ''
    #     self.saveResultsName = ''
    #     self.extractedPhone = ''
    #     self.extractedEmail = ''
    #     self.readError = ''

    def extractContent(self, userEntryPath):
        try:
            self.openContent = open(userEntryPath, encoding="utf8")
            try:
                self.content = self.openContent.read()
            except:
                self.readError = 'Error: Can\'t read file'
            else:
                self.openContent.close()
        except:
            self.openError = 'Error: Can\'t open file'
        else:
            self.extractedPhone = createPhoneRegex().findall(self.content)
            self.extractedEmail = createEmailRegex().findall(self.content)

        self.allPhoneNumbers = []
        for self.phoneNumbers in self.extractedPhone:
            self.allPhoneNumbers.append(self.phoneNumbers[0])  # 1st string from the tuple

        # we can remove the annoying ' ' in the allPhoneNumbers list by using join and make it nice new line
        self.results = '\n'.join(self.allPhoneNumbers) + '\n' + '\n'.join(self.extractedEmail)
        # pyperclip.copy(results) #pyperclip technique

        try:
            self.saveResults = open('PhoneNoAndEmail_RESULT.txt', 'w')
            try:
                self.saveResults.write(self.results)
            except:
                self.saveWriteError = 'Error: Can\'t write results into file'
            else:
                #self.saveResultsName = self.saveResults.name
                self.saveResults.close()
        except:
            self.saveOpenError = 'Error: Can\'t create and write file'

        return self.readError, self.openError, self.saveWriteError, self.saveOpenError



