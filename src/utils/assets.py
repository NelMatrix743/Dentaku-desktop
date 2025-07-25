# - - - DEFINING ASSETS  - - -

# app resource related assets
APP_NAME: str = "Dentaku"
APP_ICON: str = "assets/icons/app_icon.png"

# math related assets
DEFAULT_VALUE: str = '0'
OPERATORS: set[str] = {'×', '÷'}
PARCELABLE_OPERATORS: dict[str, str] = {
    '×'  :  '*',
    '÷'  :  '/'
}
