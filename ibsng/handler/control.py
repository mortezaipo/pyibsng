"""Main inputs validator library."""
import re
from abc import ABCMeta, abstractmethod

from ibsng.exception.method import InvalidArgumentType, InvalidArgumentValue


class Control(object, metaclass=ABCMeta):
    """Controlling inputs.

    .. note: do not implement __init__ method for this class.
    """

    # useful patterns
    EMAIL_PATTERN = r"[a-zA-Z0-9\_\-\.\+]+@[a-zA-Z0-9\.\-]+\.[a-zA-Z]+"
    IP_PATTERN = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
    ID_PATTERN = r"^[0-9]+$"
    IDS_PATTERN = r"^[0-9\,]+$"
    POSITIVE_NUMBER = r"^[0-9]+$"

    def is_valid(self, argument_value, argument_type, value_check=True):
        """Validate argument type before sending to the server.

        .. raise: InvalidArgumentType

        :param type argument_value: argument data
        :param type argument_type: type of argument which argument must be.

        :return: argument validation
        :rtype: bool
        """
        if value_check and not argument_value:
            raise InvalidArgumentValue(self.__class__.__name__,
                                       argument_value)

        if not isinstance(argument_value, argument_type):
            raise InvalidArgumentType(self.__class__.__name__,
                                      argument_value,
                                      argument_type)
        return True

    def is_valid_content(self, argument_value, regex_pattern):
        """Validate argument content before sending to the server.

        .. raise: InvalidArgumentValue

        :param type argument_value: argument data
        :param type valid_values: regular expression pattern

        :return: argument validation
        :rtype: bool
        """
        if not argument_value or not re.match(regex_pattern, argument_value):
            raise InvalidArgumentValue(self.__class__.__name__,
                                       argument_value,
                                       regex_pattern)
        return True

    @abstractmethod
    def control(self):
        """Validate arguments of methods (input).

        .. note: Should be implemented based on requirements

        :return: None
        :rtype: None
        """
        pass
