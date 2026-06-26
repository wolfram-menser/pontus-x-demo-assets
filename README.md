# pontus-x-demo-assets

Public demo data assets for Pontus-X marketplace use cases.

Each asset lives in its own directory and is published as a Data NFT on
Pontus-X Testnet (or Devnet). The Pontus-X Provider references the asset
via its GitHub raw URL during publishing — the file is then client-side
encrypted and only released to wallets that have paid the Datatoken price.

This repo intentionally hosts **non-sensitive demo data only**. Real
business data never lives here.

## Use Cases

| Directory | Description | Network | Service-ID |
|---|---|---|---|
| `use-case-1-manufacturing-benchmark/` | Anonymized machining-operations benchmarks (cycle time, OEE, energy, scrap rate, throughput) across 3 industries | Pontus-X Testnet | PX-MB-003 |
| `energy-consumption-benchmark/` | Energy-consumption benchmarks (avg power, energy/part, idle share, annual energy) by industry & machine type | Pontus-X Testnet | PX-EC-004 |
| `predictive-maintenance-signals/` | Condition-monitoring signals (vibration, bearing temp, acoustics, oil particles, health index, RUL) for a machine/pump fleet | Pontus-X Testnet | PX-PM-005 |
| `carbon-footprint-heat-pump/` | Product Carbon Footprint reference values (kgCO₂e) for heat-pump components, lifecycle phase A1–A3 | Pontus-X Testnet | PX-CF-006 |
| `compute-oee-anomaly-algorithm/` | **Compute-to-Data algorithm** — condition/anomaly analysis that runs ON a dataset; raw data never leaves the compute env, buyer receives only the aggregated `result.json` | Pontus-X Testnet | PX-CD-007 |

> Services PX-EC-004 … PX-CD-007 are published by the **Proalpha GmbH** publisher
> wallet (`0x7f8d…74d3`); purchases flow through the real `proalpha` ERP adapter
> (HashBuch tenant 245).

## Raw URL pattern

```
https://raw.githubusercontent.com/wolfram-menser/pontus-x-demo-assets/main/<use-case-dir>/<filename>
```

## License

Demo data is provided as-is for ecosystem demonstration purposes
(CC-BY-4.0). Attribution: Proalpha GmbH.
