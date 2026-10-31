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

## Network layouts in draw.io

1. In draw.io (app.diagrams.net or the desktop app): **File › Open Library from › Device** →
   `tools/drawio/50north-network.xml`. The 50NORTH shapes appear in the left panel.
2. Copy `network-layout.drawio` (beside this file) into the site's `plans/` folder and open it. Its **Plan** layer is
   locked: unlock it, import the floor or deck plan (File › Import from), set it in place, lock it again. Draw on the
   **Network** layer above it, which already holds the key.
3. Label every item as in UniFi (`AP-01`, `SW-01`), and every cable run with its cable ID (`C-01`).
4. Save the `.drawio` file here, export a PNG beside it (File › Export as › PNG), and list both in the table above
   with the plan's revision.

Use the same symbols on every plan so they read the same way at every site:

| Symbol | Meaning |
| --- | --- |
| ● cyan, labelled AP-01 | Wi-Fi access point (indoor), labelled as in UniFi |
| ○ cyan outline, AP-02 | Wi-Fi access point (outdoor) |
| ■ navy, SW-01 | Switch |
| ▲ amber, GW | Gateway / UniFi console |
| ◆ green, SRV | Server (PMS / captive portal) |
| dashed box | Rack / cabinet |
| cloud, ISP | Internet link (provider, Starlink, 4G) |
| ─ navy line, C-01 | Data cable run, labelled with the cable ID |

To change a shape for every site, edit `tools/drawio/make_library.py` and run it; it rebuilds the library and this
template.

## Large originals (private storage)

| File | Link | SHA-256 |
| --- | --- | --- |
| | | |

## Change log

| Date | Who | What |
| --- | --- | --- |
| | | Plans received |
