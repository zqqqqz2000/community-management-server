from dao.resident_information import ResidentInformation
from global_var import db
import hashlib
from typing import *


def get_all_resident():
    query_res = ResidentInformation.query.filter_by()
    residents: List[ResidentInformation] = query_res.all()
    result: List[Dict[str, Union[str, int]]] = [{
        'id': resident.id,
        'phone_number': resident.phone_number,
        'name': resident.name,
        'job': resident.job
    } for resident in residents]
    return result
