# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.radial import Radial  # noqa: F401,E501
from swagger_server import util


class Grid(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, radials: List[Radial]=None):  # noqa: E501
        """Grid - a model defined in Swagger

        :param radials: The radials of this Grid.  # noqa: E501
        :type radials: List[Radial]
        """
        self.swagger_types = {
            'radials': List[Radial]
        }

        self.attribute_map = {
            'radials': 'radials'
        }

        self._radials = radials

    @classmethod
    def from_dict(cls, dikt) -> 'Grid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Grid of this Grid.  # noqa: E501
        :rtype: Grid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def radials(self) -> List[Radial]:
        """Gets the radials of this Grid.


        :return: The radials of this Grid.
        :rtype: List[Radial]
        """
        return self._radials

    @radials.setter
    def radials(self, radials: List[Radial]):
        """Sets the radials of this Grid.


        :param radials: The radials of this Grid.
        :type radials: List[Radial]
        """

        self._radials = radials
