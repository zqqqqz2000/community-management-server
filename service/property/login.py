from dao.property_management_information import PropertyManagementInformation
import hashlib


def property_login(username: str, password: str) -> bool:
    password_m = hashlib.md5(password.encode())
    password_hash = password_m.hexdigest()
    query_res: PropertyManagementInformation = PropertyManagementInformation.query.filter_by(username=username,
                                                                                             password=password_hash)
    prop_manage: PropertyManagementInformation = query_res.first()
    return bool(prop_manage)
