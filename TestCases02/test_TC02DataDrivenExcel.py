#Page Object Model Example
from Library import ReadConfigFile
from Base import InitiateDriver
from Pages import Registration
import pytest
import openpyexcel
def datgenrator():
    wk = openpyexcel.load_workbook("D:/Python/dataTC2.xlsx")
    sh= wk['Sheet1']
    r = sh.max_row
    li=[]
    li1=[]
    for i in range(1,r+1):
        li1=[]
        un =sh.cell(i,1)
        pw = sh.cell(i,2)
        li1.insert(0,un.value)
        li1.insert(1,pw.value)
        li.insert(i-1,li1)
    #li= [['user1','user1@gmail.com'],['user2','user2@gmail.com'],['user3','user3@gmail.com']]
    print(li)
    return li

@pytest.mark.parametrize('data',datgenrator())
def test_ABC(data):
    driver = InitiateDriver.StartBrowser()
    objRegistration= Registration.registration(driver)
    objRegistration.username(data[0])
    objRegistration.email(data[1])