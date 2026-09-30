from pathlib import Path

import bpy
import pytest
from typer.testing import CliRunner

from but import app


def test_saves_blend_file(
	tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
	monkeypatch.chdir(tmp_path)

	result = CliRunner().invoke(app, ["Spirit"])

	assert result.exit_code == 0, result.output
	saved = tmp_path / "Spirit.blend"
	bpy.ops.wm.read_factory_settings(use_empty=True)
	assert bpy.ops.wm.open_mainfile(filepath=str(saved)) == {"FINISHED"}
	assert Path(bpy.data.filepath) == saved
