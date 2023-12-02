# Advent of code 2023

[![Tests](https://github.com/joonaspessi/aoc2023/actions/workflows/test.yml/badge.svg)](https://github.com/joonaspessi/aoc2023/actions/workflows/test.yml)

My solutions for [Advent of Code 2023](https://adventofcode.com/2023).

## Usage

### Prerequisites

python3.11

### Create venv and install dependencies

```bash
make venv
source venv/bin/activate
```

### Run tests

```bash
make test
```

### Upgrade dependencies

```bash
make compile-requirements
```

### Download input

Get your session cookie from [Advent of Code](https://adventofcode.com/), insert the cookie to `.env` file and run:

```bash
make download-input
```
