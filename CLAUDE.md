# 50n-fleet

The record and automation for every server 50NORTH SYSTEMS looks after (cafés, yachts). See README.md.

## Commands

```bash
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbooks/site.yml --syntax-check
ansible-lint playbooks/site.yml tests/render.yml
ansible-playbook tests/render.yml -e render_dir=/tmp/render     # every site's generated files, locally
ansible-playbook playbooks/site.yml --limit <site> --check --diff
```

## Rules

- **Never put a secret in plain text** in any file, commit, log or reply. Secrets go in `sites/<site>/secrets.sops.yml`
  (SOPS-encrypted) or the password manager; `site.md` names where a secret is, never its value. Tasks handling
  secrets use `no_log: true`.
- **Don't guess site details.** Anything not confirmed is marked **TODO: confirm** in `site.md` and `host_vars`.
- **Every change to a site adds a line to its change log** (`sites/<site>/site.md`).
- **Roles must be safe to re-run** and change only what differs.
- **Live boats:** never change a PMS database or its backups, and never update the PMS except through its own
  `scripts/update.sh` with `pms_update=true` and the owner's go-ahead. Never mid-charter.
- **Before pushing:** run the syntax check, `ansible-lint`, and `tests/render.yml`.
- Explain decisions in plain English, for a reader who isn't a programmer.
