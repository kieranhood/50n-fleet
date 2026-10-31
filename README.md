# 50n-fleet

Every server 50NORTH SYSTEMS looks after, described in one place, and the automation that sets them up. Each site's
settings live here as files; Ansible makes the servers match them. Nothing is changed on a server by hand, so this
repo (and its history) is always the true record of every installation.

The team handbook (set-up, workflows, secrets, documents, monitoring, rules) is at
https://claude.ai/artifact/JhMK219QfR7BpBaw3iLDH8.

```
inventory.yml                 every site, grouped (cafes, yachts)
group_vars/all.yml            defaults for every site
host_vars/<site>.yml          what's different about one site: which apps, versions, portal settings
sites/<site>/site.md          the human record: contacts, hardware, network, change log
sites/<site>/plans/           floor plans / deck plans and our network layouts drawn on them
sites/<site>/surveys/         Wi-Fi surveys, one folder each (predictive, validation, troubleshooting)
sites/<site>/commissioning/   one note per visit: what was done, tested and handed over
sites/<site>/portal/<id>/     the site's captive portal page, logo and fonts
sites/<site>/secrets.sops.yml the site's secrets, encrypted (never committed in plain text)
sites/_template/              copy this for a new site
playbooks/site.yml            the playbook: base OS, Docker, Cloudflare Tunnel, portal, PMS, monitoring, self-update
roles/                        one role per job (base, docker, cloudflared, portal, pms, monitoring, fleet_pull)
tests/render.yml              renders every site's generated files locally (also run by CI)
tools/drawio/                 the 50NORTH draw.io shape library (and the script that builds it)
.sops.yaml                    who can decrypt which site's secrets
```

## What runs on a server

| Role | What it does | Turned on by |
| --- | --- | --- |
| `base` | Packages, automatic security updates, time zone, the `fiftyn` admin user, SSH keys only | always |
| `docker` | Docker Engine and compose, with log rotation | when the portal or PMS is on |
| `cloudflared` | The site's Cloudflare Tunnel, for SSH through Cloudflare Access (no open ports) | `cloudflared_enabled` |
| `portal` | The guest Wi-Fi captive portal, a pinned image from `ghcr.io/kieranhood/50ncaptiveportal`, locked-down container | `portal_enabled` |
| `pms` | The vault.50N PMS boat server; installs once, updates only on request | `pms_enabled` |
| `monitoring` | A heartbeat to Uptime Kuma every minute (portal, PMS, disk); optional Netdata agent | always / `netdata_enabled` |
| `fleet_pull` | The server re-applies this repo itself whenever it's online (for boats) | `fleet_pull_enabled` |

## Your laptop: one-time set-up

```bash
pipx install "ansible-core>=2.16,<2.19"      # or pip in a venv
ansible-galaxy collection install -r requirements.yml
brew install sops age cloudflared            # or your OS's packages
age-keygen -o ~/.config/sops/age/keys.txt    # your key; put its public part in .sops.yaml
```

SSH goes through each site's tunnel (`ssh-<site>.50northsystems.com`) using `cloudflared access ssh`, so you sign in
through Cloudflare Access the first time.

## Adding a site

1. **Records.** Copy `sites/_template/` to `sites/<site>/` and fill in `site.md` during the survey. Mark unknowns
   **TODO: confirm**.
2. **Settings.** Add the site to `inventory.yml` and create `host_vars/<site>.yml` (copy `dartlings.yml`).
3. **Portal page.** Put the page, logo and fonts in `sites/<site>/portal/<client id>/public/`. Start from
   `sites/dartlings/portal/dartlings/public/`; the page contract is in the portal repo's README.
4. **Secrets.** Copy `sites/_template/secrets.example.yml` to `sites/<site>/secrets.sops.yml`, fill it in, then run
   `sops --encrypt --in-place sites/<site>/secrets.sops.yml`. Edit it later with `sops sites/<site>/secrets.sops.yml`.
5. **Remote access.** In Cloudflare Zero Trust, create a tunnel for the site. Route `ssh-<site>.50northsystems.com` to
   `ssh://localhost:22`, protect it with an Access application, and put the tunnel token in the site's secrets.
6. **First run, on the site's network** (before the tunnel exists). Use the server's LAN address and an account made
   during OS install:
   ```bash
   ansible-playbook playbooks/site.yml --limit <site> -e ansible_host=192.168.x.x -e ansible_user=<installer user> -K
   ```
