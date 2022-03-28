from common.operates import OperateElement
import time
from common.elements import Elements
import os




class Pages:
    '''
    page层
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, kwargs):
        self.driver = kwargs["driver"]

        if kwargs.get("launch", "0") == "0":  # 若为空， 刷新页面
            self.driver.get(self.driver.current_url)
        self.isOperate = True
        self.test_info = kwargs["test_info"]
        self.test_case = kwargs["test_case"]
        self.test_check = kwargs["test_check"]
        self.case_name = kwargs["case_name"]
        self.msg = ""

    '''
     操作步骤
    '''

    def operate(self):

        for item in self.test_case:
            result = OperateElement(self.driver).operate(item, self.test_info)
            if not result["result"]:
                # self.test_info[0]["msg"] = result["msg"]
                self.isOperate = False
                return False
            if item.get("is_time", "0") != "0":
                time.sleep(item["is_time"])  # 等待时间
                print("==等待%s秒==" % item["is_time"])

        return True

    def check_point(self, kwargs={}):
        result = self.check(kwargs)
        if not result:
            assert False
        else:
            assert True
        # 写入到数据库
        # statistics_result(result=result, testInfo=self.test_info, caseName=self.caseName,
        #                   driver=self.driver, logTest=self.logTest,
        #                   testCase=self.test_case,
        #                   testCheck=self.test_check)

    def check(self, kwargs):
        result = True
        # if kwargs.get("check_point", "0") != "0":
        #     return kwargs["check_point"]

        if self.isOperate:

            resp = OperateElement(self.driver).operate(self.test_check, self.test_info)
            # 默认检查点，就是查找页面元素
            if kwargs.get("check", Elements.DEFAULT_CHECK) == Elements.DEFAULT_CHECK and not resp["result"]:
                m = "{m}元素不存在".find(self.test_check["element_info"])
                print(m)
                # self.test_info[0]["msg"] = m
                result = False
            else:
                # print("检测点暂时只支持查找页面元素")
                pass
        else:
            result = False
        return result