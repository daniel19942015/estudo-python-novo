from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


elementInputLogin = browser.find_element_by_xpath('//*[@id="identifierId"]')
elementInputLogin.send_keys("daniel199257@gmail.com")


elementInputKey = browser.find_element_by_xpath('//*[@id="passwordNext"]')

browser.submit()