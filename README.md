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

## Raw URL pattern

```
https://raw.githubusercontent.com/wolfram-menser/pontus-x-demo-assets/main/<use-case-dir>/<filename>
```

## License

Demo data is provided as-is for ecosystem demonstration purposes
(CC-BY-4.0). Attribution: Proalpha GmbH.
