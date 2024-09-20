
from expects import expect, be_true, be_false

from src.refactoring_to_patterns.creation_method.product_package import ProductPackage


class TestProductPackage:

    TV_CHANNELS = ["HBO", "FOX"]
    A_PHONE_NUMBER = 1234567890
    INTERNET_MB = "100MB"

    def test_create_with_only_internet(self):
        product_package = ProductPackage(internet_label=self.INTERNET_MB)

        expect(product_package.has_internet()).to(be_true)
        expect(product_package.has_phone_number()).to(be_false)
        expect(product_package.has_tv_channels()).to(be_false)

    def test_create_with_internet_and_phone_number(self):
        product_package = ProductPackage(internet_label=self.INTERNET_MB, telephone_number=self.A_PHONE_NUMBER)

        expect(product_package.has_internet()).to(be_true)
        expect(product_package.has_phone_number()).to(be_true)
        expect(product_package.has_tv_channels()).to(be_false)

    def test_create_with_internet_and_tv_channels(self):
        standard_tv_package = ProductPackage.create_tv_standard_package(
            internet_label=self.INTERNET_MB,
            tv_channels=self.TV_CHANNELS
        )

        expect(standard_tv_package.has_internet()).to(be_true)
        expect(standard_tv_package.has_phone_number()).to(be_false)
        expect(standard_tv_package.has_tv_channels()).to(be_true)

    def test_create_with_internet_phone_number_and_tv_channels(self):
        premium_package = ProductPackage.create_premium_package(
            internet_label=self.INTERNET_MB,
            phone_number=self.A_PHONE_NUMBER,
            tv_channels=self.TV_CHANNELS
        )

        expect(premium_package.has_internet()).to(be_true)
        expect(premium_package.has_phone_number()).to(be_true)
        expect(premium_package.has_tv_channels()).to(be_true)
