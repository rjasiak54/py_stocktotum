import datetime
import io
import logging
import os
import typing

import pandas as pd
import requests


from . import cache

class TimeSeries:
    def __init__(self) -> None:
        pass    

    async def get_daily(
        self,
        symbol: str,
        startdate: str | None = None,
        enddate: typing.Optional[str] = None,
        refresh: bool = True,
    ) -> pd.DataFrame:
        fname = os.path.join("ts-daily-adj", f"{symbol}.csv")
        df = await self._init_av_data(symbol, fname, refresh)
        if startdate is not None and enddate is not None:
            return df.loc[startdate:enddate]  # type: ignore
        if startdate is not None:
            df = df.loc[startdate:]  # type: ignore
        return df


    async def _init_av_data(self, symbol: str, fname: str, refresh: bool = True) -> pd.DataFrame:
        if not cache.exists(fname):
            self._logg(f"{symbol:<8} - No Cache")
        else:
            if refresh and not await cache.is_valid(fname):
                self._logg(f"{symbol:<8} - Cache Expired")
            else:
                self._logg(f"{symbol:<8} - Loading Cache")
                df = await cache.read_csv(fname)
                df = await self._format_df(df)
                return df
        return await self._refresh_from_av(symbol, fname)


    async def _refresh_from_av(self, symbol: str, fname: str) -> pd.DataFrame:
        self._logg(f"{symbol:<8} - Refreshing from AV")
        p = self._get_intraday_params(symbol)
        response = requests.get("https://www.alphavantage.co/query", params=p)
        decoded_content = response.content.decode("utf-8")
        df = pd.read_csv(io.StringIO(decoded_content))
        df = await self._format_df(df)
        cache.write_csv(df, fname)
        return df
    

    async def _format_df(self, df: pd.DataFrame) -> pd.DataFrame:
        print(df)
        df["row_number"] = df.index
        df.set_index("timestamp", inplace=True)
        df.sort_values("timestamp", inplace=True)
        return df


    def _logg(self, msg: str) -> None:
        return
        logging.info(f"[TimeSeries] {msg}")


    def _get_intraday_params(self, symbol: str) -> dict[str, str]:
        return {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "apikey": 'A3KIN32QOLV8SMUL',
            "datatype": "csv",
            "outputsize": "full",
        }
