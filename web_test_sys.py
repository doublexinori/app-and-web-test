import unittest, os, time
import win32api
import win32con
import pytesseract
from Tools.scripts.treesync import raw_input
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from PIL import Image

DIR = os.path.dirname(__file__)
newtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())


class MyTestCase(unittest.TestCase):
    def isElementExist(self, css):
        s = self.driver.find_elements_by_xpath(css)
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True

    def login(self):
        self.driver.save_screenshot(DIR + '/login.png')
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td[2]/input').send_keys(password)
        elem_pic = self.driver.find_element_by_xpath("//img[@id='validateImg']")
        location = elem_pic.location  # 获取验证码x,y轴坐标
        size = elem_pic.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open(DIR + '/login.png')  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(DIR + '/captcha.png')
        code = pytesseract.image_to_string(Image.open(DIR + '/captcha.png'))
        self.driver.find_element_by_id('validateCodeId').send_keys(code)
        sleep(3)
        self.driver.find_element_by_xpath("//input[@align='absmiddle']").click()
        self.login_error()

    def login_error(self):
        if self.isElementExist('/html/body/form/table/tbody/tr[2]/td[2]/input'):
            self.login()

    def switch(self, text):
        self.driver.find_element_by_link_text(text).click()
        self.driver.switch_to.frame('mainFrame')
        sleep(2)
        if self.driver.find_elements_by_xpath("//tbody[@style='background-color: #ecf3ff']") == None:
            raise ValueError('显示内容有误')
        self.driver.switch_to.default_content()

    def switch1(self, text):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_link_text(text))
        self.driver.find_element_by_link_text(text).click()
        sleep(3)
        self.driver.switch_to.frame('mainFrame')
        if self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_0']") == None:
            raise ValueError('显示内容有误')
        self.driver.switch_to.default_content()

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_a_order(self):
        try:
            self.login()
            dr = self.driver
            dr.find_element_by_id('ORDER').click()
            dr.find_element_by_link_text('退款审核管理').click()
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_xpath("//tbody[@style='background-color: #ecf3ff']") == None:
                raise ValueError('显示内容有误')
            dr.find_element_by_link_text('虚拟订单').click()
            dr.switch_to.default_content()
            texts = ['虚拟订单管理', '实物订单退款', '虚拟订单退款', '点单订单退款', '点单订单管理', '水电煤订单管理', '话费订单管理', '流量订单管理']
            for text in texts:
                self.switch(text)
                sleep(1)
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_order.jpg')
            print(e)
            self.assertIsNone(e)

    def test_b_product(self):
        try:
            dr = self.driver
            dr.find_element_by_id('PRODUCT').click()
            dr.find_element_by_link_text('商品分类管理').click()
            sleep(1)
            dr.find_element_by_link_text('商品审核').click()
            # sleep(3)
            dr.switch_to.frame('mainFrame')
            sleep(2)
            if dr.find_elements_by_xpath("//tbody[@style='background-color: #ecf3ff']") == None:
                raise ValueError('显示内容有误')
            dr.find_element_by_link_text('高级搜索').click()
            dr.switch_to.default_content()
            sleep(3)
            dr.find_element_by_xpath("//*[@id='100103']/a").click()
            dr.switch_to.frame('mainFrame')
            sleep(2)
            if dr.find_elements_by_xpath("//tbody[@style='background-color: #ecf3ff']") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            dr.find_element_by_link_text('金币、限购批量管理').click()
            sleep(1)
            dr.find_element_by_link_text('推荐商品管理').click()
            sleep(1)
            dr.find_element_by_link_text('代发实物商品').click()
            sleep(1)
            dr.find_element_by_link_text('代发虚拟商品').click()
            sleep(1)
            dr.find_element_by_link_text('规格参数模板管理').click()
            sleep(1)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_xpath("//tbody") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_product.jpg')
            print(e)
            self.assertIsNone(e)

    def test_c_app(self):
        try:
            dr = self.driver
            dr.find_element_by_id('APP').click()
            dr.find_element_by_link_text('商品评论管理').click()
            sleep(1)
            dr.find_element_by_link_text('商品评论审核').click()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_app.jpg')
            print(e)
            self.assertIsNone(e)

    def test_d_user(self):
        try:
            dr = self.driver
            dr.find_element_by_id('USER').click()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='500503']/a").click()
            sleep(1)
            dr.find_element_by_link_text('个人会员冻结名单').click()
            dr.switch_to.frame('mainFrame')
            sleep(2)
            if dr.find_elements_by_xpath("//tbody[@style='background-color: #ecf3ff']") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            self.switch('个人会员管理')
            sleep(1)
            dr.find_element_by_link_text('短信验证码查询').click()
            sleep(1)
            dr.find_element_by_link_text('快捷登录/注册验证码开关').click()
            sleep(1)
            dr.find_element_by_link_text('会员奖励批量充值').click()
            sleep(1)
            dr.find_element_by_link_text('会员奖励批量充值记录').click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('DataTables_Table_0') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            dr.find_element_by_link_text('会员奖励批量充值审核').click()
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('DataTables_Table_0') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_user.jpg')
            print(e)
            self.assertIsNone(e)

    def test_e_offers(self):
        try:
            dr = self.driver
            dr.find_element_by_id('OFFERS').click()
            sleep(1)
            frames = ['优惠券领取列表', '优惠券类型列表', '翻牌管理']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('mainFrame')
                if dr.find_element_by_id('table') == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            # dr.find_element_by_link_text('优惠券类型列表').click()
            # sleep(5)
            # dr.switch_to.frame('mainFrame')
            # if dr.find_element_by_id('table') == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            # dr.find_element_by_link_text('翻牌管理').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_element_by_id('table') == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            dr.find_element_by_xpath("//*[@id='801000504']/a").click()
            dr.switch_to.frame('mainFrame')
            if dr.find_element_by_id('table') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='801000505']/a").click()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='801000506']/a").click()
            sleep(1)
            dr.find_element_by_link_text('支付打折').click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('DataTables_Table_0') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('团购').click()
            dr.switch_to.frame('mainFrame')
            if dr.find_element_by_id('table') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('新店尝鲜').click()
            dr.switch_to.frame('mainFrame')
            sleep(2)
            if dr.find_elements_by_xpath("//tbody[@style='background-color: #ecf3ff']") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_offers.jpg')
            print(e)
            self.assertIsNone(e)

    def test_f_store(self):
        try:
            dr = self.driver
            dr.find_element_by_id('STORE').click()
            sleep(1)
            dr.find_element_by_link_text('新增商户会员').click()
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_class_name('houtai_tp') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            frames = ['商户会员管理', '商户角色管理', '商户会员冻结名单']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('mainFrame')
                if dr.find_elements_by_xpath("//*[@id='fill_data']/table") == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            # dr.find_element_by_link_text('商户角色管理').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_elements_by_xpath("//*[@id='fill_data']/table") == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            # dr.find_element_by_link_text('商户会员冻结名单').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_elements_by_xpath("//*[@id='fill_data']/table") == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            dr.find_element_by_link_text('新增商户签约记录').click()
            sleep(1)
            dr.find_element_by_link_text('商户签约管理').click()
            sleep(1)
            dr.find_element_by_link_text('添加商户回访记录').click()
            sleep(1)
            dr.find_element_by_link_text('商户回访记录管理').click()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_store.jpg')
            print(e)
            self.assertIsNone(e)

    def test_g_fin(self):
        try:
            dr = self.driver
            dr.find_element_by_id('FIN').click()
            sleep(1)
            frames = ['金融产品管理', '金融产品分类管理', '银行管理', '通用模板金融产品管理']
            for frame in frames:
                self.switch1(frame)
                sleep(3)
            # dr.find_element_by_link_text('金融产品管理').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_elements_by_xpath("//*[@id='DataTables_Table_0']") == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            dr.find_element_by_link_text('金融产品申请单').click()
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_xpath("//*[@id='DataTables_Table_0_wrapper']/div[3]") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            # dr.find_element_by_link_text('金融产品分类管理').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_elements_by_xpath("//*[@id='DataTables_Table_0']") == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            # dr.find_element_by_link_text('银行管理').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_elements_by_xpath("//*[@id='DataTables_Table_0']") == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            # dr.find_element_by_link_text('通用模板金融产品管理').click()
            # dr.switch_to.frame('mainFrame')
            # if dr.find_elements_by_xpath("//*[@id='DataTables_Table_0']") == None:
            #     raise ValueError('显示内容有误')
            # dr.switch_to.default_content()
            # sleep(1)
            dr.find_element_by_link_text('金融街用户添加').click()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_fin.jpg')
            print(e)
            self.assertIsNone(e)

    def test_h_ifind(self):
        try:
            dr = self.driver
            dr.find_element_by_id('IFIND').click()
            sleep(1)
            frames = ['签到规则管理', '签到广告配置', '任务配置', '任务组图片管理', '中奖页面专区', '推广奖励设置', '注册推广奖励', '经验规则设置', '等级设置', '绑卡送金币',
                      '投诉建议', '基础配置', '活动配置', '奖池配置', '奥运活动', '帮助中心管理']
            for frame in frames:
                self.switch1(frame)
                sleep(3)
            dr.find_element_by_link_text('转盘奖励审核').click()
            sleep(3)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('tableGold') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='8002003']/a").click()
            sleep(3)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_xpath("//*[@id='DataTables_Table_0']") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('推广攻略').click()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_ifind.jpg')
            print(e)
            self.assertIsNone(e)

    def test_i_system(self):
        try:
            dr = self.driver
            dr.find_element_by_id('SYSTEM').click()
            sleep(1)
            dr.find_element_by_link_text('添加管理员').click()
            sleep(1)
            frames = ['管理员管理', '角色管理', '地区管理', '物流公司管理', '接入地市管理']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(3)
                dr.switch_to.frame('mainFrame')
                if dr.find_elements_by_xpath("//*[@id='fill_data']") == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            dr.find_element_by_link_text('缓存管理').click()
            sleep(1)
            dr.find_element_by_link_text('缓存查询').click()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_system.jpg')
            print(e)
            self.assertIsNone(e)

    def test_j_lifecolumn(self):
        try:
            dr = self.driver
            dr.find_element_by_id('LIFECOLUMN').click()
            sleep(1)
            frames = ['栏目管理', '广告配置', '新栏目配置']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('mainFrame')
                if dr.find_elements_by_id('table') == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            self.switch1('签到楼层奖励活动配置')
            sleep(1)
            dr.find_element_by_link_text('分享文案图片配置').click()
            sleep(1)
            frames1 = ['话费充值业务管理', '流量充值业务管理', '水电煤业务配置']
            for frame in frames1:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('mainFrame')
                if dr.find_elements_by_id('dataTable') == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            sleep(2)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_lifecolumn.jpg')
            print(e)
            self.assertIsNone(e)

    def test_k_settlement(self):
        try:
            dr = self.driver
            dr.find_element_by_id('SETTLEMENT').click()
            sleep(1)
            dr.find_element_by_link_text('订单列表').click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_xpath("//*[@id='fill_data']/div[2]/table") == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('运费退款').click()
            sleep(1)
            dr.find_element_by_link_text('商户列表').click()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_settlement.jpg')
            print(e)
            self.assertIsNone(e)

    def test_l_wap(self):
        try:
            dr = self.driver
            dr.find_element_by_id('WAP').click()
            sleep(1)
            frames = ['轮播图', '快捷入口', '商品专区', '精选专区']
            for frame in frames:
                dr.find_element_by_link_text(frame).click()
                sleep(2)
                dr.switch_to.frame('mainFrame')
                if dr.find_elements_by_id('dataTable') == None:
                    raise ValueError('显示内容有误')
                dr.switch_to.default_content()
                sleep(1)
            dr.find_element_by_link_text('爆品专区')
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('ShowSubTable') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(1)
            dr.find_element_by_link_text('商圈精选')
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('selectSubCfgStore') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_wap.jpg')
            print(e)
            self.assertIsNone(e)

    def test_m_mynest(self):
        try:
            dr = self.driver
            dr.find_element_by_id('MYNEST').click()
            sleep(1)
            dr.find_element_by_link_text('我的窝首页').click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_elements_by_id('table') == None:
                raise ValueError('显示内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_mynest.jpg')
            print(e)
            self.assertIsNone(e)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    raw_input()
