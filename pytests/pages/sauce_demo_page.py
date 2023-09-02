import os
from pytests.support.screenshot_service import ScreenshotService
from pytests.pages.common import Common

class SaucedemoPage:

    # **
    # * Mapeamento de elementos
    # **

    @staticmethod
    def field_email(page):
        return page.locator("xpath=//input[@id='email']")