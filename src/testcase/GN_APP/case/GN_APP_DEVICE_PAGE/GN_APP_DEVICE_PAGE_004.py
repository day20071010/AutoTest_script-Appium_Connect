# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPDevicePage4(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'设备配网过程中，弹出终止配网提示框，确定按钮功能检查'  # 用例名称
        self.zentao_id = "1800"  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["add_device"],
                          self.page["device_add_scan_page"]["title"])

        self.widget_click(self.page["device_add_scan_page"]["gateway_hw"],
                          self.page["prepare_set_network_page"]["title"])

        self.widget_click(self.page["prepare_set_network_page"]["prepare_next"],
                          self.page["set_network_page"]["title"])

        wifi_pwd = self.wait_widget(self.page["set_network_page"]["wifi_pwd"])

        data = conf["wifi_pwd"]
        data = bytearray.fromhex(str(data)).decode('utf-8').replace(" ", "")
        wifi_pwd.clear()
        self.ac.send_keys(wifi_pwd, data, self.driver)
        self.debug.info(u'[APP_INPUT] ["WiFi密码"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["set_network_page"]["prepare_next"],
                          self.page["scan_with_subscribe_page"]["title"])

        self.widget_click(self.page["scan_with_subscribe_page"]["to_return"],
                          self.page["terminate_add_device_popup"]["title"])

        self.widget_click(self.page["terminate_add_device_popup"]["confirm"],
                          self.page["set_network_page"]["title"])
