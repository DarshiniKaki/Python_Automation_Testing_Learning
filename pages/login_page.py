class LoginPage:
    def __init__(self, page):
        self.page = page
    def enter_username(self, username):
        self.page.fill("#username", username)
    def enter_password(self, password):
        self.page.fill("#password", password)
    def click_login(self):
        self.page.click("button[type='submit']")