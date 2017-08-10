# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings4(LaunchApp):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'退出当前账号后，确定按钮功能检查'  # 用例名称
        self.zentao_id = 1974  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(self.page["logout_popup"]["title"],
                              self.page["logout_popup"]["confirm"],
                              self.page["login_page"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            element = self.wait_widget(self.page["login_page"]["password"], 1, 0.5)
            pwd = self.ac.get_attribute(element, "name")
            if len(pwd) != 0:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

