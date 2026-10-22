# Repository Guidelines

## Project Structure & Module Organization

Lilyvale is a Minecraft 1.20.1 Forge modpack. Pakku controls the official mod list; consult `.pakku/docs/` for its commands. `pakku.json` declares the projects, and `pakku-lock.json` lists the resolved files. Keep both in sync when changing mods. Pack configuration lives in `config/` and `defaultconfigs/`. Put KubeJS startup registrations in `kubejs/startup_scripts/`, recipes and server events in `kubejs/server_scripts/`, and client behavior in `kubejs/client_scripts/`. KubeJS resources belong in `kubejs/assets/` and data pack files in `kubejs/data/`. Repository artwork is in `.github/assets/`. Runtime directories such as `saves/`, `logs/`, `mods/`, and `build/` are ignored; do not commit local game data.

## Build, Test, and Development Commands

- `cd kubejs && npm ci`: install the pinned ESLint dependencies (Node.js 20 is used in CI).
- `cd kubejs && npx eslint .`: check KubeJS JavaScript and the custom lint rules in `kubejs/dx/eslint-plugin/`.
- Launch the pack in Prism Launcher to check game behavior. Use `/reload` after server script changes and `F3+T` after client resource changes; restart the game for startup registrations.

The GitHub build workflow packages releases from `main` and `dev`. There is no repository-local build script or automated gameplay test command.

## Coding Style & Naming Conventions

Use four spaces in JavaScript, Unix line endings, a final newline, and no trailing whitespace. Follow the existing KubeJS event and recipe patterns. ESLint enforces these rules and the PanPack recipe-spacing and multiblock-declaration rules. Keep file names descriptive and place each script on the side where it runs.

## Testing Guidelines

Run ESLint before submitting JavaScript changes. For behavior changes, launch the pack and verify the affected recipe, event, or resource in game; consult `logs/kubejs/` for script errors. There is no test framework or coverage threshold in this repository.

## Commit & Pull Request Guidelines

Recent commits commonly use short imperative subjects with prefixes such as `feat:` and `docs:`. Describe the change and its user-visible effect in a pull request, note the in-game checks performed, and link relevant issues. Include screenshots for visible UI, texture, or gameplay changes. Review the diff for generated files and personal configuration before committing.
