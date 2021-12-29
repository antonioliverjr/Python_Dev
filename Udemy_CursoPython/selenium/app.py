from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class ChromeAuto:
    def __init__(self, *options: str):
        PATH = 'chromedriver.exe'

        self.options = webdriver.ChromeOptions()

        if options is not None:
            for option in options:
                self.options.add_argument(option)

        self.service = Service(
            executable_path=PATH
        )

        self.chrome = webdriver.Chrome(
            service=self.service,
            options=self.options
        )

    def clicar_sing(self):
        try:
            btn_sign = self.chrome.find_element_by_link_text('Sign in')
            btn_sign.click()
        except Exception as e:
            print(e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')

            input_login.send_keys('!!!!!!!!')
            input_password.send_keys('!!!!!!!!!!!!')
            sleep(3)
            input_password.send_keys(Keys.ENTER)
            #btn_login.click()
        except Exception as e:
            print(e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    sleep(3)
    chrome.clicar_sing()
    sleep(3)
    chrome.faz_login()
    sleep(3)
    chrome.sair()
