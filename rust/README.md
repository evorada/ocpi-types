# `ocpi-types` (Rust)

Auto-generated Rust type definitions for the [OCPI](https://evroaming.org/) (Open Charge Point Interface) protocol. All types derive `serde::{Serialize, Deserialize}`.

📖 **Documentation:** https://evorada.github.io/ocpi-types/rust/ — also on [docs.rs](https://docs.rs/ocpi-types).

## Installation

```sh
cargo add ocpi-types
cargo add serde_json   # to (de)serialize
```

## Usage

Each OCPI version is exposed as a module of the `ocpi_types` crate.

```rust
use ocpi_types::v2_3_0::Session;

fn main() -> Result<(), serde_json::Error> {
    let raw = r#"{
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
    }"#;

    let session: Session = serde_json::from_str(raw)?;
    println!("{} {:?}", session.id, session.status);
    Ok(())
}
```

## Available versions

| Module | OCPI version |
| --- | --- |
| `ocpi_types::v2_1_1` | 2.1.1 |
| `ocpi_types::v2_2_1` | 2.2.1 |
| `ocpi_types::v2_3_0` | 2.3.0 |
| `ocpi_types::v2_3_0_payments` | 2.3.0 + Payments |
| `ocpi_types::v2_3_0_bookings` | 2.3.0 + Bookings |
