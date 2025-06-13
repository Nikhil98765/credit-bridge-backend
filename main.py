# main.py

from fastapi import FastAPI

import loan_evaluation
from credit_score import credit_score
from loan_evaluation import loan_evaluation
app = FastAPI()

app.include_router(credit_score.router)
app.include_router(loan_evaluation.router)
