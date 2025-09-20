from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from services.calculator_brute_force import calculate_management_fee_per_shareholder  as calculate_management_fee_per_shareholder_brute_force
from services.calculator_numpy import calculate_management_fee_per_shareholder


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

@app.post("/calcular-taxa-administrativa-por-cotista-brute-force", response_model=List[float])
def evaluate_fee_per_investor_brute_force(data: InvestmentData):

    input_dict = data.model_dump()

    management_fee_result = calculate_management_fee_per_shareholder_brute_force(input_dict)


    return management_fee_result
