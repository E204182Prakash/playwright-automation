from behave import given, when, then
from pages.login_page import LoginPage

@given("I open the login page")
def step_open_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.load()

@when("I enter valid credentials")
def step_enter_credentials(context):
    context.login_page.login("user", "pass")

@then("I should see the dashboard")
def step_verify_dashboard(context):
    assert context.login_page.is_dashboard_loaded()
