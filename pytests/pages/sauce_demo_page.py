import os
import random
from pytests.support.screenshot_service import ScreenshotService
from pytests.pages.common import Common
from faker import Faker

class SaucedemoPage:

    # **
    # * Mapeamento de elementos
    # **

    @staticmethod
    def field_username(page):
        return page.locator("[data-test=\"username\"]")
    
    @staticmethod
    def field_password(page):
        return page.locator("[data-test=\"password\"]")
    
    @staticmethod
    def button_login(page):
        return page.locator("[data-test=\"login-button\"]")
    
    @staticmethod
    def message_error(page):
        return page.locator("[data-test=\"error\"]")
    
    @staticmethod
    def element_product(page):
        return page.get_by_text("Products")
    
    @staticmethod
    def button_sort_product(page):
        return page.locator("[data-test=\"product_sort_container\"]")
    
    @staticmethod
    def element_inventory_list(page):
        return page.locator(".inventory_list")
    
    @staticmethod
    def product_inventory(page, item):
        return page.locator(f"[data-test=\"{item}\"]")
    
    @staticmethod
    def button_cart_with_item(page, item):
        return page.locator("a").filter(has_text=item)
    
    @staticmethod
    def product_at_cart(page, item):
        return page.get_by_role("link", name=item)
    
    @staticmethod
    def button_checkout(page):
        return page.locator("[data-test=\"checkout\"]")
    
    @staticmethod
    def field_first_name(page):
        return page.locator("[data-test=\"firstName\"]")
    
    @staticmethod
    def field_last_name(page):
        return page.locator("[data-test=\"lastName\"]")
    
    @staticmethod
    def field_zip_code(page):
        return page.locator("[data-test=\"postalCode\"]")
    
    @staticmethod
    def button_cancel(page):
        return page.locator("[data-test=\"cancel\"]")
    
    @staticmethod
    def button_continue(page):
        return page.locator("[data-test=\"continue\"]")
    
    @staticmethod
    def element_checktout_information(page):
        return page.get_by_text("Checkout: Your Information")
    
    @staticmethod
    def button_finish(page):
        return page.locator("[data-test=\"finish\"]")
    
    @staticmethod
    def message_thank_you_order(page):
        return page.get_by_role("heading", name="Thank you for your order!")
    
    @staticmethod
    def price_item(page, price):
        return page.get_by_text(price, exact=True)
    
    # **
    # * Métodos e Funções
    # **

    # abrir a pagina saucedemo e realizar assert do title garantindo pagina aberta
    @staticmethod
    def page_saucedemo(page):
        page.goto(f"{os.environ['url_saucedemo']}")
        ScreenshotService.take_screenshot(page)
        assert page.title() == "Swag Labs"

    # realizar login no saucedemo
    @staticmethod
    def fill_login_saucedemo(page):
        SaucedemoPage.field_username(page).fill(os.environ['username'])
        SaucedemoPage.field_password(page).fill(os.environ['password'])
        ScreenshotService.take_screenshot(page)

    # realizar login no saucedemo com dados inválidos
    @staticmethod
    def fill_login_saucedemo_invalid(page, field, value):
        if field == "username":
            value = Common.values_change(value)
            SaucedemoPage.field_username(page).fill(value)
            SaucedemoPage.field_password(page).fill(os.environ['password'])
        else:
            value = Common.values_change(value)
            SaucedemoPage.field_username(page).fill(os.environ['username'])
            SaucedemoPage.field_password(page).fill(value)
        ScreenshotService.take_screenshot(page)

    # clicar em login e validar pagina carregada
    @staticmethod
    def perform_login_saucedemo(page):
        SaucedemoPage.button_login(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.element_product(page).is_visible() == True

    # validar mensagem de erro ao realizar login com dados inválido
    @staticmethod
    def perform_login_saucedemo_invalid(page):
        SaucedemoPage.button_login(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.message_error(page).is_visible() == True

    # método para validar o sort product
    @staticmethod
    def validate_sort_product(page, type):
        match type:
            case "A to Z":
                SaucedemoPage.button_sort_product(page).select_option("az")
                ScreenshotService.take_screenshot(page)
                # extrainndo da lista de produtos o primeiro item e pegando os 19 primeiros carácteres
                first_item = SaucedemoPage.element_inventory_list(page).all_text_contents()[0].split("Add to cart")[0][:19]
                assert first_item == "Sauce Labs Backpack"
            case "Z to A":
                SaucedemoPage.button_sort_product(page).select_option("za")
                ScreenshotService.take_screenshot(page)
                # extrainndo da lista de produtos o primeiro item e pegando os 19 primeiros carácteres
                first_item = SaucedemoPage.element_inventory_list(page).all_text_contents()[0].split("Add to cart")[0][:19]
                assert first_item == "Test.allTheThings()"
            case "Lo to Hi":
                SaucedemoPage.button_sort_product(page).select_option("lohi")
                ScreenshotService.take_screenshot(page)
                # extrainndo da lista de produtos o primeiro item e pegando os 5 últimos carácteres
                first_item = SaucedemoPage.element_inventory_list(page).all_text_contents()[0].split("Add to cart")[0][-5:]
                assert first_item == "$7.99"
            case "Hi to Lo":
                SaucedemoPage.button_sort_product(page).select_option("hilo")
                ScreenshotService.take_screenshot(page)
                # extrainndo da lista de produtos o primeiro item e pegando os 6 últimos carácteres
                first_item = SaucedemoPage.element_inventory_list(page).all_text_contents()[0].split("Add to cart")[0][-6:]
                assert first_item == "$49.99"

    # adiciona e remove item do carrinho na tela inicial
    @staticmethod
    def validate_add_remove_product_initial(page):
        SaucedemoPage.product_inventory(page, "add-to-cart-sauce-labs-backpack").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.button_cart_with_item(page, "1").is_visible() == True
        SaucedemoPage.product_inventory(page, "remove-sauce-labs-backpack").click()
        ScreenshotService.take_screenshot(page)

    # adiciona item e remove na tela do carrinho
    @staticmethod
    def validate_add_remove_product_cart(page):
        SaucedemoPage.product_inventory(page, "add-to-cart-sauce-labs-onesie").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.button_cart_with_item(page, "1").is_visible() == True
        SaucedemoPage.button_cart_with_item(page, "1").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.product_at_cart(page, "Sauce Labs Onesie").is_visible() == True
        SaucedemoPage.product_inventory(page, "remove-sauce-labs-onesie").click()
        ScreenshotService.take_screenshot(page)

    # valida mais de 1 item no carrinho
    @staticmethod
    def validate_add_more_then_one_product(page):
        SaucedemoPage.product_inventory(page, "add-to-cart-sauce-labs-bike-light").click()
        SaucedemoPage.product_inventory(page, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.button_cart_with_item(page, "2").is_visible() == True
        SaucedemoPage.button_cart_with_item(page, "2").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.product_at_cart(page, "Sauce Labs Bike Light").is_visible() == True
        assert SaucedemoPage.product_at_cart(page, "Sauce Labs Bolt T-Shirt").is_visible() == True

    # adiciona item e valida a tela checkout
    @staticmethod
    def add_product_to_checkout(page):
        SaucedemoPage.product_inventory(page, "add-to-cart-sauce-labs-backpack").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.button_cart_with_item(page, "1").is_visible() == True
        SaucedemoPage.button_cart_with_item(page, "1").click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.product_at_cart(page, "Sauce Labs Backpack").is_visible() == True
        SaucedemoPage.button_checkout(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.element_checktout_information(page).is_visible() == True

    # adiciona item e cancela na tela checkout
    @staticmethod
    def validate_cancel_purchase(page):
        SaucedemoPage.add_product_to_checkout(page)
        SaucedemoPage.button_cancel(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.product_at_cart(page, "Sauce Labs Backpack").is_visible() == True

    # preenche campos da tela checkout com dados inválidos
    @staticmethod
    def fill_data_checkout_invalid(page, field, value):
        SaucedemoPage.add_product_to_checkout(page)
        if field == "firstName":
            value = Common.values_change(value)
            SaucedemoPage.field_first_name(page).fill(value)
            SaucedemoPage.field_last_name(page).fill(Faker().last_name())
            SaucedemoPage.field_zip_code(page).fill(str(( ''.join(random.choice("123456789") for i in range(8)) )))
            ScreenshotService.take_screenshot(page)
        elif field == "lastName":
            value = Common.values_change(value)
            SaucedemoPage.field_first_name(page).fill(Faker().first_name())
            SaucedemoPage.field_last_name(page).fill(value)
            SaucedemoPage.field_zip_code(page).fill(str(( ''.join(random.choice("123456789") for i in range(8)) )))
            ScreenshotService.take_screenshot(page)
        else:
            value = Common.values_change(value)
            SaucedemoPage.field_first_name(page).fill(Faker.first_name())
            SaucedemoPage.field_last_name(page).fill(Faker.last_name())
            SaucedemoPage.field_zip_code(page).fill(value)
            ScreenshotService.take_screenshot(page)

    # valida mensagem de erro na tela checkout
    @staticmethod
    def validate_continue_invalid(page):
        SaucedemoPage.button_continue(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.message_error(page).is_visible() == True

    # finaliza o pedido e valida mensagem de thank you order
    @staticmethod
    def validate_finish_purchase(page):
        SaucedemoPage.add_product_to_checkout(page)
        SaucedemoPage.field_first_name(page).fill(Faker().first_name())
        SaucedemoPage.field_last_name(page).fill(Faker().last_name())
        SaucedemoPage.field_zip_code(page).fill(str(( ''.join(random.choice("123456789") for i in range(8)) )))
        ScreenshotService.take_screenshot(page)
        SaucedemoPage.button_continue(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.product_at_cart(page, "Sauce Labs Backpack").is_visible() == True
        assert SaucedemoPage.price_item(page, "$29.99").is_visible() == True
        SaucedemoPage.button_finish(page).click()
        ScreenshotService.take_screenshot(page)
        assert SaucedemoPage.message_thank_you_order(page).is_visible() == True