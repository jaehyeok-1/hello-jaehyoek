from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="KBO Rainout Predictor")


class PredictRequest(BaseModel):
    date: str = Field(..., description="YYYY-MM-DD")
    stadium: str
    game_time: str | None = Field(default=None, description="HH:MM")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(req: PredictRequest) -> dict:
    """Baseline placeholder.

    실제 구현에서는:
    1) date/stadium 기준으로 기상 feature 생성
    2) 저장된 모델 로드
    3) 우취 확률 및 설명 값 반환
    """

    # TODO: model inference 연결
    return {
        "date": req.date,
        "stadium": req.stadium,
        "rainout_probability": 0.42,
        "reason": [
            "경기시간대 예상 강수량 높음",
            "습도/풍속 조합이 과거 우취 사례와 유사",
        ],
    }
