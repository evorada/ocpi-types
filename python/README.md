# `ocpi-types` (Python)

Auto-generated Python type definitions for the [OCPI](https://evroaming.org/) (Open Charge Point Interface) protocol, using `dataclasses` and type hints.

📖 **Documentation:** https://evorada.github.io/ocpi-types/python/

## Installation

```sh
pip install ocpi-types
```

## Usage

Each OCPI version is its own module inside the `ocpi_types` package. Every class
provides `from_dict` / `to_dict` helpers.

```python
import json
from ocpi_types import v2_3_0

raw = """
{
  "country_code": "NL",
  "party_id": "TNM",
  "id": "101",
  "start_date_time": "2024-01-01T12:00:00Z",
  "kwh": 0,
  "cdr_token": {"country_code": "NL", "party_id": "TNM", "uid": "ABC", "type": "RFID", "contract_id": "NL-TNM-C12345678-X"},
  "auth_method": "WHITELIST",
  "location_id": "LOC1",
  "evse_uid": "3256",
  "connector_id": "1",
  "currency": "EUR",
  "status": "ACTIVE",
  "last_updated": "2024-01-01T12:00:00Z"
}
"""

session = v2_3_0.Session.from_dict(json.loads(raw))
print(session.id, session.status)

# serialize back to a JSON-ready dict
data = session.to_dict()
```

## Available versions

| Module | OCPI version |
| --- | --- |
| `ocpi_types.v2_1_1` | 2.1.1 |
| `ocpi_types.v2_2_1` | 2.2.1 |
| `ocpi_types.v2_3_0` | 2.3.0 |
| `ocpi_types.v2_3_0_payments` | 2.3.0 + Payments |
| `ocpi_types.v2_3_0_bookings` | 2.3.0 + Bookings |
