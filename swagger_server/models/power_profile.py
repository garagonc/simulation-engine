# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PowerProfile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, items: float=None):  # noqa: E501
        """PowerProfile - a model defined in Swagger

        :param id: The id of this PowerProfile.  # noqa: E501
        :type id: str
        :param items: The items of this PowerProfile.  # noqa: E501
        :type items: float
        """
        self.swagger_types = {
            'id': str,
            'items': float
        }

        self.attribute_map = {
            'id': 'id',
            'items': 'items'
        }

        self._id = id
        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'PowerProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PowerProfile of this PowerProfile.  # noqa: E501
        :rtype: PowerProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this PowerProfile.


        :return: The id of this PowerProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this PowerProfile.


        :param id: The id of this PowerProfile.
        :type id: str
        """

        self._id = id

    @property
    def items(self) -> float:
        """Gets the items of this PowerProfile.


        :return: The items of this PowerProfile.
        :rtype: float
        """
        return self._items

    @items.setter
    def items(self, items: float):
        """Sets the items of this PowerProfile.


        :param items: The items of this PowerProfile.
        :type items: float
        """

        self._items = items
