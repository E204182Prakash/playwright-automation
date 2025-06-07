class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.dashboard_url = "https://example.com/dashboard"

    def load(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_dashboard_loaded(self):
        return self.page.url == self.dashboard_url
