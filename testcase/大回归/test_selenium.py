import os
import time
import pytest
from multiprocessing import Process

class TestCase(object):
    @pytest.mark.finished
    def test_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def test1_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def test11_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def test2_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def test3_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def test4_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def test5_001(self, driver):
        time.sleep(3)
        driver.get("https://www.baidu.com")
        print(driver.title)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("你好")
    def main(self):
        # os.system("pytest -s -m finished")
        os.system("pytest -s d:\\project\\py_selenium_grid\\testcase\\大回归\\")

