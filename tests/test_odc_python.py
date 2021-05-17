import datetime as dt

from odc_python import ODCharts


def test_get_single_chart() -> None:
    odc = ODCharts()
    date = dt.date(year=2019, month=9, day=24)
    chart_df = odc.get_single_charts(date)
    assert chart_df.iloc[1]["info-artist"] == "Apache 207"


def test_get_album_chart() -> None:
    odc = ODCharts()
    date = dt.date(year=2019, month=9, day=24)
    chart_df = odc.get_album_charts(date)
    assert chart_df.iloc[1]["info-artist"] == "Trettmann & KitschKrieg"


def test_get_year_album_chart() -> None:
    odc = ODCharts()
    year = 2019
    chart_df = odc.get_year_album_charts(year)
    assert chart_df.iloc[4]["info-artist"] == "Andrea Berg"


def test_get_current_single_chart() -> None:
    odc = ODCharts()
    chart_df = odc.get_single_charts()
    assert len(chart_df) == 10


def test_get_current_year_chart() -> None:
    odc = ODCharts()
    chart_df = odc.get_single_charts()
    assert len(chart_df) == 10
