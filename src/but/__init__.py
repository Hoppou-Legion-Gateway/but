import bpy
from typer import Typer

app = Typer()


@app.command()
def but(file_name: str) -> None:
	bpy.ops.wm.save_as_mainfile(filepath=f"{file_name}.blend")


def main():
	app()
