import os
import markdown
import jinja2


def markdown_to_html(file_name: str) -> str:
    with open(file_name, "r") as file_pointer:
        return markdown.markdown(file_pointer.read())


def get_template(file_name: str) -> jinja2.Template:
    return jinja2.Template(open(file_name).read())


def a_link(name: str, link: str):
    return f'<a id="menu-item" href="{link}">{name}</a>'


def generate_pages(
    markdown_folder: str, base_template: str, css_file: str, output_folder: str
):
    os.makedirs(output_folder, exist_ok=True)
    template = get_template(base_template)
    file_names = [
        markdown_file.split(".")[0] for markdown_file in os.listdir(markdown_folder)
    ]
    menu_elements = [
        f'<p>{a_link(file_name, "./" + file_name + ".html")}</p>'
        for file_name in file_names
    ]
    menu = f'<div id="menu">{"".join(menu_elements)}</div>'

    for file_name in file_names:
        markdown_file_path = os.path.join(markdown_folder, file_name + ".md")
        html_file_path = os.path.join(output_folder, file_name + ".html")

        with open(html_file_path, "w+") as html_file_pointer:
            html_file_pointer.write(
                template.render(
                    page_title=file_name,
                    menu=menu,
                    body=markdown_to_html(markdown_file_path),
                )
                + f"\n<style>\n{open(css_file).read()}\n</style>\n"
            )
