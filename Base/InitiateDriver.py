from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ReadConfigFile  # Inporting config file from Library Folder
def StartBrowser():
    global driver #we are making driver object as globel so can be used in any method of the file
    #driver Type is read from config file
    if ReadConfigFile.ConfigReadData('Details','Browser')=='Chrome':
        # Path of chrome driver EXE
        #Pickink fro Drivers Folder of prject
        path = './Drivers/chromedriver.exe'
        #path = 'D:\\Python\\chromedriver.exe'
        driver = Chrome(executable_path=path)
    elif ReadConfigFile.ConfigReadData('Details','Browser')=='Firefox':
        #issue with GekoDriver
        path = './Drivers/geckodriver.exe'
        #path = 'D:\\Python\\geckodriver.exe'
        driver = Firefox(executable_path=path)
    else:
        path = './Drivers/chromedriver.exe'
        #path = 'D:\\Python\\chromedriver.exe'
        driver = Chrome(executable_path=path)
    # Launch URL
    #Getting URL Value from Config file
    driver.get(ReadConfigFile.ConfigReadData('Details','Application_URL'))
    # Maximize Browser
    driver.maximize_window()
    # Working with Text Box
    return driver # we are returning the object of chrom driver

#Method to close driver
def CloseBrowser():
    driver.close()