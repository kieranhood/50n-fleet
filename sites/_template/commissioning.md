# <Site name>: commissioning, <YYYY-MM-DD>, <install | upgrade | visit>

Copy this file to `sites/<site>/commissioning/<YYYY-MM-DD>-<what>.md`, one per visit. It records what was done,
what was tested and what was handed over. Copy the resulting *current* state (hardware, addresses, VLANs) into
`site.md`, and add a change-log line there linking to this note.

**Never write a password or key here.** Say where it is stored instead (`secrets.sops.yml` or the password manager).

## Scope and attendees

| | |
| --- | --- |
| Date and times on site | |
| 50NORTH engineers | |
| Client attendees | |
| Agreed scope | |
| Out of scope | |

## Pre-install survey

- **Internet link**: type, provider, measured speed, fixed or changing IP, CGNAT.
- **Existing equipment**: kept / replaced / removed.
- **Cabling**: existing runs, new runs needed, cable IDs.
- **Rack, power and cooling**: location, UPS, free space, temperature.
- **PoE budget**: switch model, PoE+ ports needed vs available, total watts.
- **Floor plans**: received? Which revision (see `plans/plans.md`)?
- **Wi-Fi survey**: link to the predictive survey in `surveys/`.

## Installed equipment

| Item | Model | Serial | MAC | Location (plan ref) | Switch port | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Configuration applied

- **UniFi**:
  - site
  - networks and VLANs
  - Wi-Fi networks
  - Hotspot portal (External Portal Server address, HTTPS redirection off)
  - firewall rules
  - Dynamic DNS (if used)
- **Server**: the 50n-fleet commit or Ansible run applied (`git log -1 --format=%h`), apps and versions.
- **Remote access**: tunnel name, Access policy.
- **Monitoring**: Uptime Kuma monitor, Netdata (if used), alert contacts.
- **Backups**: UniFi cloud backup on, PMS backups and off-site target (if used).

## Tests

| # | Test | Expected | Result | Pass? |
| --- | --- | --- | --- | --- |
| 1 | Internet speed test on each network | ≥ __ / __ Mbps | | |
| 2 | Wi-Fi validation survey | meets the requirements in `surveys/` | link | |
| 3 | Guest portal sign-in on iPhone | splash page appears, connects | | |
| 4 | Guest portal sign-in on Android | splash page appears, connects | | |
| 5 | Guest isolation: guest can't reach the management network or other guests | blocked | | |
| 6 | Guest can't reach the server except the portal (e.g. PMS port 3000 blocked) | blocked | | |
| 7 | Remote SSH through Cloudflare from off site | works | | |
| 8 | Monitoring heartbeat green in Uptime Kuma | green | | |
| 9 | Power-cycle the server's PoE port from UniFi; everything comes back on its own | back within __ min | | |
| 10 | Pull the internet link: alerts arrive, everything recovers when it returns | alert, recovers | | |

## Handover

- Shown to:
- Documents provided (user guide, Wi-Fi details card, support contacts):
- Client sign-off (name, date):

## Snags (outstanding)

| # | Snag | Owner | Due | Done |
| --- | --- | --- | --- | --- |
| 1 | | | | |

## Photos and exports

Small, compressed files (under 5 MB each) in `files/<YYYY-MM-DD>/`; larger ones in private storage:

| File | What it shows | Link (if in storage) |
| --- | --- | --- |
| | rack before / after, AP mounts, cable labels | |
