import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from py._xmlgen import html

_driver = None


# @pytest.fixture()
@pytest.fixture(scope='session', autouse=True)
def driver():
    global _driver
    ip = "82.157.168.101"
    server = "http://%s:7777/wd/hub" % ip
    # ip = "localhost"
    # chrome_options = webdriver.ChromeOptions()
    #
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument('--proxy-server=%s' % server)
    # _driver = webdriver.Chrome(options=chrome_options)
    _driver = webdriver.Remote(
        command_executor="http://%s:7777/wd/hub" % ip,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    # return _driver
    # _driver.maximize_window()
    _driver.get("https://www.baidu.com/")
    # 返回数据
    yield _driver
    # 实现用例后置
    _driver.close()
    _driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    if not _driver:
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


def pytest_html_results_table_html(report, data):
    # if report.passed:
    #     del data[:]
    #     data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))
    pass


def pytest_html_report_title(report):
    report.title = "pytest示例项目测试报告"

def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()