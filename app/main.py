from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# from app.calculator_brute_force import calculate_management_fee_per_shareholder
from calculator_numpy import calculate_management_fee_per_shareholder


class DailyData(BaseModel):
    valor: float
    quantidades: List[float]


class InvestmentData(BaseModel):
    taxa: float
    cotas: List[DailyData]


app = FastAPI()

@app.get("/")
def root():
    return {"System": "Backend Sparta Challenge", "Version": "1.0.0"}


@app.post("/calcular-taxa-administrativa-por-cotista", response_model=List[float])
def evaluate_fee_per_investor(data: InvestmentData):

    input_dict = data.model_dump()

    management_fee_result = calculate_management_fee_per_shareholder(input_dict)

    return management_fee_result
