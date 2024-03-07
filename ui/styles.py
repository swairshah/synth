from prompt_toolkit.styles import Style
from prompt_toolkit.styles import merge_styles

black_and_white_style = Style.from_dict({
    'dialog': 'bg:#ffffff',
    'dialog frame.label': 'bg:#000000 #ffffff',
    'dialog.body': 'bg:#ffffff #000000',
    'dialog shadow': 'bg:#000000',
    'button': 'bg:#000000 #ffffff',
    'button.arrow': '#000000',
    'button.focused': 'bg:#ffffff #000000',
    'checkbox': '#000000',
    'checkbox.checked': '#000000',
    'dialog.body label': '#000000',
})

bw_style = Style.from_dict({
    'dialog': 'bg:#222222',
    'dialog frame.label': 'bg:#cccccc #222222',
    'dialog.body': 'bg:#222222 #cccccc',
    'dialog shadow': 'bg:#cccccc',
    'button': 'bg:#cccccc #222222',
    'button.arrow': '#cccccc',
    'button.focused': 'bg:#222222 #cccccc',
    'checkbox': '#cccccc',
    'checkbox.checked': '#cccccc',
    'dialog.body label': '#cccccc',
})
