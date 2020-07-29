from selenium import webdriver
from time import sleep
import pyautogui

mensagem = 'Oi amor,te amo. Bjs, Udson <3'
emailfrom = ''
senha = ''
emailto = ''

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(executable_path=r'D:\Programação\Python\Bot de Mensagens para '
                                               r'grupo\chromedriver.exe')

driver.get('https://accounts.google.com/AccountChooser?service=mail&amp;continue=https://mail.google.com/mail/')
login_email = driver.find_element_by_class_name('whsOnd')
login_email.click()
login_email.send_keys(emailfrom)
sleep(2)
envio_email = driver.find_element_by_class_name('VfPpkd-RLmnJb')
envio_email.click()
sleep(5)
for i in senha:
    pyautogui.write(i, interval=0.5)
sleep(2)
envio_senha = driver.find_element_by_class_name('VfPpkd-RLmnJb')
envio_senha.click()
sleep(5)
escrever_email = driver.find_element_by_class_name('z0')
escrever_email.click()
sleep(2)
para = driver.find_element_by_class_name('vO')
para.click()
para.send_keys(emailto)
sleep(2)
pyautogui.press('enter')
sleep(1)
assunto = driver.find_element_by_class_name('aoT')
assunto.click()
sleep(2)
assunto.send_keys('Amor')
envio_da_mensagem = driver.find_element_by_id(':r9')
sleep(2)
envio_da_mensagem.click()
envio_da_mensagem.send_keys(mensagem)
sleep(2)
enviar_mensagem = driver.find_element_by_id(':pu')
enviar_mensagem.click()
