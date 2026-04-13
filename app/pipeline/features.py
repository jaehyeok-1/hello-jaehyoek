from dataclasses import dataclass


@dataclass
class GameWeatherFeature:
    game_id: str
    precip_3h_sum: float
    precip_6h_sum: float
    humidity_avg_3h: float
    wind_max_3h: float
    temp_avg_3h: float


def build_features() -> None:
    """게임/날씨 원천 데이터를 결합해 feature 테이블을 만든다.

    구현 포인트:
    - 경기 시작 전 N시간 window 기준 통계
    - 누출 방지를 위한 cut-off strict 적용
    - 결측치 처리 및 스케일링 기준 기록
    """

    # TODO: DB에서 games/weather 로드 후 feature 생성
    pass
