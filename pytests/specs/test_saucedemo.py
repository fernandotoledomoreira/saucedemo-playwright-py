from pytests.support.hooks import *
from pytests.pages.sauce_demo_page import SaucedemoPage
from playwright.sync_api import Page
from pytests.examples.examples_saucedemo import *
import allure

@pytest.mark.test_saucedemo
def test_login_saucedemo(page: Page):
    with allure.step("acessar o site saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("preencher o campos de login"):
        SaucedemoPage.fill_login_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.perform_login_saucedemo(page)

@pytest.mark.test_saucedemo
@pytest.mark.parametrize("field, value", examples_invalid_login_fields)
def test_login_saucedemo_invalid(page: Page, field, value):
    with allure.step("acessar o site sr saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step(f"preencher o campo {field} com o valor {value}"):
        SaucedemoPage.fill_login_saucedemo_invalid(page, field, value)
    with allure.step("realizar o login"):
        SaucedemoPage.perform_login_saucedemo_invalid(page)

@pytest.mark.test_saucedemo
@pytest.mark.parametrize("type", examples_sort_product)
def test_validate_sort_product(page: Page, type):
    with allure.step("acessar o site sr saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.fill_login_saucedemo(page)
        SaucedemoPage.perform_login_saucedemo(page)
    with allure.step(f"validar sort product por {type}"):
        SaucedemoPage.validate_sort_product(page, type)

@pytest.mark.test_saucedemo
def test_add_remove_product_cart(page: Page):
    with allure.step("acessar o site saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.fill_login_saucedemo(page)
        SaucedemoPage.perform_login_saucedemo(page)
    with allure.step("adicionar e remover item do carrinho"):
        SaucedemoPage.validate_add_remove_product_initial(page)
    with allure.step("adicionar item e remover tela do carrinho"):
        SaucedemoPage.validate_add_remove_product_cart(page)

@pytest.mark.test_saucedemo
def test_add_more_then_one_product(page: Page):
    with allure.step("acessar o site saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.fill_login_saucedemo(page)
        SaucedemoPage.perform_login_saucedemo(page)
    with allure.step("adicionar mais de um produto no carrinho"):
        SaucedemoPage.validate_add_more_then_one_product(page)

@pytest.mark.test_saucedemo
def test_validate_cancel_purchase(page: Page):
    with allure.step("acessar o site saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.fill_login_saucedemo(page)
        SaucedemoPage.perform_login_saucedemo(page)
    with allure.step("cancelar compra"):
        SaucedemoPage.validate_cancel_purchase(page)

@pytest.mark.test_saucedemo
@pytest.mark.parametrize("field, value", examples_invalid_data_checkout)
def test_checkout_data_invalid(page: Page, field, value):
    with allure.step("acessar o site saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.fill_login_saucedemo(page)
        SaucedemoPage.perform_login_saucedemo(page)
    with allure.step("prencher os campos do checkout com valores inválido"):
        SaucedemoPage.fill_data_checkout_invalid(page, field, value)
        SaucedemoPage.validate_continue_invalid(page)

@pytest.mark.test_saucedemo
def test_validate_finish_purchase(page: Page):
    with allure.step("acessar o site saucedemo"):
        SaucedemoPage.page_saucedemo(page)
    with allure.step("realizar o login"):
        SaucedemoPage.fill_login_saucedemo(page)
        SaucedemoPage.perform_login_saucedemo(page)
    with allure.step("cancelar compra"):
        SaucedemoPage.validate_finish_purchase(page)