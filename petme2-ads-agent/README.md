# PETME2 Ads Team

An AI team that manages Amazon PPC for PETME2. The rules are in `CLAUDE.md`.
It starts in **audit** mode: read only, no changes to your Amazon account.

## Start here (on your own computer)

1. **Get the project.** Download this repo (GitHub → green **Code** button → **Download ZIP**, then unzip) or clone it.
2. **Install Python packages.** Open a terminal in the folder and run:
   `pip install -r requirements.txt`
3. **Create your keys file.**
   - Find the file **`.env.example`** in the project folder.
   - Make a copy and name the copy **`.env`** (just `.env`, nothing before the dot).
   - Open `.env` in a text editor (Notepad / TextEdit) and type your 3 keys after the `=`:
     ```
     LWA_CLIENT_ID=amzn1.application-oa2-client....
     LWA_CLIENT_SECRET=amzn1.oa2-cs.v1....
     SP_API_REFRESH_TOKEN=Atzr|....
     ```
   - Save. Never upload `.env` anywhere and never paste the keys in the chat. (`.env` is blocked from GitHub by `.gitignore`.)
   - Tip: files that start with a dot are hidden. Mac Finder: press **Cmd + Shift + .** to see them. Windows: View → **Hidden items**.
4. **Test:** `python -m sp_api.test_connection`, then `python -m sp_api.snapshot` for your products table.
5. **Open the folder in Claude Code** (with Claude in Chrome connected) and say "keys are ready".
6. Every day: run `/daily-run`.

## Where to find your SP-API keys
Seller Central → **Apps and Services → Develop Apps** → your app:
- **LWA credentials → View:** Client ID and Client Secret.
- **Authorize:** gives the Refresh Token (starts with `Atzr|`).

## Folders
`data/` daily snapshots · `inbox/` downloaded ads files · `outbox/` bulk upload files ·
`reports/` daily and weekly reports · `experiments/` tests · `sp_api/` and `ads_source/` code ·
`.claude/agents/` the 6 team members · `.claude/commands/daily-run.md` the daily routine.
