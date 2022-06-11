from selenium import webdriver


class google_search():
    def __init__(self):
        self.driver = webdriver.Chrome("/home/the_shinigami/Desktop/chromedriver/chromedriver")

    def google_info(self, query):
        self.query=query
        self.driver.get(url = "https://www.google.com") 
        search = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div/span/svg/path").click()
        enter.click()

