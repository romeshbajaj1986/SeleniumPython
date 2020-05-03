#Page Object Model Example
from Library import ReadConfigFile
from Base import InitiateDriver
from Pages import Registration
import pytest
from DataGenrator import DataGen
@pytest.mark.parametrize('data',DataGen.datgenrator())
def test_ABC(data):
    driver = InitiateDriver.StartBrowser()
    objRegistration= Registration.registration(driver)
    objRegistration.username(data[0])
    objRegistration.email(data[1])