from selenium import webdriver

# open firefox browser
driver = webdriver.Firefox()

driver.get("http://econpy.pythonanywhere.com/ex/001.html")


# find elements by xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# print out all of the buyers and prices of the current page

num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text + " : " + prices[i].text)


driver.close()



