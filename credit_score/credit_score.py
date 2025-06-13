from fastapi import APIRouter

from constants import USER_INFO

router = APIRouter(
    prefix="/get-credit-score",
    tags=["credit score"]
)

# API endpoint
@router.get("")
def get_dummy_json(name: str, ssn: int, email: str, phoneNumber: int):
    USER_INFO["email"] = email
    USER_INFO["phoneNumber"] = phoneNumber
    USER_INFO["name"] = name
    USER_INFO["ssn"] = ssn

    if ssn is 1:
        return {
            "creditHistoryStatus": 0
        }
    elif ssn is 2:
        return {
            "creditHistoryStatus": 1
        }
    elif ssn is 3:
        return {
            "creditHistoryStatus": 2
        }
    return {
        "creditHistoryStatus": 1
    }
