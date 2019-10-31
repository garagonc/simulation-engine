# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401
from swagger_server.models.currents import Currents
from swagger_server.models.losses import Losses
from swagger_server.models.powers import Powers
from swagger_server.models.voltages import Voltages
from swagger_server.models.base_model_ import Model
from swagger_server.models.error import Error  # noqa: F401,E501
from swagger_server.models.voltage import Voltage  # noqa: F401,E501
from swagger_server import util


class SimulationResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, currents: Currents=None, losses: Losses=None, powers: Powers=None, voltages: Voltages=None):  # noqa: E501
        """SimulationResult - a model defined in Swagger

        :param currents: The currents of this SimulationResult.  # noqa: E501
        :type currents: Currents
        :param losses: The losses of this SimulationResult.  # noqa: E501
        :type losses: Losses
        :param powers: The powers of this SimulationResult.  # noqa: E501
        :type powers: Powers
        :param voltages: The voltages of this SimulationResult.  # noqa: E501
        :type voltages: Voltages
        """
        self.swagger_types = {
            'currents': Currents,
            'losses': Losses,
            'powers': Powers,
            'voltages': Voltages
        }

        self.attribute_map = {
            'currents': 'currents',
            'losses': 'losses',
            'powers': 'powers',
            'voltages': 'voltages'
        }

        self._currents = currents
        self._losses = losses
        self._powers = powers
        self._voltages = voltages

    @classmethod
    def from_dict(cls, dikt) -> 'SimulationResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimulationResult of this SimulationResult.  # noqa: E501
        :rtype: SimulationResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def currents(self) -> Currents:
        """Gets the currents of this SimulationResult.


        :return: The currents of this SimulationResult.
        :rtype: Currents
        """
        return self._currents

    @currents.setter
    def currents(self, currents: Currents):
        """Sets the currents of this SimulationResult.


        :param currents: The currents of this SimulationResult.
        :type currents: Currents
        """

        self._currents = currents

    @property
    def losses(self) -> Losses:
        """Gets the losses of this SimulationResult.


        :return: The losses of this SimulationResult.
        :rtype: Losses
        """
        return self._losses

    @losses.setter
    def losses(self, losses: Losses):
        """Sets the losses of this SimulationResult.


        :param losses: The losses of this SimulationResult.
        :type losses: Losses
        """

        self._losses = losses

    @property
    def powers(self) -> Powers:
        """Gets the powers of this SimulationResult.


        :return: The powers of this SimulationResult.
        :rtype: Powers
        """
        return self._powers

    @powers.setter
    def powers(self, powers: Powers):
        """Sets the powers of this SimulationResult.


        :param powers: The powers of this SimulationResult.
        :type powers: Powers
        """

        self._powers = powers

    @property
    def voltages(self) -> Voltages:
        """Gets the voltages of this SimulationResult.


        :return: The voltages of this SimulationResult.
        :rtype: Voltages
        """
        return self._voltages

    @voltages.setter
    def voltages(self, voltages: Voltages):
        """Sets the voltages of this SimulationResult.


        :param voltages: The voltages of this SimulationResult.
        :type voltages: Voltages
        """

        self._voltages = voltages
