import time
from model.credLogin import LoginCred
from random import randrange
import pytest
random = randrange(100000)

@pytest.allure.step("Login with empty fields")
def test_emptyFields(app):
    with pytest.allure.step("Login with empty fields"):
        app.session.login(LoginCred(username="", password=""))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Nickname warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

@pytest.allure.step("Login with empty username field")
def test_emptyUserName(app):
    with pytest.allure.step("Login with empty nickname field"):
        app.session.login(LoginCred(username="", password="TestTest12"))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


@pytest.allure.step("Login with empty password field")
def test_emptyPassword(app):
    with pytest.allure.step("Login with empty password field"):
        app.session.login(LoginCred(username="triced", password=""))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

@pytest.allure.step("Login with not exist username")
def test_loginNotExistUser(app):
    with pytest.allure.step("Login with not exist user by nickname"):
        app.session.login(LoginCred(username="triced" + str(random), password="TestTest12"))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

@pytest.allure.step("Login with dot after nickname")
def test_nickNameWithDoteAfter(app):
    with pytest.allure.step("Login with dot after nickname"):
        app.session.login(LoginCred(username="triced.", password="TestTest12"))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

@pytest.allure.step("Login with dot after email")
def test_emailWithDoteAfter(app):
    with pytest.allure.step("Login with dot after email"):
        app.session.login(LoginCred(username="triced8+3030@gmail.com.", password="TestTest12"))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

@pytest.allure.step("Login with dot before nickname")
def test_nickNameWithDoteBefore(app):
    with pytest.allure.step("Login with dot before nickname"):
        app.session.login(LoginCred(username=".triced", password="TestTest12"))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

@pytest.allure.step("Login with caps password")
def test_loginPasswordCaps(app):
    with pytest.allure.step("Login with caps password"):
        app.session.login(LoginCred(username=".triced", password="TestTest12".upper()))
    with pytest.allure.step("Enter captcha if it visible"):
        app.session.captchaEntering()
    with pytest.allure.step("Password warning message"):
        assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    with pytest.allure.step("Password field's boarder color Assert"):
        assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Login field's boarder color Assert"):
        assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Close login pop-up by close(x) button"):
        app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()
