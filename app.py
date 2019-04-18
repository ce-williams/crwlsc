import csv
from selenium import webdriver

# number of pages for results
MAX_PAGE_NUM = 5
# number of digits in url
MAX_PAGE_DIG = 3

driver = webdriver.Firefox()

# create columns for buyers and sellers in csv
with open('results.csv', 'w') as f:
    f.write("Buyer, Price \n")

# loop through page num to append to URL
for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

    driver.get(url)

    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    
    # write to results to csv 
    num_page_items = len(buyers)
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")

# end program
driver.close()