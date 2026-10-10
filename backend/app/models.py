from typing import Literal

from pydantic import BaseModel, Field


class TickerItem(BaseModel):
    symbol: str = Field(min_length=1, max_length=12)
    label: str = Field(min_length=1, max_length=80)
    value: str = Field(min_length=1, max_length=30)
    change: str = Field(min_length=1, max_length=30)
    direction: Literal["up", "down", "flat"] = "flat"


class TickerContent(BaseModel):
    title: str = Field(default="THE DAILY TICKER", max_length=60)
    location: str = Field(default="NEW YORK, NY", max_length=80)
    weather: str = Field(default="72° · CLEAR", max_length=80)
    headlines: list[str] = Field(default_factory=list, max_length=20)
    watchlist: list[TickerItem] = Field(default_factory=list, max_length=20)
    footer_message: str = Field(default="LOCAL DISPLAY · DATA DELAYED", max_length=160)
