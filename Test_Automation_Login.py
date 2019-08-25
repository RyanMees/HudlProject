from selenium import webdriver

driver = webdriver.Chrome("C:\Hudl\chromedriver.exe")
driver.get("http://Hudl.com")

driver.find_element_by_link_text('Log in').click()

driver.find_element_by_id("email").send_keys('ryanmees@yahoo.com')
driver.find_element_by_id("password").send_keys('GoBigRed2020')

driver.find_element_by_id("logIn").click()

#Insert wait for page to load here if needed

driver.quit()

#I would also perform automation of the Remember me check box, Need help button,
#Login Help Email and Send Password Reset.  There would also need to be automation
#of Sign up.  Logging cookies would also be considered.


