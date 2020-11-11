from dao.house_information import HouseInformation
from dao.rh import RH
from global_var import db
from typing import *


def delete_houses(ids: List[int]):
    HouseInformation.query.filter(
        HouseInformation.id.in_(ids)
    ).delete(synchronize_session=False)
    db.session.commit()


def delete_rh(rhid: int) -> bool:
    rh = RH.query.filter_by(id=rhid).first()
    if not rh:
        return False
    db.session.delete(rh)
    db.session.commit()
    return True
