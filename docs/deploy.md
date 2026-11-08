# Deployment: Tic Tac Toe auf GitHub Pages

Diese Datei beschreibt, wie das Spiel gebaut und veröffentlicht wird – und was bei Problemen zu tun ist.

## Überblick

Das Spiel ist **Python** (pygame-ce). GitHub Pages kann kein Python ausführen, deshalb wird der Code mit
**pygbag** zu **WebAssembly** gebaut. Ergebnis ist eine ganz normale statische Seite.

```
web/main.py                     <- Spielcode (pygame-ce)
      |  pygbag --build
      v
web/build/web/                  <- index.html + WASM + App-Archiv (nicht im Git!)
      |  GitHub Action: JamesIves/github-pages-deploy-action
      v
Branch gh-pages                 <- das, was GitHub Pages ausliefert
      v
https://laraa2025.github.io/adTicTacToe/
```

**Live-URL:** https://laraa2025.github.io/adTicTacToe/
**Repo:** https://github.com/laraa2025/adTicTacToe

## Dateien

| Datei | Aufgabe |
|---|---|
| `web/main.py` | Spiel in pygame-ce (Portierung von `adtictactoe_local.py`) |
| `.github/workflows/pygbag.yml` | baut das Spiel und pusht es nach `gh-pages` |
| `.gitignore` | hält `web/build/`, `__pycache__/` und `*.pdf` aus dem Repo |
| `web/.gitignore` | Build-Ausgabe im Spielordner |
| `docs/deploy.md` | diese Datei |

## Lokal testen

```powershell
# Desktop-Fenster (schneller Test der Spiellogik)
python web/main.py

# nur bauen, ohne Server
python -m pygbag --build web

# Testserver im Browser: http://localhost:8000
python -m pygbag web
```

Beim ersten Aufruf im Browser werden ca. 15 MB Python-WASM geladen. Das dauert etwas, ist danach
aber im Browser-Cache.

## Einmalige Einrichtung (bereits erledigt)

1. Öffentliches Repo `adTicTacToe` angelegt (Pages im Free-Plan nur bei public).
2. **Settings -> Actions -> General -> Workflow permissions** = *Read and write permissions*.
   Ohne diese Einstellung darf die Action den Branch `gh-pages` nicht anlegen.
3. **Settings -> Pages** -> Source: *Deploy from a branch* -> Branch `gh-pages`, Ordner `/ (root)`.
4. Git-Identität auf die GitHub-noreply-Adresse gesetzt, weil „Block command line pushes that expose
   my email“ aktiv ist:
   ```powershell
   git config --global user.email "DEINNAME@users.noreply.github.com"
   ```
5. Anmeldung über den Git Credential Manager:
   ```powershell
   git config --global credential.helper manager
   ```

## Automatisches Deployment

Der Workflow `.github/workflows/pygbag.yml` startet bei **jedem Push auf `main`**:

```yaml
on:
  workflow_dispatch:
  push:
    branches: [main]
```

Ablauf im Job `pygbag_build`:

1. Repo auschecken, Python 3.12 einrichten
2. `pip install pygbag`
3. `python -m pygbag --build web` -> erzeugt `web/build/web/`
4. `.nojekyll` anlegen (sonst ignoriert GitHub Pages Dateien mit Unterstrich)
5. `web/build/web/` nach Branch `gh-pages` deployen (`clean: true` löscht alte Dateien)

Dauer: ca. 2–4 Minuten. Ergebnis prüfen: Repo -> **Actions** -> letzter Lauf mit grünem Haken.

## Neue Version veröffentlichen

```powershell
git status
git add web/main.py            # oder gezielt die geänderten Dateien
git commit -m "Beschreibung der Änderung"
git push
```

Mehr ist nicht nötig – der Push löst Build und Deploy aus. Die URL bleibt gleich.

## Manuell neu bauen (ohne Codeänderung)

Repo -> **Actions** -> links `pygbag_build` -> **Run workflow** -> *Run workflow*.
Möglich, weil `workflow_dispatch` im Workflow steht.

## Fehlersuche

| Symptom | Ursache / Lösung |
|---|---|
| Action rot, „Permission denied“ beim `gh-pages`-Push | Workflow permissions nicht auf *Read and write* |
| Seite zeigt 404 | Pages-Source nicht auf `gh-pages` gesetzt, oder 1–2 Min warten |
| Seite lädt, aber Spiel reagiert nicht | `Strg + F5` (harter Reload) – alter WASM-Cache |
| Seite zeigt alte Version | Browser-Cache; im Actions-Lauf prüfen, ob der Deploy durchlief |
| `push declined due to email privacy restrictions` | Commit mit privater E-Mail: noreply-Adresse setzen, dann `git commit --amend --reset-author --no-edit` |
| `Password authentication is not supported` | Credential Manager: `cmdkey /delete:git:https://github.com`, dann `git config --global credential.helper manager`, erneut pushen |
| Spiel stürzt im Browser ab | Browser-Konsole öffnen (`F12`); Ursache steht meist als Python-Traceback dort |
| `pygbag` findet das Spiel nicht | Datei muss `web/main.py` heißen und `asyncio.run(main())` enthalten |

## Hinweise zum Spielcode

pygbag verlangt:

- Einstiegsdatei heißt `main.py`
- Spielschleife in `async def main()`
- `await asyncio.sleep(0)` in jeder Iteration (sonst friert der Browser ein)
- `asyncio.run(main())` am Dateiende
- keine blockierenden Aufrufe (`input()`, `messagebox`, `pygame.event.wait`)

Die Szene wird über die globale Variable `szene` gesteuert:
`namen` -> `spiel` -> `ergebnis` -> `ende`.

**Die Hauptschleife darf nicht beendet werden, um „das Spiel zu beenden“** – im Browser bleibt sonst
ein eingefrorenes Canvas stehen und es reagiert nichts mehr. Stattdessen wird die Szene `SZENE_ENDE`
angezeigt (Button „Beenden“), von dort führt „Neu starten“ zurück zur Namenseingabe.
