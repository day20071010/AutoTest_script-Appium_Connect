# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppDevicePage1(LaunchApp):
    @case_run(False)
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'默认页面信息检查'  # 用例名称
        self.zentao_id = 1773  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.wait_widget(self.page["device_page"]["user_image"], 3, 1)

            element = self.wait_widget(self.page["device_page"]["welcome"], 3, 1)
            now_time = self.ac.get_attribute(element, "name")
            if 0 < int(time.strftime("%H")) < 12:
                if now_time != u"上午好":
                    raise TimeoutException()
            else:
                if now_time != u"下午好":
                    raise TimeoutException()

            element = self.wait_widget(self.page["device_page"]["welcome"], 3, 1)
            city = self.ac.get_attribute(element, "name")
            if city != u"上海市":
                raise TimeoutException()

            self.wait_widget(self.page["device_page"]["weather"], 3, 1)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

