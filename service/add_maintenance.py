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


def pay_maintenance(
        mid: int,
        fix_date,
        fix_number,
        pay_amount,
) -> bool:
    m: MaintenanceInformation = MaintenanceInformation.query.filter_by(id=mid).first()
    m.fix_date = fix_date
    m.fix_number = fix_number
    m.pay_amount = float(pay_amount)
    # 当面结清
    if not m.from_balance:
        return False
    try:
        db.session.commit()
    except Exception as e:
        # 基金且余额不足
        print(e)
        return False
    # 扣费成功
    return True