7. **From then on**, through the tunnel: `ansible-playbook playbooks/site.yml --limit <site>`.
8. **Monitoring.** Create a push monitor for the site in Uptime Kuma and put its URL in `heartbeat_url`.
9. Commit, with a line in the site's change log.

## Plans, surveys and commissioning notes

Each site keeps its documents next to its settings, so the history of what was designed, installed and tested
stays with it:

| What | Where | Template |
| --- | --- | --- |
| Floor plans and network layouts (AP positions, switch, rack, cable runs) | `sites/<site>/plans/plans.md` and the images beside it | `sites/_template/plans/plans.md` |
| Wi-Fi surveys: a predictive design before install, validation after, troubleshooting later | `sites/<site>/surveys/<YYYY-MM-DD>-<type>/survey.md` with `heatmaps/` | `sites/_template/surveys/survey.md` |
| Commissioning: one note per visit (survey, equipment, configuration, tests, handover, snags) | `sites/<site>/commissioning/<YYYY-MM-DD>-<what>.md` with `files/` | `sites/_template/commissioning.md` |

How they fit together:
- **`site.md` is the current state.** Plans, surveys and commissioning notes are the dated history behind it.
- Surveys and commissioning notes name the **plan revision** they used (e.g. "Ground floor, rev B").
- A survey's open actions go on the commissioning note's snag list.

**Diagrams.**
- **Equipment on the floor or deck plan:** draw.io with the 50NORTH library (`tools/drawio/50north-network.xml`), starting from `sites/_template/plans/network-layout.drawio`. The steps are in the plans template.
- **Logical topology (links, VLANs):** Mermaid inside `site.md`, which GitHub draws.
- **Wi-Fi coverage design:** UniFi Design Center for cafés, Ekahau or Hamina for yachts. The exported PDF goes in `surveys/`.

**Large files stay out of Git.** Keep files here small: compressed heatmaps, annotated plans and photos, each under
5 MB (CI rejects bigger ones). Put raw survey projects (e.g. Ekahau `.esx`, ignored by Git), CAD drawings and
full-size originals in private storage, such as a Cloudflare R2 bucket with one folder per site. Link them from the
document with their SHA-256 (`shasum -a 256 <file>`), so anyone can check a file is the one that was recorded.

**Confidentiality.** Yacht GA drawings and layouts are often covered by an NDA. Check what the captain or management
company allows before storing plans, keep this repo private, and note any restrictions in `plans.md`.

## Day to day

```bash
ansible-playbook playbooks/site.yml --limit dartlings --check --diff   # what would change
ansible-playbook playbooks/site.yml --limit dartlings                  # apply
ansible-playbook playbooks/site.yml --limit cafes --tags portal        # just the portal, on every cafe
ansible-playbook tests/render.yml                                      # render every site's files locally
```

**Updating the portal.**
1. Release a new version in the portal repo (`git tag v2.2.0 && git push origin v2.2.0`; GitHub Actions publishes
   the image).
2. Set `portal_version: "2.2.0"` for **one** site and apply.
3. Check it, then roll it out to the rest.

**Updating the PMS on a boat.** Never mid-charter. Set `pms_ref` and run with `-e pms_update=true`. That uses the
PMS's own `scripts/update.sh`, which backs up the database first and refuses to update if the backup fails.

**Boats that are often offline.** Turn on `fleet_pull_enabled` for the boat. It then checks this repo every 30
minutes and applies its own changes whenever it's online. The first run prints the server's own age key: add it to
`.sops.yaml` for that site only and run `sops updatekeys sites/<site>/secrets.sops.yml`. That way the boat can read its
own secrets and nobody else's. It also needs a read-only deploy key for this repo (`fleet_deploy_key`).

## Rules

- **Everything goes through this repo.** If something was changed on a server by hand, bring it back here, or the
  next run undoes it.
- **No secrets in plain text.** Secrets live in `secrets.sops.yml` (encrypted) or the password manager. `site.md`
  says *where* a secret is, never what it is.
- **Change one site first**, check it, then the rest.
- **Never update a boat mid-charter.** Note charter periods in its `site.md`.
- **Every change gets a change-log line** in the site's `site.md`.

## Checks

GitHub Actions (`.github/workflows/check.yml`) runs on every push and pull request:
- the Ansible syntax check and `ansible-lint`;
- renders every site's files;
- checks the portal settings are valid JSON, the compose files are valid, and the heartbeat scripts are valid shell.
