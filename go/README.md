# `ocpi-types` (Go)

Auto-generated Go type definitions for the [OCPI](https://evroaming.org/) (Open Charge Point Interface) protocol.

📖 **Documentation:** https://evorada.github.io/ocpi-types/go/ — also browsable on [pkg.go.dev](https://pkg.go.dev/github.com/evorada/ocpi-types).

## Installation

```sh
go get github.com/evorada/ocpi-types@latest
```

## Usage

Each OCPI version is its own package. The types are plain structs with
`encoding/json` tags, so you can unmarshal straight into them.

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/evorada/ocpi-types/go/v230"
)

func main() {
	raw := []byte(`{
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
	}`)

	var session v230.Session
	if err := json.Unmarshal(raw, &session); err != nil {
		panic(err)
	}
	fmt.Println(session.ID, session.Status)
}
```

## Available versions

| Import path | OCPI version |
| --- | --- |
| `github.com/evorada/ocpi-types/go/v211` | 2.1.1 |
| `github.com/evorada/ocpi-types/go/v221` | 2.2.1 |
| `github.com/evorada/ocpi-types/go/v230` | 2.3.0 |
| `github.com/evorada/ocpi-types/go/v230payments` | 2.3.0 + Payments |
| `github.com/evorada/ocpi-types/go/v230bookings` | 2.3.0 + Bookings |
