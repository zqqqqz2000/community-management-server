from dao.house_information import HouseInformation
from global_var import db
from typing import *


def delete_houses(ids: List[int]):
    HouseInformation.query.filter(
        HouseInformation.id.in_(ids)
    ).delete(synchronize_session=False)
    db.session.commit()
