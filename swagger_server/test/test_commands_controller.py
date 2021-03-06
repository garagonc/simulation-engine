# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.simulation import Simulation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommandsController(BaseTestCase):
    """CommandsController integration test stubs"""

    def test_abort_simulation(self):
        """Test case for abort_simulation

        Aborts a running simulation
        """
        response = self.client.open(
            '/se/commands/abort/{id}'.format(id='id_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_simulation_status(self):
        """Test case for get_simulation_status

        Get the status of the simulation
        """
        response = self.client.open(
            '/se/commands/status/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_simulation(self):
        """Test case for run_simulation

        Runs a simulation
        """
        body = Simulation()
        response = self.client.open(
            '/se/commands/run/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
