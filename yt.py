from selenium import webdriver


class music():
    def __init__(self):
        self.driver = webdriver.Chrome("/home/the_shinigami/Desktop/chromedriver/chromedriver")
    
    def play(self, query):
        self.query=query
        self.driver.get(url = "https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
        video.click()
        
# assist = music()
# assist.play("gul by anuv jain")