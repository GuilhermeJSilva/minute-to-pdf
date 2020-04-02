# Minute to PDF

Minute to PDF provides an easier interface with `pandoc` to convert markdown files to pdf.

```
./minute-to-pdf <input-file>
```

## Requirements

* [Pandoc](https://pandoc.org)
* [GraphViz for Python](https://pypi.org/project/graphviz/)


## Command options

* `--url <url>` - Makes a `GET` request to the url in order to retrieve the input file
* `--out <out>` - Specifies an output file

## Supported Commands

* `!author` - Adds an author
