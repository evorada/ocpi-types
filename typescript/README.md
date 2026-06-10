# `ocpi-types-typescript`

Auto-generated TypeScript type definitions for the [OCPI](https://evroaming.org/) (Open Charge Point Interface) protocol.

📖 **Documentation:** https://evorada.github.io/ocpi-types/typescript/

## Installation

```sh
npm install --save-dev ocpi-types-typescript
```

## Usage

Each OCPI version is available as its own module. Import the types directly from
the version you need:

```ts
import type { Session } from 'ocpi-types-typescript/v2.3.0';

const session: Session = JSON.parse(raw);
console.log(session.id, session.status);
```

Or via the namespace export, which exposes every version at once:

```ts
import { V230 } from 'ocpi-types-typescript';

const session: V230.Session = JSON.parse(raw);
```

## Available versions

| Import | Namespace | OCPI version |
| --- | --- | --- |
| `ocpi-types-typescript/v2.1.1` | `V211` | 2.1.1 |
| `ocpi-types-typescript/v2.2.1` | `V221` | 2.2.1 |
| `ocpi-types-typescript/v2.3.0` | `V230` | 2.3.0 |
| `ocpi-types-typescript/v2.3.0-payments` | `V230Payments` | 2.3.0 + Payments |
| `ocpi-types-typescript/v2.3.0-bookings` | `V230Bookings` | 2.3.0 + Bookings |
