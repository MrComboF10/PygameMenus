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

### Setup buttons colors

```
mouse_out_colors = MousePositionButtonColors(button=(0, 255, 255), font=(0, 0, 255), bar=(200, 200, 255))

mouse_over_colors = MousePositionButtonColors(button=(255, 255, 0), font=(255, 0, 0), bar=(255, 165, 0))

colors = ButtonColors(main_slide_1_mouse_over_colors, main_slide_1_mouse_out_colors)
```
#### Objects
mouse_out_colors - Colors of the button when the mouse cursor is outside the button area.

mouse_over_colors - Colors of the button when the mouse cursor in inside the button area.

colors - Colors of the button to be passed to the button object

#### Parameters
button - Background color of the button

font - Color of the font inside button

bar - Color of the bar inside button (only applied in buttons of type SlideButtons)

