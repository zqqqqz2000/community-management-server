from dao.maintenance_information import MaintenanceInformation
from global_var import db
from datetime import date


def add_maintenance(hid: int, apply_date: date, comment: str, from_balance: int):
    m = MaintenanceInformation(
        hid=hid,
        apply_date=apply_date,
        comment=comment,
        from_balance=from_balance
    )
    db.session.add(m)
    db.session.commit()
