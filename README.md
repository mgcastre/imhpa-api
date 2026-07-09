# IMHPA API

A lightweight, independnetly developed, Python client for accessing and downloading data from the Meteorological and Hydrological Institute of Panama ([IMHPA's](https://www.imhpa.gob.pa/)).

## Data Source

This tool accesses real time hydr [IMHPA's](https://www.imhpa.gob.pa/) public gauge network, which operates hundreds of automated meteorological stations across Panama.

**What you get:**
- **Sensors:** Rainfall, air temperature, relative humidity, wind speed/direction, stream gauge level, among others. 
- **Geographic coverage:** Nationwide network spanning coastal, inland, and mountainous regions
- **Temporal resolution:** Typically 15-minute or hourly observations, with daily summaries
- **Historical depth:** Multi-year records (depth varies by station)

**Quality note:** Data comes directly from IMHPA's public data feeds. While IMHPA operates quality control procedures on their gauge network, you should be aware that raw observations may include errors, gaps, or artifacts. For critical hydrological applications, cross-reference with IMHPA's official bulletins or contact them directly.

## About This Tool

**`imhpa-api` is a Python client developed for scientific research purposes. It is an independently developed project and is not an official IMHPA product. It is not affiliated with or endorsed by IMHPA.**

- This tool calls IMHPA's public web endpoints—the same data endpoints accessible via [their public website](https://www.imhpa.gob.pa/es/estaciones-satelitales)
- It is maintained independently as a research tool
- Development and support are independent of the institution

**If you need:**
- Official data queries or historical datasets → Contact [IMHPA directly](https://www.imhpa.gob.pa/)
- Data licensing or institutional partnerships → Contact IMHPA
- Bug reports or feature requests for this *client* → Use this project's issue tracker

## Common Patterns

For detailed usage examples—filtering by date range, handling missing data, batch queries across multiple stations, and exporting to standard formats—see the `examples/` directory.

## API Reference

For detailed documentation of each method, including parameters, return types, and exceptions, consult the docstrings in your Python environment:

```python
import imhpa
client = imhpa.ImhpaClient()

help(client.list_sensors)
help(client.list_stations)
help(client.get_stations)
help(client.get_data)
```

Or view them directly in the source code under `imhpa/`.

## Legal & Attribution

By using this tool, you implicitly accept IMHPA's terms of service for their publicly available data.

When publishing research that uses data retrieved via this tool, please:
1. Acknowledge IMHPA as the data source
2. Clearly note that data was accessed through an independent client (`imhpa-api`)
3. If possible, cite this repository and mention the access date

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or pull request on GitHub.

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.