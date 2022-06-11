from selenium import webdriver


# driver = webdriver.Chrome("/home/the_shinigami/Desktop/chromedriver/chromedriver")
# driver.get("https://lovelocal.in")

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome("/home/the_shinigami/Desktop/chromedriver/chromedriver")

    def get_info(self, query):
        self.query=query
        self.driver.get(url = "https://www.wikipedia.org") 
        search = self.driver.find_element_by_xpath("/html/body/div[3]/form/fieldset/div/input")
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath("/html/body/div[3]/form/fieldset/button/i").click()
        enter.click()

