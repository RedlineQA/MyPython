class TestLogin:
    def test_login_existing_user(self, setup_asos):
        page, login_page = setup_asos
        login_page.login("testforyura@gmail.com", "qwerty12345")