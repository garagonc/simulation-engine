import connexion
import six
import logging

from swagger_server.models.coordinates import Coordinates  # noqa: E501
from swagger_server.models.grid import Grid  # noqa: E501
from swagger_server import util

from data_management.controller import gridController as gControl


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)

def create_grid(body):  # noqa: E501
    """Insert grid components

     # noqa: E501

    :param body: Created grid. gridID &#x3D; 0 because it is generated server-side
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        logger.debug("Post grid request")
        body = Grid.from_dict(connexion.request.get_json()).to_dict()  # noqa: E501
        logger.info("This is the dictionary: "+ str(body))
        gridController= gControl()
        if "loads" in body.keys() and body["loads"] is not None:
            #body=body.to_dict()
            load=body["loads"]
            gridController.setLoads(load)
        if "transformer" in body.keys() and body["transformer"] is not None:
            transformer=body["transformer"]
            gridController.setTransformers(transformer)
        if "power_lines" in body.keys() and body["power_lines"] is not None \
                and "linecode" in body.keys() and body["linecode"] is not None:
            powerlines = body["power_lines"]
            linecodes =  body["linecode"]
            gridController.setPowerLines(powerlines, linecodes)
        if "photovoltaics" in body.keys() and body["photovoltaics"] is not None \
                and "xycurves" in body.keys() and body["xycurves"] is not None \
                and "loadshapes" in body.keys() and body["loadshapes"] is not None \
                and "tshapes" in body.keys() and body["tshapes"] is not None:
            photovoltaics = body["photovoltaics"]
            xycurves = body["xycurves"]
            loadshapes = body["loadshapes"]
            tshapes = body["tshapes"]
            gridController.setPhotovoltaic(photovoltaics, xycurves, loadshapes, tshapes)
        if "storageUnits" in body.keys() and body["storageUnits"] is not None:
        #body=body.to_dict()
            storage=body["storageUnits"]
            gridController.setStorage(storage)
        if "chargingPoints" in body.keys() and body["chargingPoints"] is not None:
        #body=body.to_dict()
            chargingPoints=body["chargingPoints"]
            gridController.setChargingPoints(chargingPoints)


    return "OK"


def delete_storage(id, body):  # noqa: E501
    """Delete storage

     # noqa: E501

    :param id: Id of the grid
    :type id: int
    :param body: Deleted grid components
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Grid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_grid(id, coordinates=None):  # noqa: E501
    """Get a grid topology

    Get a grid topology by the coordinates of its entry point transformer # noqa: E501

    :param id: Id of the grid
    :type id: int
    :param coordinates: The latitude and longitude coordinates for this grids entry point
    :type coordinates: dict | bytes

    :rtype: Grid
    """
    if connexion.request.is_json:
        coordinates = Coordinates.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_storage(id, body):  # noqa: E501
    """Updated storage

     # noqa: E501

    :param id: Id of the grid
    :type id: int
    :param body: Updated grid components
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Grid.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
