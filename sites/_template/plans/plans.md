# <Site name>: floor plans

Every plan used for this site: the clean originals, and our annotated network layouts drawn on them. Surveys and
commissioning notes name the plan and revision they used (e.g. "Ground floor, rev B"), so a heatmap or an AP
position can always be traced back to the exact drawing.

Copy this file to `sites/<site>/plans/plans.md`. Put small images and PDFs (under 5 MB each) in this folder. Large
originals (CAD files, full-size GA drawings) go in the private storage bucket and are linked from the table below.

**Confidentiality: TODO: confirm.** Yacht GA drawings are often covered by an NDA, so check what the captain or
management company allows before storing them anywhere. Note any restrictions here.

## Plans

| Area / deck | Kind | Revision | Date | Source | Scale | File | Restrictions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ground floor | original | A | | client / architect / shipyard | 1:100 | `ground-floor-revA.pdf` | |
| Ground floor | network layout | A | | 50NORTH | 1:100 | `ground-floor-network-revA.png` | |

*Kind*:
- **original**: the drawing as received.
- **network layout**: our annotations on it (AP positions, switch, rack, cable runs, server, PoE ports).
- **as-built**: the network layout updated to what was actually installed.

## Network layout key

Use the same symbols on every plan so they read the same way at every site:

| Symbol | Meaning |
| --- | --- |
| ● AP-01 | Wi-Fi access point, labelled as in UniFi |
| ■ SW-01 | Switch |
| ▲ GW | Gateway / UniFi console |
| ◆ SRV | Server (PMS / captive portal) |
| ─ | Data cable run (label with the cable ID) |

## Large originals (private storage)

| File | Link | SHA-256 |
| --- | --- | --- |
| | | |

## Change log

| Date | Who | What |
| --- | --- | --- |
| | | Plans received |
