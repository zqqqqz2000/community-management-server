from typing import *
from global_var import db
from dao.resident_information import ResidentInformation


def delete_residents(resident_ids: List[int]):
    db.session.query(ResidentInformation).filter(ResidentInformation.id.in_(resident_ids)).delete(
        synchronize_session=False
    )
    db.session.commit()
