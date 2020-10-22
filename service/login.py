from dao.property_management_information import PropertyManagementInformation
from dao.resident_information import ResidentInformation
import hashlib


def property_login(username: str, password: str) -> bool:
    password_m = hashlib.md5(password.encode())
    password_hash = password_m.hexdigest()
    query_res: PropertyManagementInformation = PropertyManagementInformation.query.filter_by(username=username,
                                                                                             password=password_hash)
    prop_manage: PropertyManagementInformation = query_res.first()
    return bool(prop_manage)


def resident_login(username: str, password: str) -> bool:
    password_m = hashlib.md5(password.encode())
    password_hash = password_m.hexdigest()
    query_res: ResidentInformation = ResidentInformation.query.filter_by(username=username,
                                                                         password=password_hash)
    res_manage: ResidentInformation = query_res.first()
    return bool(res_manage)
