from datetime import datetime
from pathlib import Path

# from allure.constants import AttachmentType
import allure
import pytest

import Runner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from utils.Logger import Logger


@pytest.fixture(scope="class")
def test_setup(request):
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver = webdriver.Chrome(service=Service("../drivers/chromedriver.exe"))
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("End of Test")


@pytest.fixture(scope="function", autouse=True)
def create_log(request):
    log = Logger()
    class_name = request.node.parent.name
    test_name = request.node.name
    request.cls.logger = log.get_logger(test_name, class_name)


# For allure report use this method
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     extra = getattr(rep, 'extra', [])
#     if rep.when == 'call' and rep.failed:
#         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         file_name = rep.nodeid.replace("::", "_").split("py_")[1] + f"{now}.png"
#         allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=allure.attachment_type.PNG)


# For pytest report use this method
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    pytest_html = item.config.pluginmanager.getplugin('html')
    extra = getattr(rep, 'extra', [])
    if rep.when == 'call' and rep.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = rep.nodeid.replace("::", "_").split("py_")[1] + f"{now}.png"
        full_file_path = str(Path(__file__).parent) + f"\\reports\\screenshots\\{file_name}"
        driver.save_screenshot(full_file_path)
        screenshot = driver.get_screenshot_as_base64()
        extra.append(pytest_html.extras.image(screenshot))
        rep.extra = extra
