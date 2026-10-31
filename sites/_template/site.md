# <Site name>

The human record of this site. Keep it current: every visit or change adds a line to the change log.
Anything not yet known is marked **TODO: confirm**. Secrets are never written here: name the password-manager item
or the key in `secrets.sops.yml` instead.

## Overview

| | |
| --- | --- |
| Client | |
| Kind | cafe / yacht / other |
| Address or home port | |
| Website | |
| Inventory name | `<site>` (in `inventory.yml`, `host_vars/<site>.yml`, `sites/<site>/`) |

## Contacts and access

| Role | Name | Phone / email | Notes |
| --- | --- | --- | --- |
| Main contact | | | |
| On-site / captain / ETO | | | |

- When we may work on it (opening hours, charter calendar, quiet times):
- How to get physical access:

## Hardware

| Item | Model | Serial | MAC | Location | Notes |
| --- | --- | --- | --- | --- | --- |
| Server | | | | | |
| UniFi console | | | | | |
| Switch (PoE port for the server) | | | | | port no. |

## Network

- **Internet**: provider, type (fibre / Starlink / 4G / marina Wi-Fi), fixed or changing IP, CGNAT?
- **UniFi**: site name, console ID (unifi.ui.com), Network version, UniFi OS version
- **Remote access**: Cloudflare tunnel name, `ssh-<site>.50northsystems.com`, Access policy

| VLAN | ID | Range | Purpose | Notes |
| --- | --- | --- | --- | --- |
| Management | | | server, console, switches | |
| Guest | | | guest Wi-Fi (Hotspot Portal) | may reach the server on TCP 80 only |

| Device | Address | How set |
| --- | --- | --- |
| Server | | DHCP reservation |
| UniFi console | | |

Firewall rules that matter (UniFi):
- Guest → server: TCP 80 only (the portal). Nothing else, in particular not the PMS (TCP 3000).
- Server → console: TCP 443 (UniFi API).

## Services

| Service | Setting | Where |
| --- | --- | --- |
| Captive portal | version, clients, External Portal Server IP | `host_vars/<site>.yml` |
| PMS | ref, installed on | `host_vars/<site>.yml` |
| Monitoring | Uptime Kuma monitor name, Netdata room | |
| Backups | PMS nightly + off-site target, UniFi cloud backups | |

## Secrets (where they are, never what they are)

| Secret | Where |
| --- | --- |
| UniFi API key | `secrets.sops.yml` › `unifi_api_keys` |
| Tunnel token | `secrets.sops.yml` › `cloudflared_tunnel_token` |
| Local admin logins (console, switches) | password manager › `<item>` |

## Change log

| Date | Who | What |
| --- | --- | --- |
| | | Site record created |

## Known issues and notes
