from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Firefox(executable_path ='./geckodriver')
    context.driver.implicitly_wait(30)
def after_all(context):
    context.driver.quit()