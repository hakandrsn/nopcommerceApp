from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\hakan\\Desktop\\Proje\\Python\\driver\\chromedriver.exe")
        print("Launching Chrome Browser.......")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\hakan\\Desktop\\Proje\\Python\\driver\\geckodriver64.exe")
        print("Launching Firefox Browser.......")
    else:
        driver = webdriver.Edge(executable_path="C:\\Users\\hakan\\Desktop\\Proje\\Python\\driver\\msedgedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########## PyTest HTML Reports #########

# İt is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Pavan"

# it is hook for delete(modify environment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)