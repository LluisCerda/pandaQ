# pandaQ

Implementation of a small SQL interpreter called PandaQ.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install streamlit.

```bash
pip install streamlit
```

## Usage

Run:
```bash
streamlit run pandaQ.py
```
You can now view PandaQ in your browser.

## Extra-Features

- Added the possibility to use saved tables with inner join.
- Custom Error Listener for ANTLR Parser.

## Known-Bugs

- ID1 as ID2 will create a new column ID2 with ID1 in each file

- Error with non decimal values, .0 needed: 2 -> No, 2.0 -> Yes

## Extra

- Plot works by using only the numeric columns.

- If no order is specified, ascending order is used by default.

## License

[Creative Commons](https://creativecommons.org/licenses/by-nc-sa/4.0/)
