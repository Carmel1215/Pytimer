# Pytimer

Pytimer is a Python library for measuring the execution time of functions. 

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip 22.0 or higher
- Git must be installed and accessible in your system PATH

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytimer.

```bash
pip install git+https://github.com/Carmel1215/Pytimer.git
```

## Usage

```python
from pytimer import timer

@timer
def quick():
    pass

@timer(ns=True)
def slow():
    for _ in range(10**6):
        pass

quick()
slow()
```

## Roadmap

- [ ] Add comparison feature

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
