import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Set lang env (default=en)")

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'language'})

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    user_language = request.config.getoption("language")
    yield browser
    print("\nquit browser..")
    browser.quit()

#browser = webdriver.Chrome(options=options)
