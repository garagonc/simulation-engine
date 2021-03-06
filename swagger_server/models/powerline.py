# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Powerline(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, bus1: str=None, phases: int=None, bus2: str=None, length: float=None, unitlength: str=None, linecode: str=None, r1: float=None, r0: float=None, x1: float=None, x0: float=None, c1: float=None, c0: float=None, switch: bool=False):  # noqa: E501
        """Powerline - a model defined in Swagger

        :param id: The id of this Powerline.  # noqa: E501
        :type id: str
        :param bus1: The bus1 of this Powerline.  # noqa: E501
        :type bus1: str
        :param phases: The phases of this Powerline.  # noqa: E501
        :type phases: int
        :param bus2: The bus2 of this Powerline.  # noqa: E501
        :type bus2: str
        :param length: The length of this Powerline.  # noqa: E501
        :type length: float
        :param unitlength: The unitlength of this Powerline.  # noqa: E501
        :type unitlength: str
        :param linecode: The linecode of this Powerline.  # noqa: E501
        :type linecode: str
        :param r1: The r1 of this Powerline.  # noqa: E501
        :type r1: float
        :param r0: The r0 of this Powerline.  # noqa: E501
        :type r0: float
        :param x1: The x1 of this Powerline.  # noqa: E501
        :type x1: float
        :param x0: The x0 of this Powerline.  # noqa: E501
        :type x0: float
        :param c1: The c1 of this Powerline.  # noqa: E501
        :type c1: float
        :param c0: The c0 of this Powerline.  # noqa: E501
        :type c0: float
        :param switch: The switch of this Powerline.  # noqa: E501
        :type switch: bool
        """
        self.swagger_types = {
            'id': str,
            'bus1': str,
            'phases': int,
            'bus2': str,
            'length': float,
            'unitlength': str,
            'linecode': str,
            'r1': float,
            'r0': float,
            'x1': float,
            'x0': float,
            'c1': float,
            'c0': float,
            'switch': bool
        }

        self.attribute_map = {
            'id': 'id',
            'bus1': 'bus1',
            'phases': 'phases',
            'bus2': 'bus2',
            'length': 'length',
            'unitlength': 'unitlength',
            'linecode': 'linecode',
            'r1': 'r1',
            'r0': 'r0',
            'x1': 'x1',
            'x0': 'x0',
            'c1': 'c1',
            'c0': 'c0',
            'switch': 'switch'
        }

        self._id = id
        self._bus1 = bus1
        self._phases = phases
        self._bus2 = bus2
        self._length = length
        self._unitlength = unitlength
        self._linecode = linecode
        self._r1 = r1
        self._r0 = r0
        self._x1 = x1
        self._x0 = x0
        self._c1 = c1
        self._c0 = c0
        self._switch = switch

    @classmethod
    def from_dict(cls, dikt) -> 'Powerline':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Powerline of this Powerline.  # noqa: E501
        :rtype: Powerline
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Powerline.


        :return: The id of this Powerline.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Powerline.


        :param id: The id of this Powerline.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def bus1(self) -> str:
        """Gets the bus1 of this Powerline.

        ID for the connected node  # noqa: E501

        :return: The bus1 of this Powerline.
        :rtype: str
        """
        return self._bus1

    @bus1.setter
    def bus1(self, bus1: str):
        """Sets the bus1 of this Powerline.

        ID for the connected node  # noqa: E501

        :param bus1: The bus1 of this Powerline.
        :type bus1: str
        """
        if bus1 is None:
            raise ValueError("Invalid value for `bus1`, must not be `None`")  # noqa: E501

        self._bus1 = bus1

    @property
    def phases(self) -> int:
        """Gets the phases of this Powerline.


        :return: The phases of this Powerline.
        :rtype: int
        """
        return self._phases

    @phases.setter
    def phases(self, phases: int):
        """Sets the phases of this Powerline.


        :param phases: The phases of this Powerline.
        :type phases: int
        """
        if phases is None:
            raise ValueError("Invalid value for `phases`, must not be `None`")  # noqa: E501

        self._phases = phases

    @property
    def bus2(self) -> str:
        """Gets the bus2 of this Powerline.

        ID for the connected node  # noqa: E501

        :return: The bus2 of this Powerline.
        :rtype: str
        """
        return self._bus2

    @bus2.setter
    def bus2(self, bus2: str):
        """Sets the bus2 of this Powerline.

        ID for the connected node  # noqa: E501

        :param bus2: The bus2 of this Powerline.
        :type bus2: str
        """
        if bus2 is None:
            raise ValueError("Invalid value for `bus2`, must not be `None`")  # noqa: E501

        self._bus2 = bus2

    @property
    def length(self) -> float:
        """Gets the length of this Powerline.


        :return: The length of this Powerline.
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length: float):
        """Sets the length of this Powerline.


        :param length: The length of this Powerline.
        :type length: float
        """

        self._length = length

    @property
    def unitlength(self) -> str:
        """Gets the unitlength of this Powerline.


        :return: The unitlength of this Powerline.
        :rtype: str
        """
        return self._unitlength

    @unitlength.setter
    def unitlength(self, unitlength: str):
        """Sets the unitlength of this Powerline.


        :param unitlength: The unitlength of this Powerline.
        :type unitlength: str
        """

        self._unitlength = unitlength

    @property
    def linecode(self) -> str:
        """Gets the linecode of this Powerline.


        :return: The linecode of this Powerline.
        :rtype: str
        """
        return self._linecode

    @linecode.setter
    def linecode(self, linecode: str):
        """Sets the linecode of this Powerline.


        :param linecode: The linecode of this Powerline.
        :type linecode: str
        """

        self._linecode = linecode

    @property
    def r1(self) -> float:
        """Gets the r1 of this Powerline.


        :return: The r1 of this Powerline.
        :rtype: float
        """
        return self._r1

    @r1.setter
    def r1(self, r1: float):
        """Sets the r1 of this Powerline.


        :param r1: The r1 of this Powerline.
        :type r1: float
        """

        self._r1 = r1

    @property
    def r0(self) -> float:
        """Gets the r0 of this Powerline.


        :return: The r0 of this Powerline.
        :rtype: float
        """
        return self._r0

    @r0.setter
    def r0(self, r0: float):
        """Sets the r0 of this Powerline.


        :param r0: The r0 of this Powerline.
        :type r0: float
        """

        self._r0 = r0

    @property
    def x1(self) -> float:
        """Gets the x1 of this Powerline.


        :return: The x1 of this Powerline.
        :rtype: float
        """
        return self._x1

    @x1.setter
    def x1(self, x1: float):
        """Sets the x1 of this Powerline.


        :param x1: The x1 of this Powerline.
        :type x1: float
        """

        self._x1 = x1

    @property
    def x0(self) -> float:
        """Gets the x0 of this Powerline.


        :return: The x0 of this Powerline.
        :rtype: float
        """
        return self._x0

    @x0.setter
    def x0(self, x0: float):
        """Sets the x0 of this Powerline.


        :param x0: The x0 of this Powerline.
        :type x0: float
        """

        self._x0 = x0

    @property
    def c1(self) -> float:
        """Gets the c1 of this Powerline.


        :return: The c1 of this Powerline.
        :rtype: float
        """
        return self._c1

    @c1.setter
    def c1(self, c1: float):
        """Sets the c1 of this Powerline.


        :param c1: The c1 of this Powerline.
        :type c1: float
        """

        self._c1 = c1

    @property
    def c0(self) -> float:
        """Gets the c0 of this Powerline.


        :return: The c0 of this Powerline.
        :rtype: float
        """
        return self._c0

    @c0.setter
    def c0(self, c0: float):
        """Sets the c0 of this Powerline.


        :param c0: The c0 of this Powerline.
        :type c0: float
        """

        self._c0 = c0

    @property
    def switch(self) -> bool:
        """Gets the switch of this Powerline.


        :return: The switch of this Powerline.
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch: bool):
        """Sets the switch of this Powerline.


        :param switch: The switch of this Powerline.
        :type switch: bool
        """

        self._switch = switch
