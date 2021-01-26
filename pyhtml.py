# creates html elements with attributes if any
class HTML():
    def __init__(self, tag, data, **attrs):
        if attrs:
            html = f'<{tag} '
            for attr in attrs:
                cleaned = attr.lower() + "=" + "\"" + attrs[attr] + '"' + " "
                html += cleaned

            html = f"{html[:-1]}>{data}</{tag}>"

            self.html = html

        else:
            self.html = f"<{tag}>{data}</{tag}>"

    def __str__(self) -> str:
        return self.html

    # prints out your html code
    def preview_html(self):
        print(self.html)

    # creates .html file without html5 template
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.html)

    # Saves your code as html5 template
    def save_as_template(self, filename, title="[ Change Title Here ]", additional_link="", css_filename="style.css"):
        template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {additional_link}
    <link rel="stylesheet" href="style.css" />
    <title>{title}</title>
</head>
<body>
    {self.html}
</body>
</html>"""

        with open(filename, 'w') as file:
            file.write(template)


# Only returns html code, same as html_bundler but returns html code instead of creating .html file
def html(*data, title="[ Change Title Here ]", css_link="", additional_link=""):
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {additional_link}
    <style>
    {css_link}
    </style>
    <title>{title}</title>
</head>
<body>
"""
    for tag in data:
        template += str(tag) + "\n"

    template += """</body>
</html>"""

    return template


# Bundles all HTML elements into one .html file
def html_bundler(*data, title="[ Change Title Here ]", css_filename="style.css", filename, additional_link=""):
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {additional_link}
    <link rel="stylesheet" href='{css_filename}' />
    <title>{title}</title>
</head>
<body>
"""
    for tag in data:
        template += str(tag) + "\n"

    template += """</body>
</html>"""

    with open(filename, 'w') as file:
        file.write(template)
