from selenium import webdriver
import pdb

try:
	#pdb.set_trace()
	driver = webdriver.Firefox(executable_path='./bin/geckodriver.exe')
	variable = input("Enter something or Ctrl+C: ")
	driver.get(variable)
except Exception as e:
	pass
finally:
	# driver.close()
	driver.quit()
