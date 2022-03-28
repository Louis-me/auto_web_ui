from common.pages import Pages
from common.elements import Elements
import logging
class BaiduPage:
    def __init__(self, driver, case_name):
        self.driver = driver
        self.test_info = {"title": "搜索selenium", "info": "用例描述"}
        test_case = [
            {"element_info": "kw","find_type": "id", "operate_type": Elements.CLICK, "info": "用例步骤"},
            {"element_info": "kw","find_type": "id", "operate_type": Elements.SEND_KEYS, "info": "用例步骤", "msg": "selenium"},
            {"element_info": "su", "find_type": "id", "operate_type": Elements.CLICK, "info": "点击搜索按钮"}
        ]
        # test_check = {"element_info": "//*[contains(@aria-label,'selenium')]", "find_type": "xpath", "info": "查找页面元素"}
        test_check = {}
        _init = {"driver": self.driver, "test_info": self.test_info,'test_case':test_case,'test_check':test_check,"case_name": case_name}
        self.page = Pages(_init)

    def operate(self):  # 操作步骤
        self.driver.get("https://www.baidu.com/")
        logging.info("执行用例—%s" % self.test_info["title"])
        self.page.operate()

    def check_point(self):  # 检查点
        self.page.check_point()
