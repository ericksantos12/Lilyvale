@AGENTS.md

## Releases

`dev` is the working branch and `main` is the release branch; the repository only allows squash merges.

1. To release, add a new `## [x.y.z]` entry at the top of `CHANGELOG.md` on `dev`, commit, and push. The build workflow takes the version from that entry.
2. Do not open or merge a `dev` → `main` pull request yourself. `.github/workflows/build-release.yml` opens a draft `Release: x.y.z` pull request when the version has no tag yet; the maintainer reviews and merges it.
3. After a release lands on `main`, merge `main` back into `dev` so the squashed history stays in sync. Confirm with the maintainer before pushing that merge.

Feature pull requests into `dev` are fine when requested.
