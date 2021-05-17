# Python "www.offiziellecharts.de" API

Python API for [www.offiziellecharts.de](https://www.offiziellecharts.de).
A minimal toolkit to obtain the top 100 music charts from germany.

## Installation
*Note that you must be using Python >= 3.8*

```
pip install odc-python
```


## Examples

__Get current music charts__
```python
from odc_python import ODCharts
odc = ODCharts()
odc.get_single_charts() # Returns a Pandas Datframe of the top 100 charts.
```

```
                                    info-artist         info-label                      info-title last-week this-week
0      187 Strassenbande, Bonez MC & Frauenarzt  187 Strassenbande                          Extasy                   1
1                                  Nathan Evans            Polydor                       Wellerman         1         2
2                                        Jamule       Life Is Pain               Liege wieder wach         3         3
3  Riton x Nightcrawlers feat. Mufasa & Hypeman           Columbia       Friday (Dopamine Re-Edit)         4         4
4                         Luciano feat. Lil Zey              Urban                           Elmas                   5
5                                     Lil Nas X           Columbia  Montero (Call Me By Your Name)         5         6
6                         Cro feat. Capital Bra              Urban                         Blessed         2         7
7                       P!nk + Willow Sage Hart                RCA            Cover Me In Sunshine         7         8
8                                    The Weeknd   Republic Records                 Save Your Tears         6         9
9               Miksu / Macloud / Jamule / Nimo             Futura                 Frag mich nicht         8        10
```

__Get album charts of a specific date__
```python
from odc_python import ODCharts
import datetime as dt

odc = ODCharts()
date = dt.date(year = 2019, month=9, day=24)
odc.get_album_charts(date)
```

```
                          info-artist                  info-label                             info-title last-week this-week
0                    Andreas Gabalier                   Electrola  10 Jahre - Best Of VolksRock'n'Roller                   1
1             Trettmann & KitschKrieg                         BMG                              Trettmann                   2
2                            Loredana                    Loredana                              King Lori                   3
3                          Die Lochis        Warner Music Germany                              Kapitel X                   4
4                             Olexesh                    385ideal                            Augen Husky                   5
..                                ...                         ...                                    ...       ...       ...
95                         Adel Tawil                         BMG                             Alles lebt        97        96
96                  AnnenMayKantereit  Universal Domestic Vertigo                    Alles nix Konkretes        93        97
97                         Soundtrack                    Atlantic                   The Greatest Showman                  98
98  Mike Patton & Jean-Claude Vannier                        Pias                          Corpse Flower                  99
99                           Bon Iver                  Jagjaguwar                                    i,i        71       100
```

__Get yearly single charts__

```python
from odc_python import ODCharts

odc = ODCharts()
year = 2019
odc.get_year_album_charts(year)
```

```
                                          info-artist                           info-title this-week
0                                           Rammstein                            Rammstein         1
1                                        Sarah Connor                     Herz Kraft Werke         2
2                                      Udo Lindenberg  MTV Unplugged 2 - Live vom Atlantik         3
3                                  Herbert Grönemeyer                               Tumult         4
4                                         Andrea Berg                               Mosaik         5
..                                                ...                                  ...       ...
95                                         Soundtrack                 The Greatest Showman        96
96                                           18 Karat               Je m'appelle kriminell        97
97                            Trettmann & KitschKrieg                            Trettmann        98
98  Helene Fischer & The Royal Philharmonic Orchestra                          Weihnachten        99
99                                      Xavier Naidoo                          Hin und weg       100
```
