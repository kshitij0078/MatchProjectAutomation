from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:7575")
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
driver.get("https://rediff.com")