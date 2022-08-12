# naek ssg

A simple static site generator I've made for myself. It generates the site from a set of markdown files. Pages will be named as the markdown files are named.

The config file can be passed to the program with the `--config/-c` command line argument.

In the json config, it takes:
- css_file: the path to the css file
- base_template: the jinja2 template for the page. it takes a page_title, menu, and body variable.
- markdown_folder: the path to the folder containing the markdown pages
- output_folder: the folder where the generated HTML will be outputted.

Basic Usage

`python3 -m ssg --config config.json`