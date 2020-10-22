from dao.resident_information import ResidentInformation
from global_var import db
import hashlib


def add_resident(
        username: str,
        password: str,
        phone_number: str,
        name: str,
        job: str
):
    m = hashlib.md5(password.encode())
    pass_hash = m.hexdigest()
    query_res = ResidentInformation.query.filter_by(username=username)
    resident_information = query_res.first()
    if not resident_information:
        resident_information = ResidentInformation(
            username=username,
            password=pass_hash,
            phone_number=phone_number,
            name=name,
            job=job
        )
        db.session.add(resident_information)
    else:
        if password != 'do_not_change':
            resident_information.password = pass_hash
        resident_information.username = username
        resident_information.phone_number = phone_number
        resident_information.name = name
        resident_information.job = job
    db.session.commit()
