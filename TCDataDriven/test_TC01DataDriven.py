#Page Object Model Example
from Library import ReadConfigFile
from Base import InitiateDriver
from Pages import Registration
import pytest
def datgenrator():
    li= [['user1','user1@gmail.com'],['user2','user2@gmail.com'],['user3','user3@gmail.com']]
    return li

@pytest.mark.parametrize('data',datgenrator())
def test_DataDrivenA(data):
    driver = InitiateDriver.StartBrowser()
    objRegistration= Registration.registration(driver)
    objRegistration.username(data[0])
    objRegistration.email(data[1])