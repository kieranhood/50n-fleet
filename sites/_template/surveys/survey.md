# <Site name>: <predictive | validation | troubleshooting> Wi-Fi survey, <YYYY-MM-DD>

Copy this folder to `sites/<site>/surveys/<YYYY-MM-DD>-<type>/`. Keep a few compressed heatmap images (under 5 MB
each) in `heatmaps/` next to this file. The raw survey project and full reports go in private storage, linked below.

- **Predictive**: a design made from the plans before install.
- **Validation**: measured on site after install, to prove the design was met.
- **Troubleshooting**: a survey to investigate a complaint or change.

## Survey details

| | |
| --- | --- |
| Date | |
| Surveyor | |
| Type | predictive / passive / active / validation |
| Tool and version | e.g. Ekahau AI Pro 11 + Sidekick 2, Hamina, NetSpot |
| Measuring device | e.g. Sidekick 2, iPhone 15 (for client-device checks) |
| Plans used | name and revision from `../../plans/plans.md` (e.g. "Ground floor, rev B") |
| Conditions | e.g. café open with ~40 guests / yacht at anchor, all doors closed |

## Requirements (agreed with the client)

The defaults below are common starting points. **TODO: confirm** each one per site.

| Requirement | Target | Applies to |
| --- | --- | --- |
| Primary signal (RSSI) | ≥ −67 dBm | areas used for calls, video, crew work |
| Primary signal (RSSI) | ≥ −70 dBm | guest browsing areas |
| Signal-to-noise (SNR) | ≥ 25 dB | everywhere covered |
| Secondary signal (for roaming) | within 5–10 dB of primary | areas where people walk while connected |
| Co-channel overlap | ≤ 2 APs heard above −85 dBm on the same channel | everywhere covered |
| Throughput (active test) | ≥ __ Mbps down / __ Mbps up | guest network |
| Bands | 2.4 / 5 / 6 GHz | |

## Access point plan

| AP | Model | Location (plan ref) | Mount | 2.4 GHz ch / power | 5 GHz ch / width / power | 6 GHz ch / width / power | Firmware |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AP-01 | | | ceiling / wall | | | | |

## Results by area

| Area / deck | Min RSSI | Min SNR | Secondary within | Co-channel | Throughput | Pass? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | dBm | dB | dB | APs | Mbps | ✅ / ❌ | |

Heatmaps:

| Area / deck | Signal | SNR | Channel overlap |
| --- | --- | --- | --- |
| | `heatmaps/<area>-rssi.png` | `heatmaps/<area>-snr.png` | `heatmaps/<area>-overlap.png` |

## Interference and environment

Other networks seen (count and strongest), non-Wi-Fi interference, and materials affecting signal (steel bulkheads,
glass, water tanks, mirrors).

## Issues and actions

| # | Issue | Action | Owner | Due | Done |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |

Open actions also go on the commissioning snag list.

## Conclusion

Does the site meet the requirements? What changed since the last survey?

## Raw files (private storage)

| File | Link | SHA-256 |
| --- | --- | --- |
| Survey project (e.g. `.esx`) | | |
| Full report (PDF) | | |
