import typer

from mlspace.my_module import main_func
from mlspace.my_module2 import add_one, minus_one, double_it, half_it

app = typer.Typer()

@app.command()
def say_something(message: str):
    return message

@app.command()
def calculate_something(number: int):
    number = add_one(number)
    number = double_it(number)
    return number