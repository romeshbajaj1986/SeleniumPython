#Page Object Model Example
from Library import ReadConfigFile
from Base import InitiateDriver
from Pages import Registration
def test_pomregistration():
    driver = InitiateDriver.StartBrowser()
    objRegistration= Registration.registration(driver)
    objRegistration.username('romesh')
    objRegistration.email('romesh.bajaj@gmail.com')