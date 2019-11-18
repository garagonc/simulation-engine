# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta import Meta
from swagger_server import util


class Photovoltaic(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, inverter_efficiency: float=None, phases: int=None, power: float=None, max_power_k_w: float=None, powerunit: str=None, powerfactor: float=None, bus1: str=None, k_v: float=None, effcurve: str=None, ptcurve: str=None, daily: str=None, tdaily: str=None, temperature: float=None, irrad: float=None, voltageunit: str=None, power_profile_id: str=None, control_strategy: str='no_control', meta: Meta=None):  # noqa: E501
        """Photovoltaic - a model defined in Swagger

        :param id: The id of this Photovoltaic.  # noqa: E501
        :type id: str
        :param inverter_efficiency: The inverter_efficiency of this Photovoltaic.  # noqa: E501
        :type inverter_efficiency: float
        :param phases: The phases of this Photovoltaic.  # noqa: E501
        :type phases: int
        :param power: The power of this Photovoltaic.  # noqa: E501
        :type power: float
        :param max_power_k_w: The max_power_k_w of this Photovoltaic.  # noqa: E501
        :type max_power_k_w: float
        :param powerunit: The powerunit of this Photovoltaic.  # noqa: E501
        :type powerunit: str
        :param powerfactor: The powerfactor of this Photovoltaic.  # noqa: E501
        :type powerfactor: float
        :param bus1: The bus1 of this Photovoltaic.  # noqa: E501
        :type bus1: str
        :param k_v: The k_v of this Photovoltaic.  # noqa: E501
        :type k_v: float
        :param effcurve: The effcurve of this Photovoltaic.  # noqa: E501
        :type effcurve: str
        :param ptcurve: The ptcurve of this Photovoltaic.  # noqa: E501
        :type ptcurve: str
        :param daily: The daily of this Photovoltaic.  # noqa: E501
        :type daily: str
        :param tdaily: The tdaily of this Photovoltaic.  # noqa: E501
        :type tdaily: str
        :param temperature: The temperature of this Photovoltaic.  # noqa: E501
        :type temperature: float
        :param irrad: The irrad of this Photovoltaic.  # noqa: E501
        :type irrad: float
        :param voltageunit: The voltageunit of this Photovoltaic.  # noqa: E501
        :type voltageunit: str
        :param power_profile_id: The power_profile_id of this Photovoltaic.  # noqa: E501
        :type power_profile_id: str
        :param control_strategy: The control_strategy of this Photovoltaic.  # noqa: E501
        :type control_strategy: str
        :param meta: The meta of this Photovoltaic.  # noqa: E501
        :type meta: Meta
        """
        self.swagger_types = {
            'id': str,
            'inverter_efficiency': float,
            'phases': int,
            'power': float,
            'max_power_k_w': float,
            'powerunit': str,
            'powerfactor': float,
            'bus1': str,
            'k_v': float,
            'effcurve': str,
            'ptcurve': str,
            'daily': str,
            'tdaily': str,
            'temperature': float,
            'irrad': float,
            'voltageunit': str,
            'power_profile_id': str,
            'control_strategy': str,
            'meta': Meta
        }

        self.attribute_map = {
            'id': 'id',
            'inverter_efficiency': 'inverterEfficiency',
            'phases': 'phases',
            'power': 'power',
            'max_power_k_w': 'max_power_kW',
            'powerunit': 'powerunit',
            'powerfactor': 'powerfactor',
            'bus1': 'bus1',
            'k_v': 'kV',
            'effcurve': 'effcurve',
            'ptcurve': 'ptcurve',
            'daily': 'daily',
            'tdaily': 'tdaily',
            'temperature': 'temperature',
            'irrad': 'irrad',
            'voltageunit': 'voltageunit',
            'power_profile_id': 'power_profile_id',
            'control_strategy': 'control_strategy',
            'meta': 'meta'
        }

        self._id = id
        self._inverter_efficiency = inverter_efficiency
        self._phases = phases
        self._power = power
        self._max_power_k_w = max_power_k_w
        self._powerunit = powerunit
        self._powerfactor = powerfactor
        self._bus1 = bus1
        self._k_v = k_v
        self._effcurve = effcurve
        self._ptcurve = ptcurve
        self._daily = daily
        self._tdaily = tdaily
        self._temperature = temperature
        self._irrad = irrad
        self._voltageunit = voltageunit
        self._power_profile_id = power_profile_id
        self._control_strategy = control_strategy
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'Photovoltaic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Photovoltaic of this Photovoltaic.  # noqa: E501
        :rtype: Photovoltaic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Photovoltaic.


        :return: The id of this Photovoltaic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Photovoltaic.


        :param id: The id of this Photovoltaic.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inverter_efficiency(self) -> float:
        """Gets the inverter_efficiency of this Photovoltaic.


        :return: The inverter_efficiency of this Photovoltaic.
        :rtype: float
        """
        return self._inverter_efficiency

    @inverter_efficiency.setter
    def inverter_efficiency(self, inverter_efficiency: float):
        """Sets the inverter_efficiency of this Photovoltaic.


        :param inverter_efficiency: The inverter_efficiency of this Photovoltaic.
        :type inverter_efficiency: float
        """

        self._inverter_efficiency = inverter_efficiency

    @property
    def phases(self) -> int:
        """Gets the phases of this Photovoltaic.


        :return: The phases of this Photovoltaic.
        :rtype: int
        """
        return self._phases

    @phases.setter
    def phases(self, phases: int):
        """Sets the phases of this Photovoltaic.


        :param phases: The phases of this Photovoltaic.
        :type phases: int
        """
        if phases is None:
            raise ValueError("Invalid value for `phases`, must not be `None`")  # noqa: E501

        self._phases = phases

    @property
    def power(self) -> float:
        """Gets the power of this Photovoltaic.


        :return: The power of this Photovoltaic.
        :rtype: float
        """
        return self._power

    @power.setter
    def power(self, power: float):
        """Sets the power of this Photovoltaic.


        :param power: The power of this Photovoltaic.
        :type power: float
        """

        self._power = power

    @property
    def max_power_k_w(self) -> float:
        """Gets the max_power_k_w of this Photovoltaic.


        :return: The max_power_k_w of this Photovoltaic.
        :rtype: float
        """
        return self._max_power_k_w

    @max_power_k_w.setter
    def max_power_k_w(self, max_power_k_w: float):
        """Sets the max_power_k_w of this Photovoltaic.


        :param max_power_k_w: The max_power_k_w of this Photovoltaic.
        :type max_power_k_w: float
        """
        if max_power_k_w is None:
            raise ValueError("Invalid value for `max_power_k_w`, must not be `None`")  # noqa: E501

        self._max_power_k_w = max_power_k_w

    @property
    def powerunit(self) -> str:
        """Gets the powerunit of this Photovoltaic.


        :return: The powerunit of this Photovoltaic.
        :rtype: str
        """
        return self._powerunit

    @powerunit.setter
    def powerunit(self, powerunit: str):
        """Sets the powerunit of this Photovoltaic.


        :param powerunit: The powerunit of this Photovoltaic.
        :type powerunit: str
        """

        self._powerunit = powerunit

    @property
    def powerfactor(self) -> float:
        """Gets the powerfactor of this Photovoltaic.


        :return: The powerfactor of this Photovoltaic.
        :rtype: float
        """
        return self._powerfactor

    @powerfactor.setter
    def powerfactor(self, powerfactor: float):
        """Sets the powerfactor of this Photovoltaic.


        :param powerfactor: The powerfactor of this Photovoltaic.
        :type powerfactor: float
        """

        self._powerfactor = powerfactor

    @property
    def bus1(self) -> str:
        """Gets the bus1 of this Photovoltaic.


        :return: The bus1 of this Photovoltaic.
        :rtype: str
        """
        return self._bus1

    @bus1.setter
    def bus1(self, bus1: str):
        """Sets the bus1 of this Photovoltaic.


        :param bus1: The bus1 of this Photovoltaic.
        :type bus1: str
        """
        if bus1 is None:
            raise ValueError("Invalid value for `bus1`, must not be `None`")  # noqa: E501

        self._bus1 = bus1

    @property
    def k_v(self) -> float:
        """Gets the k_v of this Photovoltaic.


        :return: The k_v of this Photovoltaic.
        :rtype: float
        """
        return self._k_v

    @k_v.setter
    def k_v(self, k_v: float):
        """Sets the k_v of this Photovoltaic.


        :param k_v: The k_v of this Photovoltaic.
        :type k_v: float
        """
        if k_v is None:
            raise ValueError("Invalid value for `k_v`, must not be `None`")  # noqa: E501

        self._k_v = k_v

    @property
    def effcurve(self) -> str:
        """Gets the effcurve of this Photovoltaic.


        :return: The effcurve of this Photovoltaic.
        :rtype: str
        """
        return self._effcurve

    @effcurve.setter
    def effcurve(self, effcurve: str):
        """Sets the effcurve of this Photovoltaic.


        :param effcurve: The effcurve of this Photovoltaic.
        :type effcurve: str
        """

        self._effcurve = effcurve

    @property
    def ptcurve(self) -> str:
        """Gets the ptcurve of this Photovoltaic.


        :return: The ptcurve of this Photovoltaic.
        :rtype: str
        """
        return self._ptcurve

    @ptcurve.setter
    def ptcurve(self, ptcurve: str):
        """Sets the ptcurve of this Photovoltaic.


        :param ptcurve: The ptcurve of this Photovoltaic.
        :type ptcurve: str
        """

        self._ptcurve = ptcurve

    @property
    def daily(self) -> str:
        """Gets the daily of this Photovoltaic.


        :return: The daily of this Photovoltaic.
        :rtype: str
        """
        return self._daily

    @daily.setter
    def daily(self, daily: str):
        """Sets the daily of this Photovoltaic.


        :param daily: The daily of this Photovoltaic.
        :type daily: str
        """

        self._daily = daily

    @property
    def tdaily(self) -> str:
        """Gets the tdaily of this Photovoltaic.


        :return: The tdaily of this Photovoltaic.
        :rtype: str
        """
        return self._tdaily

    @tdaily.setter
    def tdaily(self, tdaily: str):
        """Sets the tdaily of this Photovoltaic.


        :param tdaily: The tdaily of this Photovoltaic.
        :type tdaily: str
        """

        self._tdaily = tdaily

    @property
    def temperature(self) -> float:
        """Gets the temperature of this Photovoltaic.


        :return: The temperature of this Photovoltaic.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: float):
        """Sets the temperature of this Photovoltaic.


        :param temperature: The temperature of this Photovoltaic.
        :type temperature: float
        """

        self._temperature = temperature

    @property
    def irrad(self) -> float:
        """Gets the irrad of this Photovoltaic.


        :return: The irrad of this Photovoltaic.
        :rtype: float
        """
        return self._irrad

    @irrad.setter
    def irrad(self, irrad: float):
        """Sets the irrad of this Photovoltaic.


        :param irrad: The irrad of this Photovoltaic.
        :type irrad: float
        """

        self._irrad = irrad

    @property
    def voltageunit(self) -> str:
        """Gets the voltageunit of this Photovoltaic.


        :return: The voltageunit of this Photovoltaic.
        :rtype: str
        """
        return self._voltageunit

    @voltageunit.setter
    def voltageunit(self, voltageunit: str):
        """Sets the voltageunit of this Photovoltaic.


        :param voltageunit: The voltageunit of this Photovoltaic.
        :type voltageunit: str
        """

        self._voltageunit = voltageunit

    @property
    def power_profile_id(self) -> str:
        """Gets the power_profile_id of this Photovoltaic.


        :return: The power_profile_id of this Photovoltaic.
        :rtype: str
        """
        return self._power_profile_id

    @power_profile_id.setter
    def power_profile_id(self, power_profile_id: str):
        """Sets the power_profile_id of this Photovoltaic.


        :param power_profile_id: The power_profile_id of this Photovoltaic.
        :type power_profile_id: str
        """

        self._power_profile_id = power_profile_id

    @property
    def control_strategy(self) -> str:
        """Gets the control_strategy of this Photovoltaic.

        Possibilities: no_control, ofw, limit_power, volt-watt, volt-var  # noqa: E501

        :return: The control_strategy of this Photovoltaic.
        :rtype: str
        """
        return self._control_strategy

    @control_strategy.setter
    def control_strategy(self, control_strategy: str):
        """Sets the control_strategy of this Photovoltaic.

        Possibilities: no_control, ofw, limit_power, volt-watt, volt-var  # noqa: E501

        :param control_strategy: The control_strategy of this Photovoltaic.
        :type control_strategy: str
        """

        self._control_strategy = control_strategy

    @property
    def meta(self) -> Meta:
        """Gets the meta of this Photovoltaic.


        :return: The meta of this Photovoltaic.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        """Sets the meta of this Photovoltaic.


        :param meta: The meta of this Photovoltaic.
        :type meta: Meta
        """

        self._meta = meta
