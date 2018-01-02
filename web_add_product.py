import unittest, os, time, random
import win32api
import win32con
import pytesseract
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from PIL import Image

DIR = os.path.dirname(__file__)
newtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())

url = input('url:')
username = input('username:')
password = input('password:')


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

    def scroll(self, id):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_id(id))

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_c_addrealproduct(self):
        try:
            dr = self.driver
            self.login()
            product_name = str(input('请输入商品名称'))
            product_id = str(input('请输入商品编号'))
            phone = str(input('请输入代发商户'))
            dr.find_element_by_id('PRODUCT').click()
            sleep(1)
            dr.find_element_by_link_text('代发实物商品').click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            dr.find_element_by_xpath("//*[@id='subCategoryId0']/ul/li[1]").click()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='subCategoryId1']/li[3]").click()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='subCategoryId2']/li[1]").click()
            sleep(1)
            dr.find_element_by_id('registName').send_keys(phone)
            sleep(1)
            dr.find_element_by_xpath("/html/body/div[6]/ul/li/input[3]").click()
            sleep(2)
            dr.find_element_by_id('productName').send_keys(product_name)
            sleep(1)
            dr.find_element_by_id('productNo').send_keys(product_id)
            sleep(1)
            dr.find_element_by_id('quantity').clear()
            dr.find_element_by_id('quantity').send_keys('100')
            sleep(1)
            self.scroll('listPrice')
            dr.find_element_by_id('listPrice').clear()
            dr.find_element_by_id('listPrice').send_keys('0.01')
            sleep(1)
            self.scroll('unitPrice')
            dr.find_element_by_id('unitPrice').clear()
            dr.find_element_by_id('unitPrice').send_keys('0.01')
            sleep(1)
            self.scroll('weight')
            dr.find_element_by_id('weight').clear()
            dr.find_element_by_id('weight').send_keys('1')
            sleep(1)
            self.scroll('note')
            dr.find_element_by_id('note').send_keys('测试')
            sleep(1)
            self.scroll('bigPicDataInputFile')
            dr.find_element_by_id('bigPicDataInputFile').send_keys(DIR + '/logo.jpg')
            sleep(3)
            frame = dr.find_element_by_xpath("//*[@id='cke_1_contents']/iframe")
            dr.execute_script("arguments[0].scrollIntoView();", frame)
            dr.switch_to.frame(frame)
            dr.find_element_by_xpath("/html/body").send_keys('测试')
            sleep(2)
            # dr.switch_to.default_content()
            dr.switch_to.parent_frame()
            dr.find_element_by_xpath("//*[@id='productForm']/div[1]/div[2]/input[1]").click()
            sleep(2)
            alert = self.driver.switch_to_alert()
            alert.accept()
            sleep(2)
            alert1 = self.driver.switch_to_alert()
            alert1.accept()
            sleep(5)
            dr.refresh()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='100103']/a").click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            if dr.find_element_by_xpath("//*[@id='productList']/tbody/tr[1]/td[3]").text != product_name:
                raise ValueError('内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_addrealproduct.jpg')
            print(e)
            self.assertIsNone(e)

    @unittest.skip
    def test_d_addvirproduct(self):
        try:
            dr = self.driver
            product_name = 'selenium虚品测试' + str(random.randint(1, 9)) + str(random.randint(0, 9))
            product_id = str(random.randint(312313321, 7849327983))
            dr.find_element_by_link_text('代发虚拟商品').click()
            sleep(2)
            dr.switch_to.frame('mainFrame')
            dr.find_element_by_xpath("//*[@id='subCategoryId0']/ul/li[1]").click()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='subCategoryId1']/li[1]").click()
            sleep(1)
            dr.find_element_by_xpath("//*[@id='subCategoryId2']/li[1]").click()
            sleep(1)
            dr.find_element_by_id('registName').send_keys('18601407983')
            sleep(1)
            dr.find_element_by_xpath("/html/body/div[6]/ul/li/input[3]").click()
            sleep(2)
            dr.find_element_by_id('productName').send_keys(product_name)
            sleep(1)
            dr.find_element_by_id('productNo').send_keys(product_id)
            sleep(1)
            dr.find_element_by_id('startTime').click()
            sleep(1)
            dr.find_element_by_id('dpTodayInput').click()
            sleep(1)
            dr.find_element_by_id('endTime').click()
            sleep(1)
            dr.find_element_by_id('dpTodayInput').click()
            sleep(1)
            dr.find_element_by_id('extFileld30').send_keys('24小时')
            sleep(1)
            dr.find_element_by_id('quantity').clear()
            dr.find_element_by_id('quantity').send_keys('100')
            sleep(1)
            self.scroll('listPrice')
            dr.find_element_by_id('listPrice').clear()
            dr.find_element_by_id('listPrice').send_keys('0.01')
            sleep(1)
            self.scroll('unitPrice')
            dr.find_element_by_id('unitPrice').clear()
            dr.find_element_by_id('unitPrice').send_keys('0.01')
            sleep(1)
            self.scroll('extFileld31')
            dr.find_element_by_id('extFileld31').send_keys('测试')
            sleep(1)
            self.scroll('note')
            dr.find_element_by_id('note').send_keys('测试')
            sleep(1)
            self.scroll('bigPicDataInputFile')
            dr.find_element_by_id('bigPicDataInputFile').send_keys(DIR + '/logo.jpg')
            sleep(3)
            frame = dr.find_element_by_xpath("//*[@id='cke_1_contents']/iframe")
            dr.execute_script("arguments[0].scrollIntoView();", frame)
            dr.switch_to.frame(frame)
            dr.find_element_by_xpath("/html/body").send_keys('测试')
            sleep(2)
            # dr.switch_to.default_content()
            dr.switch_to.parent_frame()
            dr.find_element_by_xpath("//*[@id='productForm']/div[1]/div[2]/input[1]").click()
            sleep(2)
            alert = self.driver.switch_to_alert()
            alert.accept()
            sleep(2)
            alert1 = self.driver.switch_to_alert()
            alert1.accept()
            sleep(3)
            dr.switch_to.default_content()
            dr.find_element_by_link_text('商品管理').click()
            sleep(1)
            dr.switch_to.frame('mainFrame')
            if dr.find_element_by_xpath("//*[@id='productList']/tbody/tr[1]/td[3]") != product_name:
                raise ValueError('内容有误')
            dr.switch_to.default_content()
            sleep(3)
        except Exception as e:
            dr.get_screenshot_as_file(DIR + '/' + newtime + '_test_addrealproduct.jpg')
            print(e)
            self.assertIsNone(e)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
