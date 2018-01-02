# -*-coding:utf-8-*-

from PIL import Image
import pytesseract
import os
import unittest
import time
from selenium import webdriver as a
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

newtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
DIR = os.path.dirname(__file__)
if os.path.isdir(DIR + u'/screenshot') is False:
    os.mkdir(DIR + u'/screenshot')

url = input('url:')
url_2 = input('url_2:')
username = input('username:')
password = input('password:')
username_2 = input('username_2:')
password_2 = input('password_2')
username_app = input('username_app:')
password_app = input('password_app:')


class MyTestCase(unittest.TestCase):
    def isElementExist(self, css):
        s = self.driver.find_elements_by_xpath(css)
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True

    def isEnabled(self, id):
        s = self.driver.find_elements_by_id(id)
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True

    # def write_log(self, path, name, text):
    #     with open(path + "\\" + name + r".text", 'w', encoding="utf8") as f:
    #         f.writelines(text)
    #     f.close()
    def order_assess(self):
        dr = self.driver
        dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
        sleep(1)
        dr.find_element_by_android_uiautomator('new UiSelector().text("商品订单")').click()
        sleep(1)
        dr.find_element_by_android_uiautomator('new UiSelector().text("待评价")').click()
        sleep(1)
        layouts = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_product_name')
        layouts[0].click()
        sleep(3)
        dr.swipe(500, 1500, 500, 800, 800)
        sleep(3)
        dr.find_element_by_id('com.ruiyin.lovelife:id/btn_refuse').click()
        sleep(1)

    def yan(self, code):
        self.login()
        self.driver.find_element_by_link_text('虚拟商品管理').click()
        sleep(3)
        self.driver.find_element_by_link_text('卡密校验').click()
        sleep(3)
        self.driver.switch_to.frame('commonFrame')
        self.driver.find_element_by_class_name('input-text').send_keys(code)
        sleep(3)
        self.driver.find_element_by_class_name('btn25z').click()
        sleep(3)
        btn = self.driver.find_elements_by_class_name('btn25z')
        btn[1].click()
        sleep(3)
        alert = self.driver.switch_to_alert()
        alert.accept()
        sleep(3)
        self.driver.quit()

    def confirm(self):
        self.login()
        self.driver.find_element_by_link_text('交易管理').click()
        sleep(3)
        self.driver.find_element_by_link_text('退款订单').click()
        sleep(3)
        self.driver.switch_to.frame('commonFrame')
        # iframe = dr.find_elements_by_id('commonFrame')
        fa = self.driver.find_elements_by_link_text('审核协议')
        fa[0].click()
        sleep(3)
        js = 'var q = document.documentElement.scrollTop=10000'
        self.driver.execute_script(js)
        sleep(3)
        self.driver.find_element_by_id('backnote').send_keys('测试')
        sleep(1)
        self.driver.find_element_by_id('beanbackaddress').send_keys('测试')
        sleep(1)
        button = self.driver.find_elements_by_class_name('btn25z')
        button[0].click()
        sleep(3)
        alert = self.driver.switch_to_alert()
        alert.accept()
        sleep(3)
        self.driver.quit()

    def confirm2(self):
        self.login()
        self.driver.find_element_by_link_text('交易管理').click()
        sleep(3)
        self.driver.find_element_by_link_text('退款订单').click()
        sleep(3)
        self.driver.switch_to.frame('commonFrame')
        # iframe = dr.find_elements_by_id('commonFrame')
        fa = self.driver.find_elements_by_link_text('确认收到退货')
        fa[0].click()
        sleep(3)
        js = 'var q = document.documentElement.scrollTop=10000'
        self.driver.execute_script(js)
        sleep(3)
        button = self.driver.find_elements_by_class_name('btn25z')
        button[0].click()
        sleep(3)
        alert = self.driver.switch_to_alert()
        alert.accept()
        sleep(3)
        self.driver.quit()

    def confirm3(self):
        self.login()
        self.driver.find_element_by_link_text('交易管理').click()
        sleep(3)
        self.driver.find_element_by_link_text('退款订单').click()
        sleep(3)
        self.driver.switch_to.frame('commonFrame')
        # iframe = dr.find_elements_by_id('commonFrame')
        fa = self.driver.find_elements_by_link_text('审核协议')
        fa[0].click()
        sleep(3)
        js = 'var q = document.documentElement.scrollTop=10000'
        self.driver.execute_script(js)
        sleep(3)
        self.driver.find_element_by_id('butongyi').click()
        sleep(1)
        self.driver.find_element_by_id('backnote').send_keys('测试')
        sleep(1)
        button = self.driver.find_elements_by_class_name('btn25z')
        button[0].click()
        sleep(3)
        alert = self.driver.switch_to_alert()
        alert.accept()
        sleep(3)
        self.driver.quit()

    def confirm4(self):
        self.login2()
        self.driver.find_element_by_link_text('订单系统').click()
        sleep(3)
        self.driver.find_element_by_link_text('退款审核管理').click()
        sleep(3)
        self.driver.switch_to.frame('mainFrame')
        alt = self.driver.find_elements_by_xpath("//img[@alt='订单处理']")
        alt[0].click()
        sleep(3)
        js = 'var q = document.documentElement.scrollTop=10000'
        self.driver.execute_script(js)
        sleep(3)
        self.driver.find_element_by_id('dealMsg').send_keys('测试')
        sleep(1)
        self.driver.find_element_by_id('btn').click()
        sleep(3)
        self.driver.quit()

    def login(self):
        self.driver = a.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id('loginStoreId').send_keys(username)
        sleep(3)
        self.driver.find_element_by_xpath("//input[@id='loginUserPwd1']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//input[@id='loginUserPwd']").send_keys(password)
        sleep(3)
        self.driver.find_element_by_class_name('qd_btn').click()

    def login2(self):
        self.driver = a.Chrome()
        self.driver.get(url_2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.save_screenshot(DIR + '/login.png')
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').send_keys(username_2)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input').send_keys(password_2)
        elem_pic = self.driver.find_element_by_xpath("//img[@id='validateImg']")
        location = elem_pic.location  # 获取验证码x,y轴坐标
        size = elem_pic.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open(DIR + '/login.png')  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(DIR + '/captcha.png')
        code = pytesseract.image_to_string(Image.open(DIR + '/captcha.png'))
        # os.remove('C:/Users/Administrator/Downloads/captcha.jpg')
        self.driver.find_element_by_id('validateCodeId').send_keys(code)
        sleep(3)
        self.driver.find_element_by_xpath("//input[@align='absmiddle']").click()
        self.login_error()

    def login_error(self):
        if self.isElementExist('/html/body/form/table/tbody/tr[2]/td[2]/input'):
            self.driver.quit()
            self.login2()

    def order_buy(self):
        dr = self.driver
        dr.find_element_by_id('com.ruiyin.lovelife:id/order_pay_submit').click()
        # password = dr.find_elements_by_id('com.ruiyin.lovelife:id/password_ly')
        j = 8
        for i in range(1, 7):
            sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/code_' + str(i)).click()
            dr.keyevent(j)
            j += 1
            # i += 1
        sleep(3)
        dr.find_element_by_id('com.ruiyin.lovelife:id/right_ly').click()

    # def order_buy(self):
    #     dr = self.driver
    #     dr.find_element_by_id('com.ruiyin.lovelife:id/order_pay_submit').click()
    #     # sleep(3)
    #     passwords = dr.find_elements_by_class_name('android.widget.EditText')
    #     j = 8
    #     for i in range(len(passwords)):
    #         sleep(2)
    #         passwords[i].click()
    #         sleep(2)
    #         dr.keyevent(j)
    #         j += 1
    #         i += 1
    #     sleep(3)
    #     dr.find_element_by_id('com.ruiyin.lovelife:id/right_ly').click()

    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'test'
        desired_caps['appPackage'] = 'com.ruiyin.lovelife'
        desired_caps['appActivity'] = '.activity.WelComeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def test_a_login(self):  # 登录账号
        dr = self.driver
        if self.isEnabled('com.ruiyin.lovelife:id/tv_immediate_switchover'):
            dr.find_element_by_id('com.ruiyin.lovelife:id/tv_immediate_switchover').click()
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
            dr.find_element_by_android_uiautomator('new UiSelector().text("立即登录")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_username').send_keys(username_app)
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_pass').send_keys(password_app)
            # driver.hide_keyboard()
            sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/login_button').click()
            if not dr.find_element_by_id('com.ruiyin.lovelife:id/level_name').is_displayed():
                raise ValueError('登录错误')
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_life')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_login.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_b_ergodic(self):  # 遍历按钮
        dr = self.driver
        try:
            ergodic = ['首页', '福利', '银行', '购物车', '我的']
            for i in range(len(ergodic)):
                dr.find_element_by_android_uiautomator('new UiSelector().text("' + ergodic[i] + '")').click()
                sleep(1)
                i += 1
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_ergodic.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_c_buy(self):  # 实品单规格直接购买
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            sleep(3)
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 500, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试单规格")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_put_into_shop_car').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_product_detail_buy').click()
            sleep(3)
            dr.tap([(600, 1830)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_submit_order').click()
            self.order_buy()
            sleep(5)
            if dr.find_element_by_id('com.ruiyin.lovelife:id/tv_paySucess_hint').is_displayed():
                if dr.find_element_by_id('com.ruiyin.lovelife:id/tv_paySucess_hint').text != '已成功支付！':
                    raise ValueError('未完成支付')
            dr.back()
            dr.back()
            dr.back()
            WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.NAME, '购物车')))
        except Exception as e:
            # path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'D:\\log')
            # file_path = os.path.join(path, self.name)
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_buy.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_d_send(self):  # 订单发货
        try:
            self.login()
            self.driver.find_element_by_link_text('交易管理').click()
            sleep(3)
            self.driver.find_element_by_link_text('待发货的订单').click()
            sleep(3)
            self.driver.switch_to.frame('commonFrame')
            # iframe = dr.find_elements_by_id('commonFrame')
            fa = self.driver.find_elements_by_link_text('发货')
            fa[0].click()
            sleep(3)
            s = self.driver.find_element_by_id('company')
            s.find_element_by_xpath("//option[@value='ff808081548216900154a385356e0262-顺丰快递']").click()
            sleep(3)
            self.driver.find_element_by_id('expressNo').send_keys('123123123132')
            sleep(3)
            self.driver.find_element_by_id('fhNote').send_keys('测试')
            sleep(3)
            button = self.driver.find_elements_by_class_name('btn25z')
            button[1].click()
            sleep(3)
            self.driver.quit()
        except Exception as e:
            self.driver.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_send.jpg')
            print(str(e))
            self.assertIsNone(e)

    def test_e_order_verify(self):  # 确认收货
        dr = self.driver
        try:
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("商品订单")').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("待收货")').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_remind_delivery').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/right_ly').click()
            sleep(1)
            dr.back()
            WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.NAME, '购物车')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_order_verify.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_f_order_assess1(self):  # 订单退款
        try:
            self.order_assess()
            dr = self.driver
            dr.tap([(98, 1111)])
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/amont').send_keys('0.01')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/edit_note').send_keys('测试')
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("提交申请")').click()
            sleep(3)
            self.confirm()
            dr.back()
            dr.back()
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_order_assess1.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_h_order_assess2(self):  # 订单退货
        try:
            dr = self.driver
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 500, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试单规格")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_product_detail_buy').click()
            sleep(3)
            dr.tap([(600, 1830)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_submit_order').click()
            self.order_buy()
            sleep(5)
            dr.back()
            dr.back()
            dr.back()
            WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.NAME, '购物车')))
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("商品订单")').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("待发货")').click()
            sleep(1)
            name = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_product_name')
            name[0].click()
            sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_refuse').click()
            # self.order_assess()
            sleep(2)
            dr.tap([(665, 417)])
            sleep(2)
            dr.tap([(98, 1111)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/amont').send_keys('0.01')
            dr.find_element_by_id('com.ruiyin.lovelife:id/edit_note').send_keys('测试')
            dr.find_element_by_android_uiautomator('new UiSelector().text("提交申请")').click()
            sleep(3)
            dr.back()
            dr.back()
            self.confirm()
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
            dr.find_element_by_android_uiautomator('new UiSelector().text("退款售后")').click()
            sleep(1)
            productname = dr.find_elements_by_id('com.ruiyin.lovelife:id/product_name')
            productname[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 400, 800)
            sleep(2)
            # dr.find_element_by_android_uiautomator('new UiSelector().text("填写物流信息")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/write_goods_message').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/logistics_edittext').send_keys('测试')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/logistics_order_num_editext').send_keys('1233212321')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/note_edittext').send_keys('测试')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/publish').click()
            self.confirm2()
            dr.back()
            dr.back()
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_order_assess2.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_i_order_assess3(self):  # 订单申诉
        try:
            dr = self.driver
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 500, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试单规格")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_product_detail_buy').click()
            sleep(3)
            dr.tap([(600, 1830)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_submit_order').click()
            self.order_buy()
            sleep(5)
            dr.back()
            dr.back()
            dr.back()
            WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.NAME, '购物车')))
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("商品订单")').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("待发货")').click()
            sleep(1)
            name = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_product_name')
            name[0].click()
            sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_refuse').click()
            # self.order_assess()
            # dr.tap([(665, 417)])
            # sleep(1)
            sleep(1)
            dr.tap([(98, 1111)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/amont').send_keys('0.01')
            dr.find_element_by_id('com.ruiyin.lovelife:id/edit_note').send_keys('测试')
            dr.find_element_by_android_uiautomator('new UiSelector().text("提交申请")').click()
            sleep(3)
            dr.back()
            dr.back()
            self.confirm3()
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
            dr.find_element_by_android_uiautomator('new UiSelector().text("退款售后")').click()
            sleep(1)
            productname = dr.find_elements_by_id('com.ruiyin.lovelife:id/product_name')
            productname[0].click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("客服申诉")').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_title').send_keys('测试')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_complain_detail').send_keys('测试')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_complain_num').send_keys('18608882233')
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/commit_complain').click()
            self.confirm4()
            dr.back()
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_order_assess3.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_j_hexiao(self):  # 虚拟商品购买&虚拟商品核销
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 400, 800)
            dr.swipe(500, 1500, 500, 400, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试虚品")').click()
            dr.find_element_by_android_uiautomator('new UiSelector().text("立即购买")').click()
            dr.find_element_by_android_uiautomator('new UiSelector().text("提交")').click()
            self.order_buy()
            sleep(5)
            for i in range(4):
                dr.back()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
            sleep(3)
            dr.find_element_by_android_uiautomator('new UiSelector().text("代金券")').click()
            sleep(3)
            dr.find_element_by_android_uiautomator('new UiSelector().text("未消费")').click()
            sleep(3)
            dr.tap([(583, 530)])
            sleep(1)
            code = dr.find_element_by_id('com.ruiyin.lovelife:id/tv_voucher_char_no').text
            sleep(3)
            dr.back()
            dr.back()
            self.yan(code)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_hexiao.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_k_shop_car1(self):  # 购物车购买
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("购物车")').click()
            if not dr.find_element_by_id('com.ruiyin.lovelife:id/item_check_choice_one').get_attribute("checked"):
                dr.find_element_by_id('com.ruiyin.lovelife:id/item_check_choice_one').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_pay').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_shop_car_submit_order').click()
            self.order_buy()
            sleep(5)
            dr.back()
            # dr.back()
            WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.NAME, '首页')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_shop_car1.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_l_shop_car2(self):  # 父子订单
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 500, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试单规格")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_put_into_shop_car').click()
            sleep(3)
            dr.back()
            dr.back()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('伞')
            dr.find_element_by_android_uiautomator('new UiSelector().text("搜索")').click()
            san = dr.find_elements_by_class_name('android.widget.LinearLayout')
            san[0].click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_put_into_shop_car').click()
            sleep(1)
            for i in range(0, 3):
                dr.back()
                i += 1
            WebDriverWait(dr, 20).until(EC.presence_of_element_located((By.NAME, '购物车')))
            dr.find_element_by_android_uiautomator('new UiSelector().text("购物车")').click()
            if not dr.find_element_by_id('com.ruiyin.lovelife:id/cb_select_all').get_attribute("checked"):
                dr.find_element_by_id('com.ruiyin.lovelife:id/cb_select_all').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_pay').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_shop_car_submit_order').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/order_pay_submit').click()
            sleep(3)
            passwords = dr.find_elements_by_class_name('android.widget.EditText')
            j = 8
            for i in range(len(passwords)):
                sleep(2)
                passwords[i].click()
                sleep(2)
                dr.keyevent(j)
                j += 1
                i += 1
            sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/right_ly').click()
            sleep(5)
            dr.back()
            # dr.back()
            WebDriverWait(dr, 20).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_shop_car2.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_m_buy_double(self):  # 实品双规格直接购买
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 500, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试多规格")').click()
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_product_detail_buy').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("白色")').click()
            sleep(2)
            dr.tap([(600, 1830)])
            sleep(1)
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_submit_order').click()
            sleep(3)
            self.order_buy()
            sleep(5)
            dr.back()
            dr.back()
            dr.back()
            WebDriverWait(dr, 20).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_test_buy_double.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    def test_n_group_buy(self):  # 拼团直接购买
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()

            dr.find_element_by_android_uiautomator('new UiSelector().text("聚惠拼团")').click()
            sleep(3)
            dr.tap([(933, 885)])
            sleep(3)
            dr.tap([(612, 1823)])

            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_product_detail_buy').click()
            sleep(3)
            dr.tap([(600, 1830)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_submit_order').click()
            self.order_buy()
            sleep(5)
            dr.back()
            dr.back()
            dr.back()
            WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.NAME, '我的')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_group_buy.jpg')
            print(e)
            self.assertIsNone(e)

    @unittest.skip
    def test_o_buy_secondary(self):  # 商品二次支付
        dr = self.driver
        try:
            dr.find_element_by_android_uiautomator('new UiSelector().text("首页")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/et_search').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/search_second_ed').send_keys('自动化')
            layout = dr.find_elements_by_id('com.ruiyin.lovelife:id/tv_automated_words')
            layout[0].click()
            sleep(3)
            dr.swipe(500, 1500, 500, 500, 800)
            dr.find_element_by_android_uiautomator('new UiSelector().text("自动化测试单规格")').click()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_product_detail_buy').click()
            sleep(3)
            dr.tap([(600, 1830)])
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_submit_order').click()
            sleep(3)
            dr.back()
            dr.find_element_by_id('com.ruiyin.lovelife:id/right_txt').click()
            sleep(3)
            dr.back()
            dr.back()
            dr.back()
            dr.find_element_by_id('com.ruiyin.lovelife:id/btn_container_user').click()
            dr.find_element_by_android_uiautomator('new UiSelector().text("商品订单")').click()
            sleep(1)
            dr.find_element_by_android_uiautomator('new UiSelector().text("待付款")').click()
            if self.isEnabled('com.ruiyin.lovelife:id/item_order_action'):
                buy = dr.find_elements_by_id('com.ruiyin.lovelife:id/item_order_action')
                buy[0].click()
                sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/order_pay_submit').click()
            sleep(3)
            passwords = dr.find_elements_by_class_name('android.widget.EditText')
            j = 8
            for i in range(len(passwords)):
                sleep(2)
                passwords[i].click()
                sleep(2)
                dr.keyevent(j)
                j += 1
                i += 1
            sleep(3)
            dr.find_element_by_id('com.ruiyin.lovelife:id/right_ly').click()
            sleep(5)
            dr.back()
            sleep(3)
            dr.back()
            WebDriverWait(dr, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ruiyin.lovelife:id/btn_container_user')))
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/screenshot/' + newtime + '_group_buy.jpg')
            print(e)
            dr.start_activity('com.ruiyin.lovelife', '.activity.WelComeNewActivity')
            self.assertIsNone(e)

    @classmethod
    def tearDownClass(self):
        dr = self.driver
        dr.reset()
        sleep(10)
        for i in range(1, 5):
            dr.swipe(900, 1000, 200, 1000, 500)
            sleep(4)
        if dr.find_elements_by_id('com.ruiyin.lovelife:id/to_main_btn'):
            dr.find_element_by_id('com.ruiyin.lovelife:id/to_main_btn').click()
            sleep(10)
        dr.close_app()
        dr.quit()


if __name__ == '__main__':
    unittest.main()
