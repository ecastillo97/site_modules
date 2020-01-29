
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

query_string = input('search stuff: ')
options = Options()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", {
    "download.default_directory" : r"/Users/bch4/Desktop/ABC/new dude/modules/new_stuff",
    "download.prompt_for_download" : False,
    "download.directory_upgrade" : True,
    "safebrowsing.enabled" : True
    })
# options.add_argument('--browser.helperApps.neverAsk.saveToDisk=application/pdf')
# options.add_argument('--browser.download.dir=Users/bch4/downloads/em_dl')

driver = Chrome(executable_path = '/Users/bch4/Desktop/ABC/new dude/modules/chromedriver', options = options)
driver.get('https://google.com')
search_form  = driver.find_element_by_name('q')
search_form.send_keys(query_string)
search_form.submit()

# first_elem = driver.find_element_by_class_name('r')
# link = first_elem.get_attribute('href')
# print(link)

# acts = ActionChains(driver).context_click(link).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN)
# acts.perform()

# results = driver.find_elements_by_class_name('r')
# pdf_list = [e for e in results if '[PDF]' in e.text]
# links = [text.find_element_by_xpath('.//a').get_attribute('href') for text in pdf_list]

acts = ActionChains(driver).send_keys(Keys.ALT).send_keys('w')
acts.perform()

# for i in range(len(links)):
#     new_driver = Chrome(executable_path = '/Users/bch4/Desktop/ABC/new dude/modules/chromedriver', options = options)
#     new_driver.get(links[i])

# print(len(links))
