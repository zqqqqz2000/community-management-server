from dao.house_information import HouseInformation
from global_var import db, sessionmaker
from flask_sqlalchemy import orm
from dao.maintenance_information import MaintenanceInformation


@db.event.listens_for(MaintenanceInformation, 'before_update')
def before_maintenance_update(mapper, connection, target: MaintenanceInformation):
    # 是否从维修基金扣除
    if target.from_balance:
        session = orm.object_session(target)
        h: HouseInformation = db.session.query(HouseInformation).filter(
            HouseInformation.id == target.hid
        ).first()
        # 余额充足
        if h.maintenance_balance >= target.pay_amount:
            ht = h.__table__
            connection.execute(
                ht.update(ht.c.id == target.hid).values(
                    maintenance_balance=ht.c.maintenance_balance - target.pay_amount
                )
            )
            return
        session.rollback()
