from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'chromedriver.exe')

browser.get("https://www.linkedin.com/login")

input_email = browser.find_element_by_id("username")
input_email.send_keys('antoniobatistajr@gmail.com')

input_senha = browser.find_element_by_id("password")
input_senha.send_keys('Antjr@1986')

btn_login = browser.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

busca = browser.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca.send_keys("Backend")
busca.send_keys(Keys.RETURN)

time.sleep(10)

filtro_vagas = browser.find_element_by_xpath("//button[@aria-label='Vagas']")
filtro_vagas.click()

time.sleep(10)

vagas_title = browser.find_element_by_class_name("disabled.ember-view.job-card-container__link.job-card-list__title")
print(vagas_title)
#vagas_company = browser.find_element_by_class_name("job-card-container__company-name")

#for title in vagas_title:
#    print(title)

input('')