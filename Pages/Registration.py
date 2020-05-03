#class for registration Page Creating method for each function
from Library import ReadConfigFile
class registration:
    def __init__(self,obj):
        global driver
        driver = obj

    def username(self,username):
        driver.find_element_by_xpath(ReadConfigFile.RegistrationPageData('Registration', 'MyUserName')).send_keys(
            username)

    def email(self,email):
        driver.find_element_by_name(ReadConfigFile.RegistrationPageData('Registration', 'Email')).send_keys(
            email)
