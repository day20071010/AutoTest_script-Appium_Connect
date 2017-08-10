# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppLogin8(LaunchApp):
    @case_run(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—密码输入超过5次后，信息检查'  # 用例名称
        self.zentao_id = 1898  # 禅道ID

    # 用例动作
    def case(self):
        try:
            user_name = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["username"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = conf["user_and_pwd"][self.user]["user_name"]
            data = str(data).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            count = 1
            while count > 0:
                self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
                login_pwd = self.widget_click(self.page["login_page"]["title"],
                                              self.page["login_page"]["password"],
                                              self.page["login_page"]["title"],
                                              1, 1, 1, 10, 0.5)

                data = str(conf["err_pwd"]).decode('hex').replace(" ", "")
                login_pwd.clear()
                self.ac.send_keys(login_pwd, data)
                self.logger.info(u'[APP_INPUT] ["错误密码"] input success')
                time.sleep(0.5)

                self.widget_click(self.page["login_page"]["title"],
                                  self.page["login_page"]["login_button"],
                                  self.page["god_page"]["title"],
                                  1, 1, 1, 10, 0.5)

                while True:
                    try:
                        self.wait_widget(self.page["loading_popup"]["title"], 1, 0.5)
                    except TimeoutException:
                        break

                count -= 1

            widget_px = self.page["login_page"]["login_button"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["px"]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["px"]["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            try:
                self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
                login_pwd = self.widget_click(self.page["login_page"]["title"],
                                              self.page["login_page"]["password"],
                                              self.page["login_page"]["title"],
                                              1, 1, 1, 10, 0.5)

                data = conf["user_and_pwd"][self.user]["login_pwd"]
                data = str(data).decode('hex').replace(" ", "")
                login_pwd.clear()
                self.ac.send_keys(login_pwd, data)
                self.logger.info(u'[APP_INPUT] ["正确密码"] input success')
                self.widget_click(self.page["login_page"]["title"],
                                  self.page["login_page"]["login_button"],
                                  self.page["device_page"]["title"],
                                  1, 1, 1, 10, 0.5)
            except TimeoutException:
                i = 1
                while i <= 33:
                    time.sleep(10)
                    widget_px = self.page["god_page"]["title"]
                    width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["px"]["width"])
                    height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["px"]["height"])
                    self.driver.tap([(width, height)], )
                    print "time sleep %sS" % (i * 10)
                    i += 1
                self.widget_click(self.page["login_page"]["title"],
                                  self.page["login_page"]["login_button"],
                                  self.page["device_page"]["title"],
                                  1, 1, 1, 10, 0.5)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)

