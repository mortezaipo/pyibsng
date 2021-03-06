"""Voucher recharge user API method."""
from ibsng.handler.handler import Handler


class voucherRechargeUser(Handler):
    """Voucher recharge user method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.voucher_pin, str)

    def setup(self, voucher_pin):
        """Setup required parameters.

        :param str voucher_pin: voucher pin

        :return: None
        :rtype: None
        """
        self.voucher_pin = voucher_pin
