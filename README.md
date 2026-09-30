<div align="center">

# BUT

A Blender utility built to accelerate workflows.

<br>

[![Built for Blender](https://badges.hoppou.dev/badge?title=Built%20for&label=Blender&color=E87D0D&icon=blender)](https://www.blender.org/)
[![Built with Python](https://badges.hoppou.dev/badge?title=Built%20with&label=Python&color=3776AB&icon=python)](https://www.python.org/)
[![Packaged with UV](https://badges.hoppou.dev/badge?title=Packaged%20with&label=UV&color=DE5FE9&icon=uv)](https://docs.astral.sh/uv/)
[![CI Passing](https://badges.hoppou.dev/ci/Hoppou-Legion-Gateway/but/tests.yml)](https://github.com/Hoppou-Legion-Gateway/but/actions/workflows/tests.yml)

</div>

<br>

## Usage

```sh
# Show help for command
uv run but --help

# Test
uv run pytest

# Build
uv build

# Publish
uv publish
```

## Releasing

Bump the version and push to `main`. The release workflow publishes
`v<version>` when that tag doesn't exist yet; other pushes skip releasing.

```sh
uv version --bump patch   # or minor / major
git commit -am "chore: release v$(uv version --short)"
git push
```

## License

This project is licensed under the MIT license. Refer to [LICENSE.md](LICENSE.md)
