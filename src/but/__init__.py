from typer import Typer

app = Typer()


@app.command()
def but(file_name: str) -> None:
	# Imported here, not at module level: importing bpy boots Blender (~0.3s),
	# which `--help` and argument errors don't need.
	import bpy

	bpy.ops.wm.save_as_mainfile(filepath=f"{file_name}.blend")


def main():
	app()
