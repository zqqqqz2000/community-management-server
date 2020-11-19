from dao.maintenance_information import MaintenanceInformation
from global_var import db


def delete_maintenance(mid: int):
    m = MaintenanceInformation.query.filter_by(id=mid).first()
    db.session.delete(m)
    db.session.commit()
