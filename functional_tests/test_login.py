from .base import FunctionalTest
import time
from selenium.webdriver.support.ui import WebDriverWait


test_e = 'adrian186192@personatestuser.org' # V3oJlemAhICwloAa


class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 10
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')
        
    def test_login_with_persona(self):
        #Edith goes to awesome superlist site
        #and notices a "Sigin in" link for the first time
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        #Persona login box appears
        self.switch_to_new_window('Mozilla Persona')

        #Edith logs in with her email address
        self.browser.find_element_by_id('authentication_email').send_keys(test_e)
        self.browser.find_element_by_tag_name('button').click()

        #The Persona window closes
        self.switch_to_new_window('To-Do')

        #She can see that she is logged in
        self.wait_to_be_logged_in(email=test_e)

        #Refreshing the page, she sees its a real session login,
        #not just a one-off for that page
        self.browser.refresh()
        self.wait_to_be_logged_in(email=test_e)

        #Terrified of this new feature, she reflexively clicks "logout"
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=test_e)

        #The "logged out" status also persists after a refresh
        self.browser.refresh()
        
        self.wait_to_be_logged_out(email=test_e)