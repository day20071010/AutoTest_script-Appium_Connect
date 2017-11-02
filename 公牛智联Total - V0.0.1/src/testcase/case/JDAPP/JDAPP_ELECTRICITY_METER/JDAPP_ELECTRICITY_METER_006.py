# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppElectricityMeter6(WidgetOperationJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'单一电价设置'  # 用例名称
        self.zentao_id = 1151  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_on")

        self.ac.swipe(0.5, 0.9, 0.5, 0.7, 0, self.driver)

        self.widget_click(self.page["control_device_page"]["set_elec"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_button"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["single_price"],
                          self.page["single_price_page"]["title"])

        elec_price = self.widget_click(self.page["single_price_page"]["set_price"],
                                       self.page["single_price_page"]["title"])

        elec_price_data = "5"
        elec_price.clear()
        self.ac.send_keys(elec_price, elec_price_data, self.driver)
        self.logger.info(u'[APP_INPUT] ["单一电价"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["single_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["set_elec"]), "name")
        if u"单一电价" not in attribute:
            raise TimeoutException("set signal price is wrong, current mode is %s" % [attribute])

        # self.ac.swipe(0.5, 0.7, 0.5, 0.9, 0, self.driver)


        now_h = int(time.strftime("%H"))
        elec, elec_bill = self.get_device_elect(now_h + 2, False)

        elec_bill_info = ("elec bill is wrong, current [elec_bill:%s, elec:%s, elec_price:%s]"
                          % (sum(elec_bill[now_h + 1]), sum(elec[now_h + 1]), elec_price_data))
        self.logger.info(elec_bill_info)

        if sum(elec_bill[now_h + 1]) != sum(elec[now_h + 1]) * int(elec_price_data):
            raise TimeoutException(elec_bill_info)

        self.case_over(True)
