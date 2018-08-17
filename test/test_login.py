import time
from model.credLogin import LoginCred
from random import randrange
import pytest
random = randrange(100000)

@pytest.allure.step("Login with NickName")
def test_loginNick(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Login with nickname"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    with pytest.allure.step("Assert to number of cash button"):
        assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    with pytest.allure.step("Ensure Login"):
        app.session.ensureLogin(username="triced")
    with pytest.allure.step("Logout"):
        app.session.logout()

@pytest.allure.step("Login with space after NickName")
def test_loginNickSpaceAfter(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Login with space after nickname"):
        app.session.login(LoginCred(username="triced ", password="TestTest12"))
    with pytest.allure.step("Assert to number of cash button"):
        assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    with pytest.allure.step("Ensure Login"):
        app.session.ensureLogin(username="triced")
    with pytest.allure.step("Logout"):
        app.session.logout()

@pytest.allure.step("Login with space before NickName")
def test_loginNickSpaceBefore(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Login with space before nickname"):
        app.session.login(LoginCred(username=" triced", password="TestTest12"))
    with pytest.allure.step("Assert to number of cash button"):
        assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    with pytest.allure.step("Ensure Login"):
        app.session.ensureLogin(username="triced")
    with pytest.allure.step("Logout"):
        app.session.logout()

@pytest.allure.step("Login with Email")
def test_loginEmail(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Login with email"):
        app.session.login(LoginCred(username="triced8+3030@gmail.com", password="TestTest12"))
    with pytest.allure.step("Assert to number of cash button"):
        assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    with pytest.allure.step("Ensure Login"):
        app.session.ensureLogin(username="tricedu")
    with pytest.allure.step("Logout"):
        app.session.logout()

@pytest.allure.step("Login with Email Caps")
def test_loginEmailCaps(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Login with email Caps"):
        app.session.login(LoginCred(username="triced8+3030@gmail.com".upper(), password="TestTest12"))
    with pytest.allure.step("Assert to number of cash button"):
        assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    with pytest.allure.step("Ensure Login"):
        app.session.ensureLogin(username="tricedu")
    with pytest.allure.step("Logout"):
        app.session.logout()

@pytest.allure.step("Login with NuckName Caps")
def test_loginNickCaps(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Login with nickname Caps"):
        app.session.login(LoginCred(username="tricedu".upper(), password="TestTest12"))
    with pytest.allure.step("Assert to number of cash button"):
        assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    with pytest.allure.step("Ensure Login"):
        app.session.ensureLogin(username="tricedu")
    with pytest.allure.step("Logout"):
        app.session.logout()

@pytest.allure.step("Close Login pop-up by click outside")
def test_closeOutside(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Open Login pop-up"):
        app.session.openLoginPopup()
    with pytest.allure.step("Click outside pop-up"):
        app.session.clickOutSide()
    with pytest.allure.step("Sign In button is not at the page"):
        assert not app.session.elementIsDisplay("//form[@action='/login/']//div[@class='modala-button__text']")

@pytest.allure.step("See password button")
def test_seePasword(app):
    with pytest.allure.step("Open main page"):
        app.pages.openMainPage()
    with pytest.allure.step("Fill fields with correct data"):
        app.session.fillFieldsSeePasword(LoginCred(username="triced", password="TestTest12"))
    with pytest.allure.step("Password is visible"):
        assert app.warning.getValue(xpath="(//input[@name='password'])[2]") == "TestTest12"

#def test_openadmin(app):
#    app.session.login(LoginCred(username="tricedu", password="TestTest12"))
#    time.sleep(0.1)
#    app.admin.open()
