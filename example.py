from pyhtml import *

# Example for wraping elements with other elements

group = Render(
    HTML('label', "Todo"),
    HTML("input", Type="text", placeholder="Todo Item..."),
    HTML("input", type="submit", value="Add"),
).as_element()

# Wraping form tags around variable group
form = Render(
    HTML('form', group, method='post'),
    title="Todo"
)

print(form.html()) # returns html code as string
