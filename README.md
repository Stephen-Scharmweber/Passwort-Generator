# Single Password Generator

A lightweight GUI application for generating and copying individual passwords, built with Python and Tkinter.

## Features

- Generate random passwords with customizable length
- Toggle inclusion of numbers
- Toggle inclusion of special characters
- Customizable set of special characters
- One-click copy to clipboard
- Clean, simple interface

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Usage

1. Run the script: `python password_generator.py`
2. Configure your password:
   - **LENGTH**: Set password length (default: 9)
   - **NUMBERS**: Check to include numbers (0-9)
   - **SPECIAL CHARS**: Check to include special characters
   - **Special chars field**: Edit the special characters to use (default: `!§$%&/()=?+*#-_.:,;<>+-`)
3. Click "GENERATE PASSWORD"
4. Click "COPY PASS" to copy to clipboard

## Customization

You can modify the default values in the code:
- Change default length by modifying `length_entry.insert(0, "9")`
- Change default special characters by modifying `special_chars_entry.insert(0, r"!§$%&/()=?+*#-_.:,;<>+-")`
- Adjust colors by changing `overall_background_button` variable
- Modify fonts by changing `overall_font` and `overall_font_size`

## How It Works

1. The generator creates passwords using:
   - Letters (always included)
   - Numbers (optional)
   - Special characters (optional)
2. When copying:
   - If no password exists, one is generated automatically
   - Password is copied to clipboard
   - Confirmation message appears

## License

This project is open-source and free to use.
