
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
assert options.headless
driver = Chrome(executable_path = '/Users/bch4/Desktop/modules/chromedriver', options = options)

def search(query: str, element_id: str) -> None:
    search_form = driver.find_element_by_id(element_id)
    search_form.send_keys(query)
    search_form.submit()

def get_result() -> 'results':
    results = driver.find_elements_by_class_name('result')
    return results
    
driver.get('https://duckduckgo.com')

search('reddit', 'search_form_input_homepage')
##print(get_result()[3].text)
##res = [i.text for i in get_result()]
##print(res)
get_result()[0].click()
search('arch linux', 'header-search-bar')
res = driver.find_elements_by_class_name('rpBJOHq2PR60pnwJlUyP0')
print(len(res))



##driver.get_screenshot_as_file('/Users/bch4/bin/oh my.png')

driver.quit()

##opts = Options()
##opts.headless = True
##assert opts.headless
##driver = Chrome(options = opts)
##driver.get('https://duckduckgo.com')
