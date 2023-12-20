# Simulação de testes automatizado para website
# Disciplina de Qualidade de Software e Testes - UEA-2023
# Equipe: Edney F.da Silva, Francisco Junior e Jéssica Tapajós
# Manaus, 14 de dezembro de 2023

import time
import unittest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestWebPage(unittest.TestCase):
    
    browser = Chrome()

    def test_valid_webpage(self):
        
        # CT01 - Acessar website https://www.saucedemo.com/
        self.browser.get('https://www.saucedemo.com/')
        wpage_login = self.browser.find_element(By.CLASS_NAME, 'login_logo').text
        self.assertEqual(wpage_login,'Swag Labs')

        # CT02 - Teste de login com credenciais válidas
        campo_login = self.browser.find_element(By.ID, 'user-name')
        campo_password = self.browser.find_element(By.ID, 'password')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        campo_login.send_keys('standard_user')
        campo_password.send_keys('secret_sauce')
        botao_login.click()
        wpage_products = self.browser.find_element(By.CLASS_NAME, 'title').text
        self.assertEqual(wpage_products,'Products')

        # CT03 - Adição de produto 1 no carrinho
        campo_select_product1 = self.browser.find_element(By.CLASS_NAME, 'inventory_item_label')
        campo_select_product1.click()
        time.sleep(2)
        campo_add_cart1 = self.browser.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light')
        campo_add_cart1.click()
        time.sleep(2)

        # CT04 - Adição de produto 2 no carrinho
        campo_select_product2 = self.browser.find_element(By.CLASS_NAME, 'inventory_item_name')
        campo_select_product2.click()
        time.sleep(2)
        campo_add_cart2 = self.browser.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
        campo_add_cart2.click()
        time.sleep(2)

        # CT05 - Ir para carrinho verificar itens
        campo_go_cart = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
        campo_go_cart.click()
        time.sleep(2) 

        # CT06 - Remove produto 1 do carrinho
        campo_remove_product1 = self.browser.find_element(By.ID, 'remove-sauce-labs-backpack')
        campo_remove_product1.click()
        time.sleep(2)
        

        # CT07 - Finalização da compra
        campo_checkout = self.browser.find_element(By.NAME, 'checkout')
        campo_checkout.click()
        time.sleep(2)
        
        # CT08 - Preencher dados do comprador e clicar em continue
        campo_check_name = self.browser.find_element(By.ID, 'first-name')
        campo_check_name.send_keys('Jonh')
        campo_check_last_name = self.browser.find_element(By.ID, 'last-name')
        campo_check_last_name.send_keys('Paraiba')
        campo_check_zip_code = self.browser.find_element(By.ID, 'postal-code')
        campo_check_zip_code.send_keys('66012-171')
        time.sleep(2)
        botao_checkout = self.browser.find_element(By.ID, 'continue')
        botao_checkout.click()
        time.sleep(2)

        # CT09 - Encerrar compra
        botao_finish = self.browser.find_element(By.ID, 'finish')
        botao_finish.click()
        time.sleep(2)
        botao_home = self.browser.find_element(By.ID, 'back-to-products')
        botao_home.click()
        time.sleep(2)
        
        # CT10 - Open more tabs
        for _ in range(2):
           self.browser.execute_script("window.open('', '_blank');")
        for i in range(1, 3):
            nova_aba = self.browser.window_handles[i]
            self.browser.switch_to.window(nova_aba)
            self.browser.get(f'https://www.saucedemo.com/inventory.html')
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(2)

        # CT11 - Test Icons Social Midia
        click_twitter = self.browser.find_element(By.CLASS_NAME, 'social_twitter')
        click_twitter.click()
        click_facebook = self.browser.find_element(By.CLASS_NAME, 'social_facebook')
        click_facebook.click()
        click_linkedin = self.browser.find_element(By.CLASS_NAME, 'social_linkedin')
        click_linkedin.click()
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(2)

        # CT12 - logout 
        botao_menu = self.browser.find_element(By.ID, 'react-burger-menu-btn')
        botao_menu.click()
        time.sleep(2)
        botao_logout = self.browser.find_element(By.ID, 'logout_sidebar_link')
        botao_logout.click()
        time.sleep(2)
        
        # CT13 - Teste de login com credenciais inválidas
        #campo_login.clear()
        #campo_password.clear()
        campo_login = self.browser.find_element(By.ID, 'user-name')
        campo_password = self.browser.find_element(By.ID, 'password')
        botao_login = self.browser.find_element(By.ID, 'login-button')
        campo_login.send_keys('user_invalid')
        campo_password.send_keys('secret')
        botao_login.click()
        #wpage_test = self.browser.find_element(By.test, 'data_test').text
        #self.assertEqual(wpage_test,'error')
        time.sleep(2)

if __name__ == '__main__':
     unittest.main()     