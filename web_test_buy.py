import unittest, os, time
from selenium import webdriver
from time import sleep

DIR = os.path.dirname(__file__)
newtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())


class MyTestCase(unittest.TestCase):
    def login(self):
        self.driver.find_element_by_id('loginStoreId').send_keys(username)
        sleep(3)
        self.driver.find_element_by_xpath("//input[@id='loginUserPwd1']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//input[@id='loginUserPwd']").send_keys(password)
        sleep(3)
        self.driver.find_element_by_class_name('qd_btn').click()

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_a_shangpinguanli(self):
        try:
            self.login()
            dr = self.driver
            dr.find_element_by_id('S2000000').click()
            sleep(1)
            dr.find_element_by_link_text('发布新商品').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_elements_by_class_name('store-right') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            frames = ['仓库中的商品', '出售中的商品']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('commonFrame')
                if dr.find_elements_by_class_name('store-table') == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            sleep(2)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_shangpinguanli.jpg')
            print(e)
            self.assertIsNone(e)

    def test_b_xunishangpinguanli(self):
        try:
            dr = self.driver
            dr.find_element_by_id('S3000000').click()
            sleep(1)
            dr.find_element_by_link_text('发布虚拟商品').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_elements_by_class_name('sta-main') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('卡密校验').click()
            sleep(1)
            frames = ['出售中的虚拟商品', '仓库中的虚拟商品']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('commonFrame')
                if dr.find_elements_by_class_name('store-table') == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            sleep(2)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_xunishangpinguanli.jpg')
            print(e)
            self.assertIsNone(e)

    def test_c_jiaoyiguanli(self):
        try:
            dr = self.driver
            dr.find_element_by_id('S4000000').click()
            sleep(1)
            dr.find_element_by_link_text('我的全部订单').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            dr.find_element_by_id('orderId').send_keys('7082917313811133')
            sleep(1)
            dr.find_element_by_xpath("/html/body/div/div[2]/ul[4]/li/a[1]").click()
            sleep(2)
            code = dr.find_element_by_xpath("//*[@id='orderTable']/tr[2]/td/div[1]/div[2]/span/span[6]").text
            if code.find('1231231') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('待发货的订单').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            dr.find_element_by_id('orderId').send_keys('7081814341073094')
            sleep(1)
            dr.find_element_by_xpath("/html/body/div/div[3]/ul[4]/li/a[1]").click()
            sleep(2)
            code = dr.find_element_by_xpath("//*[@id='orderTable']/tr[2]/td/div[1]/div[2]/span/span[6]").text
            if code.find('21312') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('待评价的订单').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            dr.find_element_by_id('orderId').send_keys('7071911120868626')
            sleep(1)
            dr.find_element_by_xpath("/html/body/div/div[2]/ul[4]/li/a[1]/span").click()
            sleep(2)
            code = dr.find_element_by_xpath("//*[@id='orderTable']/tr[2]/td/div[1]/div[2]/span/span[6]").text
            if code.find('311') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('退款订单').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            dr.find_element_by_id('orderId').send_keys('7082917370984225')
            sleep(1)
            dr.find_element_by_xpath("/html/body/div/div[2]/ul[3]/li/a[1]/span").click()
            sleep(2)
            code = dr.find_element_by_xpath("//*[@id='orderTable']/tr[3]/td/div[1]/div[2]/span/span[2]").text
            if code.find('1231231') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('运费模版管理').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_elements_by_class_name('store-table') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_jiaoyiguanlii.jpg')
            print(e)
            self.assertIsNone(e)

    def test_d_pingjiaguanli(self):
        try:
            dr = self.driver
            dr.find_element_by_id('S6000000').click()
            sleep(1)
            dr.find_element_by_link_text('评价管理').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            dr.find_element_by_id('productName').send_keys('接口测试')
            sleep(1)
            dr.find_element_by_xpath("//*[@id='dataTable']/div[2]/ul[2]/li/a[1]").click()
            sleep(2)
            if dr.find_element_by_xpath("//*[@id='dataTable']/div[3]/table/tbody/tr[2]/td[2]").text.find('评价测试') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_pingjiaguanli.jpg')
            print(e)
            self.assertIsNone(e)

    def test_e_dianpushezhi(self):
        try:
            dr = self.driver
            dr.find_element_by_id('S7000000').click()
            sleep(1)
            dr.find_element_by_link_text('地图设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_element_by_xpath("//*[@id='container']") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_dianpushezhi.jpg')
            print(e)
            self.assertIsNone(e)

    def test_f_dianpudajian(self):
        try:
            dr = self.driver
            dr.find_element_by_id('S8000000').click()
            sleep(1)
            dr.find_element_by_link_text('联系方式设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            phone = dr.find_element_by_xpath("//*[@id='shipTypeContent']").get_attribute('value')
            if phone != '18601407983':
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('店招店标设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_element_by_xpath("//*[@id='formFile']/div/div[3]/table") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_dianpudajian.jpg')
            print(e)
            self.assertIsNone(e)

    def test_g_zhanghuzhongxin(self):
        try:
            dr = self.driver
            dr.find_element_by_id('S9000000').click()
            sleep(1)
            dr.find_element_by_link_text('安全设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_element_by_xpath("/html/body/div/div[3]/p[1]").text.find('18601407983') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('商户资料设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]/span").text.find('审核通过') == -1:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('商户扩展资料设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_elements_by_xpath("/html/body/div/div[2]/table") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('商户库存预警设置').click()
            sleep(2)
            dr.switch_to.frame('commonFrame')
            if dr.find_elements_by_xpath("/html/body/div/div[2]/table") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_zhanghuzhongxin.jpg')
            print(e)
            self.assertIsNone(e)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()