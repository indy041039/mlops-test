import typer

from mlspace.math import add_one, minus_one, double_it, half_it
from mlspace.string import main_func

app = typer.Typer()

@app.command()
def say_something(message: str = 'Hello'):
    print(message)
    return message

@app.command()
def calculate_something(number: int = 1):
    number = add_one(number)
    number = double_it(number)
    print(number)
    return number

@app.command()
def required_args(message: str, number: int):
    print(message)
    print(number)
    return message
