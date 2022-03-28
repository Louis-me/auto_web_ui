from pages.baidu_page import BaiduPage
import pytest

class TestBaidu:
    def test_baidu1(self, driver):
        page = BaiduPage(driver, "test_baidu1")
        page.operate()
        page.check_point()

    @pytest.mark.finished
    def test_baidu2(self, driver):
        page = BaiduPage(driver, "test_baidu2")
        page.operate()
        page.check_point()

    def test_baidu3(self, driver):
        page = BaiduPage(driver, "test_baidu3")
        page.operate()
        page.check_point()

    def test_baidu4(self, driver):
        page = BaiduPage(driver, "test_baidu4")
        page.operate()
        page.check_point()

    def test_baidu5(self, driver):
        page = BaiduPage(driver, "test_baidu5")
        page.operate()
        page.check_point()

    def test_baidu6(self, driver):
        page = BaiduPage(driver, "test_baidu6")
        page.operate()
        page.check_point()

    def test_baidu7(self, driver):
        page = BaiduPage(driver, "test_baidu7")
        page.operate()
        page.check_point()

    def test_baidu8(self, driver):
        page = BaiduPage(driver, "test_baidu8")
        page.operate()
        page.check_point()

    def test_baidu9(self, driver):
        page = BaiduPage(driver, "test_baidu9")
        page.operate()
        page.check_point()