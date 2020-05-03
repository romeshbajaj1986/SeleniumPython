from Library import ReadConfigFile
def test_MultiWindow():
    from Base import InitiateDriver
    driver =InitiateDriver.StartBrowser()
    #above code helps to comment out below code
    # from selenium.webdriver import Chrome
    # path = 'D:\\Python\\chromedriver.exe'
    # driver = Chrome(executable_path=path)
    # driver.get("https://thetestingworld.com/testings/")
    # driver.maximize_window()
    # in below code properties of object is given in config file and it is read with help ReadConfigFile
    driver.find_element_by_xpath(ReadConfigFile.LoginPageData('Login','login')).click()
    driver.find_element_by_name(ReadConfigFile.LoginPageData('Login','UserName')).send_keys('test')
    driver.find_element_by_name(ReadConfigFile.LoginPageData('Login','Password')).send_keys('test')
    driver.find_element_by_xpath(ReadConfigFile.LoginPageData('Login','LoginBtn')).click()
    driver.find_element_by_xpath(ReadConfigFile.MyAccountData('Account','myaccount')).click()
    driver.find_element_by_xpath(ReadConfigFile.MyAccountData('Account', 'delete')).click()
    # for tab also we use window handels a it returns number of tab open in driver
    alltabs = driver.window_handles
    mainwindow = ''
    print(alltabs)
    for win in alltabs:
        driver.switch_to.window(win)
        # using above code we are switching to windows and to identify in which tab we need to perform action we are using current URL with IF
        # we can use driver.title or any other element present on page if URL and Title are Dynamic
        print(driver.current_url)
        if (driver.current_url == "https://thetestingworld.com/testings/manage_customer.php"):
            driver.find_element_by_xpath("//button[text()='Start Download']").click()
            mainwindow = win
        # else:
        #    driver.close()
        # need to move back to main window as controle is on Las window
    driver.switch_to.window(mainwindow)


