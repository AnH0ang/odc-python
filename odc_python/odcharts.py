import datetime as dt
import time
from typing import List, Optional

import dateutil.relativedelta as rt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


class ODCharts:
    url_template: str = "https://www.offiziellecharts.de/charts/{type}/for-date-{date}"

    def __init__(self) -> None:
        pass

    def get_single_charts(self, date: Optional[dt.date] = None) -> pd.DataFrame:
        """Returns the top 100 single charts a pandas dataframe for the given date.

        Args:
            date: date of the music chart.

        Returns:
            the top 100 music chart for the given date
        """

        url = self.url_template.format(type="single", date=self._get_timestamp(date))
        span_class_names = ["this-week", "last-week", "info-artist", "info-title", "info-label"]
        return self._get_chart_df(url, span_class_names)

    def get_album_charts(self, date: Optional[dt.date]) -> pd.DataFrame:
        """Returns the top 100 album charts a pandas dataframe for the given date.

        Args:
            date: date of the music chart.

        Returns:
            the top 100 music chart for the given date
        """

        url = self.url_template.format(type="album", date=self._get_timestamp(date))
        span_class_names = ["this-week", "last-week", "info-artist", "info-title", "info-label"]
        return self._get_chart_df(url, span_class_names)

    def get_dance_charts(self, date: Optional[dt.date]) -> pd.DataFrame:
        """Returns the top 100 dance charts a pandas dataframe for the given date.

        Args:
            date: date of the music chart.

        Returns:
            the top 100 music chart for the given date
        """

        url = self.url_template.format(type="dance", date=self._get_timestamp(date))
        span_class_names = ["this-week", "last-week", "info-artist", "info-title", "info-label"]
        return self._get_chart_df(url, span_class_names)

    def get_year_single_charts(self, year: int) -> pd.DataFrame:
        """Returns the top 100 single charts a pandas dataframe for the given year.

        Args:
            year: year of the music chart.

        Returns:
            the top 100 music chart for the given date
        """

        url = self.url_template.format(type="single-jahr", date=str(year))
        span_class_names = ["this-week", "info-artist", "info-title"]
        return self._get_chart_df(url, span_class_names)

    def get_year_album_charts(self, year: int) -> pd.DataFrame:
        """Returns the top 100 album charts a pandas dataframe for the given year.

        Args:
            year: year of the music chart.

        Returns:
            the top 100 music chart for the given date
        """

        url = self.url_template.format(type="album-jahr", date=str(year))
        span_class_names = ["this-week", "info-artist", "info-title"]
        return self._get_chart_df(url, span_class_names)

    def _get_timestamp(self, date: Optional[dt.date]) -> str:
        date = date if date is not None else dt.date.today()
        next_thursday = date + rt.relativedelta(days=0, weekday=rt.TH)
        timestamp = int(time.mktime(next_thursday.timetuple()))
        return str(timestamp).ljust(13, "0")

    def _get_chart_df(self, url: str, span_class_names: List[str]) -> pd.DataFrame:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="html.parser")

        charts_df = pd.DataFrame()
        chart_items = soup.find("table", attrs={"class": "table chart-table"}).find_all("tr")

        for item in chart_items:
            item_vals = []
            for c in span_class_names:
                val = item.find("span", attrs={"class": c}).string
                item_vals.append(val.strip() if val else "")
            item_info = pd.Series(item_vals, span_class_names)
            charts_df = charts_df.append(item_info, ignore_index=True)

        charts_df.replace("", np.nan)
        return charts_df
