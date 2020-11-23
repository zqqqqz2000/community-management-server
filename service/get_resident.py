from dao.resident_information import ResidentInformation
from typing import *


def get_all_resident():
    query_res = ResidentInformation.query.filter_by()
    residents: List[ResidentInformation] = query_res.all()
    result: List[Dict[str, Union[str, int]]] = [{
        'id': resident.id,
        'username': resident.username,
        'phone_number': resident.phone_number,
        'name': resident.name,
        'job': resident.job,
        'actions': None
    } for resident in residents]
    return result


def query_residents(**opt):
    query_res = ResidentInformation.query.filter_by(**opt)
    residents: List[ResidentInformation] = query_res.all()
    result: List[Dict[str, Union[str, int]]] = [{
        'id': resident.id,
        'username': resident.username,
        'phone_number': resident.phone_number,
        'name': resident.name,
        'job': resident.job,
        'actions': None
    } for resident in residents]
    return result


def get_resident(username: str):
    query_res = ResidentInformation.query.filter_by(username=username)
    resident: Optional[ResidentInformation] = query_res.first()
    result: Dict[str, Union[str, int]] = {
        'id': resident.id,
        'username': resident.username,
        'phone_number': resident.phone_number,
        'name': resident.name,
        'job': resident.job,
        'actions': None
    }
    return result
