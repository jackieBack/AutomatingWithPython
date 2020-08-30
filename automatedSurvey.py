from datetime import date
import splinter

url = "http://me2.do/xjNC2vO9"

#my fields
DOB = "960802"
today = date.today()
d1 = today.strftime("%Y%m%d")[2:]
name = "백범준"

browser = splinter.Browser('chrome')
browser.visit(url)

#page1
browser.find_by_text('다음').click()

#page2
browser.find_by_name("AN_1335692").fill(name)
browser.find_by_name("AN_1335693").fill(DOB)
browser.find_by_name("AN_1335747").fill(d1)
browser.find_by_text('다음').click()

#page3
browser.find_by_value("4516907").click()
browser.find_by_value("4516927").click()
browser.find_by_value("4516932").click()
browser.find_by_value("4516937").click()

#end
browser.find_by_text('응답완료').click()
#browser.quit()