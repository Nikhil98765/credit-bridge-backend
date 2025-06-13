from fastapi.responses import JSONResponse
import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter(
    prefix="/get-credit-score",
    tags=["credit score"]
)

# API endpoint
@router.get("")
def get_dummy_json(name: str, ssn: int, email: str, phoneNumber: int):
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
    return {"error": "File not found"}
