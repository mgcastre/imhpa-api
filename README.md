# IMHPA API

A lightweight, independnetly developed, Python client for accessing and downloading data from the Meteorological and Hydrological Institute of Panama ([IMHPA](https://www.imhpa.gob.pa/)).

## Motivation

Hydrological and water resource research requires quick, automated access to real-time hydrometeorological data for modeling and forecasting. This tool enables programmatic data workflows essential for research and proof-of-concept studies.

## Data Source

This tool accesses real-time data from [IMHPA's public gauge network](https://www.imhpa.gob.pa/es/estaciones-satelitales), which operates hundreds of automated hydrologicla and meteorological stations across Panama.

**What you get:**
- **Sensors:** Rainfall, air temperature, relative humidity, wind speed/direction, stream gauge and reservoir level, among others. 
- **Temporal resolution:** Measurements are reported typically in 15-minute intervals.
- **Historical depth:** Up to one month of historical records, depending on station and sensor.

**Quality note:** Data comes directly from IMHPA's public data feeds. While IMHPA operates quality control procedures on their gauge network, you should be aware that raw observations may include errors, gaps, or artifacts. For critical hydrological applications, cross-reference with IMHPA's official bulletins or contact them [directly](https://www.imhpa.gob.pa/es/contactenos).

## About This Tool

**`imhpa-api` is a Python client developed for scientific research purposes. It is an independently developed project and is not an official IMHPA product. It is not affiliated with or endorsed by IMHPA.**

This tool calls IMHPA's public data endpoints with no authentication required. It fetches data from the endpoints that power their [interactive website](https://www.imhpa.gob.pa/es/estaciones-satelitales). The same data is already publicly accessible there; this client simply automates programmatic access to it.

**If you need:** Official data queries, historical datasets or data licensing -> Contact IMHPA [directly](https://www.imhpa.gob.pa/es/contactenos).

### Installation Guide

**Latest development version:**
```bash
pip install git+https://github.com/mgcastre/imhpa-api.git
```

**Specific release (e.g., alpha version):**
```bash
pip install git+https://github.com/mgcastre/imhpa-api.git@v0.1.0a1
```

### Common Patterns

For detailed usage examples see the `notebooks/` directory (comming soon).

### API Reference

For detailed documentation of each method, including parameters, return types, and exceptions, consult the docstrings in your Python environment:

```python
import imhpa
client = imhpa.ImhpaClient()

help(client.list_sensors)
help(client.list_stations)
help(client.get_stations)
help(client.get_data)
```

Or view them directly in the source code under `src/imhpa/`.

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or pull request on GitHub.

## Legal & Attribution

By using this tool, you implicitly accept IMHPA's terms of service for their publicly available data.

When publishing research that uses data retrieved via this tool, please:
1. Acknowledge IMHPA as the data source
2. Clearly note that data was accessed through an independent client (`imhpa-api`)
3. If possible, cite this repository and mention the access date

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).