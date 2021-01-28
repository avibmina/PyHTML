# PyHTML (Python HTML)

### PyHTML is used create html using only python.

---

#### Usage:

- clone this repository
- import and start using

```python
from pyhtml import HTML
```

### Try examples for yourself, for better understanding

---

## Examples

#### Example 1: Creating Basic HTML Elements

```python
from pyhtml import HTML

# Creating h1 with value "Hello World"
h1 = HTML("h1", "Hello World")

# we can preview the code with .preview_html()
h1.preview_html() # outputs <h1>Hello World</h1>
# OR
print(h1) # outputs <h1>Hello World</h1>
```

Outputs:

```html
<h1>Hello World</h1>
```

---

#### Example 2 : Attributes

```python
from pyhtml import HTML

# using id attribute
h1 = HTML("h1", "Hello World", id="heading")

h1.preview_html()
```

Outputs:

```html
<h1 id="heading">Hello World</h1>
```

---

### NOTE:

#### Use Capitalized word if html attribute is in python too (like: 'class' and 'for')

- **example**: word 'class' is a valid attribute in html but it is also a keyword in python,so we cannot use it in python as a variable or something else, so we use capitalized 'Class' instead of 'class', in PyHTML reffering 'class' attribute in html.

##### See Below Example For Better Understanding

---

#### Example 3 : Using attribute class (python keywords)

```python
from pyhtml import HTML

# using class attribute
# notice 'class' is capitalized as 'Class'
# because 'class' is a keyword in python
h1 = HTML("h1", "Hello World", Class="main")

h1.preview_html()
```

Outputs:

```html
<h1 class="main">Hello World</h1>
```

---

#### Example 4: saving the code as .html file

```python
from pyhtml import HTML

h1 = HTML("h1", "Hello World", Class="main")

# save() requires filename as argument
h1.save('h1.html')
```

code in h1.html:

```html
<h1 class="main">Hello World</h1>
```

---

#### Example 5: saving with html5 boilerplate

```python
from pyhtml import HTML

h1 = HTML("h1", "Hello World", Class="main")

# save_as_template() requires filename, optional title as argument
# you can pass css file too: css_filename, additonal_link(bootstrap cdn)
# or, you can use bootstrap cdn too
h1.save_as_template('home.html', title="Hello World")
```

code in home.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Hello World</title>
  </head>
  <body>
    <h1 class="main">Hello World</h1>
  </body>
</html>
```

---

#### Example 6: creating html elements, combining them and saving them into one .html file

```python
from pyhtml import HTML, Html_bundler

h1 = HTML("h1", "Welcome To The Home Page!",Class="heading")
h3 = HTML("h3", "Hello World")
p = HTML("p", "This is a paragraph", id="para")

# Html_bundler() takes data, filename, title, css_filename,additional_link(css or bootstrap cdn) as arguments
Html_bundler(
    h1,
    h3,
    p,
    filename='home.html',
    title="Hello World"
)
```

code in home.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link rel="stylesheet" href="style.css" />
    <title>Hello World</title>
  </head>
  <body>
    <h1 class="heading">Welcome To The Home Page!</h1>
    <h3>Hello World</h3>
    <p id="para">This is a paragraph</p>
  </body>
</html>
```

#### Alternatively you can do the same as above with the below code:

```python
from pyhtml import HTML, Html_bundler

Html_bundler(
    HTML("h1", "Welcome To The Home Page!",Class="heading"),
    HTML("h3", "Hello World"),
    HTML("p", "This is a paragraph", id="para"),
    filename='home.html',
    title="Hello World"
)
```

code in home.html and notice that css filename defaulted to "style.css" you can change that with additonal_link="your_css.css" arg

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link rel="stylesheet" href="style.css" />
    <title>Hello World</title>
  </head>
  <body>
    <h1 class="heading">Welcome To The Home Page!</h1>
    <h3>Hello World</h3>
    <p id="para">This is a paragraph</p>
  </body>
</html>
```

---

#### Example 7: class Render() which only returns html code without saving or creating html file

```python
from pyhtml import HTML, Render

# arguments are: data, title, css_link, additonal_link
# Render -> defaultly returns code with html5 boilerplate
home = Render(
    HTML("h1", "Welcome To The Home Page!",Class="heading"),
    HTML("h3", "Hello World"),
    HTML("p", "This is a paragraph", id="para"),
    title="Hello World"
).html()

print(home) # outputs html with boilerplate

# we can print without the boilerplate too, like given below
print(home.as_element()) # outputs html without boiler plate

# below code will work same as above
"""
h1 = HTML("h1", "Welcome To The Home Page!",Class="heading")
h3 = HTML("h3", "Hello World")
p = HTML("p", "This is a paragraph", id="para")

home = Render(
    h1,
    h3,
    p,
    title="Hello World"
).html()

print(home)
"""
```

outputs below html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <style></style>
    <title>Hello World</title>
  </head>
  <body>
    <h1 class="heading">Welcome To The Home Page!</h1>
    <h3>Hello World</h3>
    <p id="para">This is a paragraph</p>
  </body>
</html>
```

---

### Thanks :)

### Have a nice day
