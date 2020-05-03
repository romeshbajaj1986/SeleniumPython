#Config file is used to contain data which will cjange lile browser / URL Cofig Parser need to be imported
import configparser
def ConfigReadData(section,key):
    #creating obeject of configparser Remember to put pranthis
    config = configparser.ConfigParser()
    # to read file we will give relative path of config file ../ move one folder up
    config.read('./ConfigrationFile/config.cfg')
    #will return value for Key in Section
    return config.get(section,key)

def RegistrationPageData(section,key):
    # creating obeject of configparser Remember to put pranthis
    config = configparser.ConfigParser()
    # to read file we will give relative path of config file ../ move one folder up
    config.read('./ConfigrationFile/register.cfg')
    # will return value for Key in Section
    return config.get(section,key)

def LoginPageData(section,key):
    # creating obeject of configparser Remember to put pranthis
    config = configparser.ConfigParser()
    # to read file we will give relative path of config file ../ move one folder up
    config.read('./ConfigrationFile/Login.cfg')
    # will return value for Key in Section
    return config.get(section,key)

def MyAccountData(section,key):
    config= configparser.ConfigParser()
    config.read('./ConfigrationFile/my_account.cfg')
    return config.get(section,key)
