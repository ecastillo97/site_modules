
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()
##options.headless = True
##assert options.headless
driver = Chrome(executable_path = '/Users/bch4/Desktop/modules/chromedriver', options = options)

query = 'cats'
driver.get('https://www.reddit.com/search/?q=' + query)

results = driver.find_elements_by_class_name('rpBJOHq2PR60pnwJlUyP0')
print(len(results))
for i in range(len(results)):
    print(results[i].text)
