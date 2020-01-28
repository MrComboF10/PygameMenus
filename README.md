# PygameMenus
Make menus for pygame with PygameMenus

This packages helps you to not waste time creating menus for games or others pygame projects.

## Commands

### Install

```
py -m pip install PygameMenus
```

### Upload to PyPI

Go to project root folder
```
py setup.py sdist
py -m twine upload dist/*
```

### Release new version to PyPI

Update version number in setup.py
```
py setup.py sdist
py -m twine upload --skip-existing dist/*
```

## Examples

### Setup button colors

```
mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))

mouse_over_colors = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))

button_colors = ButtonColors(mouse_over_colors, mouse_out_colors)
```
#### Objects
mouse_out_colors - Colors of the button when the mouse cursor is outside the button area.

mouse_over_colors - Colors of the button when the mouse cursor in inside the button area.

button_colors - Colors of the button to be passed to the button object.

#### Parameters
button - Background color of the button.

font - Color of the font inside button.

bar - Color of the bar inside button (only applied in buttons of type SlideButtons).

### Create button

```
button_font = FloatFont("Arial", 70)

button_range = range(101)

slide_button = SlideButton(button_font, 10, button_range, button_colors)
```
#### Objects
button_font - font inside button (Object of PygameFloatObjects package).

button_range - list of all values that can be displayed on the button (In this case, when the bar is leaning to left the value is 0 and when the bar is leaning to the right the value is 100).

slide_button - type of button which has a slide bar (object of PygameMenus package).

##### Variables
10 - bar width.
