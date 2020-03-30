from selenium import webdriver
import time

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore

#UI파일 연결
# form_class = uic.loadUiType("login.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id_val = None
        self.password_val = None

        # 버튼에 기능을 할당하는 코드
        self.id.textChanged.connect(self.idTextFunction)
        self.password.textChanged.connect(self.passwordTextFunction)
        self.login.clicked.connect(self.clickBtn)
        self.file_open.clicked.connect(self.pushButtonClicked)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(757, 434)
        self.login = QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(90, 170, 113, 32))
        self.login.setObjectName("login")
        self.id = QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(150, 50, 113, 21))
        self.id.setObjectName("id")
        self.password = QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 80, 113, 21))
        self.password.setObjectName("password")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 115, 82, 18))
        self.label_3.setObjectName("label_3")
        self.file_open = QPushButton(Dialog)
        self.file_open.setGeometry(QtCore.QRect(150, 110, 113, 32))
        self.file_open.setObjectName("file_open")
        self.file_name = QLabel(Dialog)
        self.file_name.setGeometry(QtCore.QRect(20, 150, 711, 16))
        self.file_name.setText("")
        self.file_name.setObjectName("file_name")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 131, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login.setText(_translate("Dialog", "로그인"))
        self.label.setText(_translate("Dialog", "아이디"))
        self.label_2.setText(_translate("Dialog", "비밀번호"))
        self.label_3.setText(_translate("Dialog", "크롬 드라이버"))
        self.file_open.setText(_translate("Dialog", "파일 찾기"))
        self.label_4.setText(_translate("Dialog", "쿠팡 장바구니 매크로"))

    def idTextFunction(self):
        self.id_val = self.id.text()

    def passwordTextFunction(self):
        self.password_val = self.password.text()

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.file_name.setText(fname[0])

    def validation_check(self):
        # 유효성 체크
        if self.id_val is None or self.password_val is None or self.file_name is None:
            return False
        else:
            return True

    # 로그인 버튼 클릭
    def clickBtn(self):
        if self.validation_check() is False:
            return
        # browser = webdriver.Chrome('./chromedriver')
        browser = webdriver.Chrome(self.file_name.text())
        browser.get('https://login.coupang.com/login/login.pang')

        # 로그인
        browser.find_element_by_name('email').send_keys(self.id_val)
        browser.find_element_by_class_name('_loginPasswordInput').send_keys(self.password_val)
        login_btn = browser.find_element_by_class_name('login__button')
        login_btn.click()
        time.sleep(3)

        # 검색
        search_box = browser.find_element_by_name("q")
        search_box.send_keys("마스크 kf94")
        search_box.submit()

        # 로켓 배송
        rocket = browser.find_element_by_xpath("//label[@for='deliveryFilterOption-rocket_all']")
        rocket.click()

        # 72개씩 보기
        # page_length_selector = browser.find_element_by_xpath("/html/body/div[2]/section/form/div[2]/div[2]/div[2]/div/div[2]/ul")
        #
        # browser.execute_script("arguments[0].setAttribute('class','selectbox-options opened')", page_length_selector)
        # page_length = browser.find_element_by_xpath('/html/body/div[2]/section/form/div[2]/div[2]/div[2]/div/div[2]/ul/li[4]/label')
        # time.sleep(1)
        # page_length.click()

        # 상품 장바구니 담기
        product_list = browser.find_elements_by_class_name('delivery')
        while len(product_list) == 0:
            browser.refresh()
            time.sleep(2)
        print('product_list')
        for idx, product in enumerate(product_list):
            if idx > 3:
                print('break')
                break
            product.click()
            browser.switch_to.window(browser.window_handles[1])

            time.sleep(1)
            # 장바구니 담기
            cart_btn = browser.find_element_by_class_name('prod-cart-btn')
            cart_btn.click()

            time.sleep(1)
            # 탭 종료
            browser.close()
            browser.switch_to.window(browser.window_handles[0])


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

