"""Recharge users API method."""
from ibsng.handler.handler import Handler


class rechargeUsers(Handler):
    """Recharge users method class."""

    def control(self):
        """Validate inputs after setup method.

        :return: None
        :rtype: None
        """
        self.is_valid(self.user_id, str)
        self.is_valid_content(self.user_id)
        self.is_valid(self.comment, str)

    def setup(self, user_ids, comment):
        """Setup required parameters.

        :param list user_ids: ibsng user ids
        :param str comment: comment for this action

        :return: None
        :rtype: None
        """
        self.user_id = ",".join(map(str, user_ids))
        self.comment = comment