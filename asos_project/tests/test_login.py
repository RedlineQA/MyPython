class TestLogin:
    def test_login_existing_user(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("added4074@mechanicspedia.com")
        login_page.login_user_password("qwerty12345")
        login_page.verify_login_success()

    def test_login_invalid_email_format(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("qwerty")
        login_page.verify_login_invalid_email_format()

    def test_login_unregistered_email(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("unregistered@gmail.com")
        login_page.verify_login_unregistered_email()

    def test_login_wrong_password(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("berta7@mechanicspedia.com")
        login_page.login_user_password("wrongpassword")
        login_page.verify_login_wrong_password()