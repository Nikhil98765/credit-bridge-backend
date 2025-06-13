from fastapi import APIRouter, File, UploadFile, Form, HTTPException, Query
from typing import Optional, Union
import random

from fastapi.responses import JSONResponse

from constants import USER_INFO

router = APIRouter(
    prefix="/evaluate-loan",
    tags=["evaluate loan"]
)

@router.post("")
async def evaluate_loan(
        loan_amount: float = Query(..., description="Requested loan amount"),
        bank_statements: Optional[UploadFile] = File(None),
        rent_bill: Optional[UploadFile] = File(None),
        insurance_installments: Optional[UploadFile] = File(None),
        seasonal_income: Optional[UploadFile] = File(None),
        investments: Optional[UploadFile] = File(None),
):
    documents_analyzed = sum(
        1 for f in [bank_statements, rent_bill, insurance_installments, seasonal_income, investments] if f
    )

    credit_score = random.randint(30, 85)
    fraud_score = round(random.uniform(0.1, 0.9), 2)
    max_score = 100

    score_label = (
        "Poor" if credit_score < 50 else
        "Fair" if credit_score < 70 else
        "Good"
    )

    risk_level = (
        "High Risk" if credit_score < 50 else
        "Moderate Risk" if credit_score < 70 else
        "Low Risk"
    )

    loan_options = [
        {
            "id": f"loan-option-{i}",
            "type": "Personal Loan" if i % 2 == 0 else "Secured Loan",
            "amount": loan_amount,
            "apr": round(random.uniform(10.0, 20.0), 2),
            "term": random.choice([12, 24, 36]),
            "monthlyPayment": random.randint(300, 700),
            "recommended": i == 0
        }
        for i in range(2)
    ]

    score_factors = [
        {
            "category": "Payment History",
            "impact": "negative",
            "score": random.randint(30, 60),
            "description": "Missed or late payments noted",
            "weight": 35
        },
        {
            "category": "Income Stability",
            "impact": "negative" if credit_score < 50 else "neutral",
            "score": random.randint(40, 65),
            "description": "Seasonal income or inconsistent employment",
            "weight": 25
        },
        {
            "category": "Spending Patterns",
            "impact": "negative",
            "score": random.randint(40, 60),
            "description": "High utilization or frequent overdrafts",
            "weight": 20
        },
        {
            "category": "Account Diversity",
            "impact": "neutral",
            "score": random.randint(50, 70),
            "description": "Limited mix of account types",
            "weight": 10
        },
        {
            "category": "Account Age",
            "impact": "neutral",
            "score": random.randint(55, 70),
            "description": "Moderate account age",
            "weight": 10
        },
    ]

    print(USER_INFO)
    return JSONResponse(content={
        "userDetails": {
            "name": USER_INFO["name"],
            "phoneNumber": USER_INFO["phoneNumber"],
            "email": USER_INFO["email"],
            "ssn": USER_INFO["ssn"],
        },
        "creditScore": {
            "score": credit_score,
            "label": score_label,
            "description": f"Credit profile indicates {risk_level.lower()}",
            "maxScore": max_score
        },
        "assessmentSummary": {
            "documentsAnalyzed": documents_analyzed,
            "processingTimeSeconds": random.randint(3, 10),
            "riskLevel": risk_level,
            "fraudScore": {
                "value": fraud_score,
                "label": "High" if fraud_score > 0.7 else "Moderate" if fraud_score > 0.4 else "Low"
            }
        },
        "loanOptions": loan_options,
        "scoreFactors": score_factors
    })