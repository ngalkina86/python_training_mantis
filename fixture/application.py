from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper



class Application:
    def __init__(self, browser,config):
        if browser == "firefox":
           self.wd = webdriver.Firefox()
        elif browser == "chrome":
           self.wd = webdriver.Chrome()
        elif browser == "ie":
           self.wd = webdriver.Ie()
        else:
            raise ValueError ("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.project = ProjectHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_manage_proj_page(self):
        wd = self.wd
        if not (wd.current_url.endswith('/manage_proj_page.php') and len(wd.find_elements_by_name("width75")) > 0):
           wd.find_element_by_link_text("Manage").click()

    def destroy (self):
        self.wd.quit()

