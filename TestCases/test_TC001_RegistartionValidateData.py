from Library import ReadConfigFile
def testValidateRegistration():
    #we need to import InitiateDriverFile to call Start Broser Function Import path start from project level
    from Base import InitiateDriver
    #Base is not a package it is folder and to treat as a package we need to create a test.py file in Base folder
    #calling StartBrowser it will return object for driver and storing in driver
    driver = InitiateDriver.StartBrowser()
    #inserting value in user Name
    #Xpath is read from register config file
    # driver.find_element_by_xpath("//input[@placeholder='myusername']").send_keys("HelloWorld")
    driver.find_element_by_xpath(ReadConfigFile.RegistrationPageData('Registration','MyUserName')).send_keys("HelloWorld")
    #Calling Close Browser
    InitiateDriver.CloseBrowser()