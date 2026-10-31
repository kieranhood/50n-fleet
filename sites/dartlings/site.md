# Dartlings

The human record of this site. Keep it current: every visit or change adds a line to the change log.
Anything not yet known is marked **TODO: confirm**. Secrets are never written here.

## Overview

| | |
| --- | --- |
| Client | Dartlings Indoor Play Café |
| Kind | cafe (Montessori-inspired indoor play café, ages 0–7) |
| Address | The Refectory, Higher Close, Dartington Hall Estate, Totnes, Devon TQ9 6EL |
| Website | www.dartlingsplay.com |
| Inventory name | `dartlings` |

## Contacts and access

| Role | Name | Phone / email | Notes |
| --- | --- | --- | --- |
| Main contact | **TODO: confirm** | | |
| On site | **TODO: confirm** | | |

- When we may work on it: outside opening hours (**TODO: confirm** hours).
- Physical access: **TODO: confirm**.

## Hardware

| Item | Model | Serial | MAC | Location | Notes |
| --- | --- | --- | --- | --- | --- |
| Server | **TODO: confirm** (shortlist: Minisforum S100, or Raspberry Pi 5 + GeeekPi P33 PoE+ NVMe kit) | | | | PoE+ (802.3at) from the UniFi switch |
| UniFi console | **TODO: confirm** | | | | |
| Switch (server's PoE port) | **TODO: confirm** | | | | port no. |

## Network

- **Internet**: **TODO: confirm** provider and whether the IP is fixed. (The portal runs on site, so a changing IP
  doesn't matter to it.)
- **UniFi**: site `default` (**TODO: confirm**), console address `192.168.1.1` (**TODO: confirm**).
- **Remote access**: Cloudflare tunnel → `ssh-dartlings.50northsystems.com` (**TODO: set up**).

| VLAN | ID | Range | Purpose | Notes |
| --- | --- | --- | --- | --- |
| Management | **TODO** | **TODO** | server, console, switches | |
| Guest | **TODO** | `10.0.50.0/24` (**TODO: confirm**) | "Dartlings Guest" Wi-Fi with Hotspot Portal | may reach the server on TCP 80 only |

| Device | Address | How set |
| --- | --- | --- |
| Server | **TODO** | DHCP reservation |
| UniFi console | `192.168.1.1` (**TODO: confirm**) | |

Firewall rules that matter (UniFi):
- Guest → server: TCP 80 only (the portal).
- Server → console: TCP 443 (UniFi API).

UniFi Hotspot settings: Landing Page › External Portal Server = the server's address; HTTPS redirection off.

## Services

| Service | Setting | Where |
| --- | --- | --- |
| Captive portal | 2.1.0, client `dartlings`, on-site `integration` mode | `host_vars/dartlings.yml` |
| PMS | not used | |
| Monitoring | Uptime Kuma push monitor "Dartlings" (**TODO: create**) | |

The portal's page, logo and fonts are in `sites/dartlings/portal/dartlings/public/`. The terms of use in that page are
a template: **TODO: Dartlings to review before going live.**

## Secrets (where they are, never what they are)

| Secret | Where |
| --- | --- |
| UniFi Network API key | `secrets.sops.yml` › `unifi_api_keys.dartlings` (**TODO: create**) |
| Tunnel token | `secrets.sops.yml` › `cloudflared_tunnel_token` (**TODO: create**) |
| Heartbeat URL | `secrets.sops.yml` › `heartbeat_url` (**TODO: create**) |
| GitHub image token | `secrets.sops.yml` › `ghcr_token` (**TODO: create**) |

## Change log

| Date | Who | What |
| --- | --- | --- |
| 2026-10-31 | 50NORTH | Site record created; captive portal built (kieranhood/50NCaptivePortal) |

## Known issues and notes

- Not yet installed. Hardware and network details above are placeholders until the site survey.
