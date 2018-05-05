import javascript
import sys
import time
import traceback
from browser import document, window, alert
from browser import html, console, timer

STATUS = "status"
ECLIPSE_THEME = "ace/theme/eclipse"
MONOKAI_THEME = "ace/theme/monokai"
STORE_SRC = "editor_src"
STORE_THEME = "editor_theme"
PRINT_OUTPUT = "output"
__BRYTHON__.debug = True

if hasattr(window, 'localStorage'):
    from browser.local_storage import storage
else:
    storage = None

editor = window.ace.edit("editor")
session = editor.getSession()
session.setMode("ace/mode/python")
editor.setFontSize(14)
editor.setOptions({
    'enableLiveAutocompletion': True,
    'enableSnippets': True,
    'highlightActiveLine': True,
    'highlightSelectedWord': True
})

EXAMPLE = """# This is a Python comment
print("Welcome to Python and Turtle!")
"""

info = sys.implementation.version
console.log('Brython version %s.%s.%s' % (info.major, info.minor, info.micro))


def editor_on_blur(*args):
    save()

editor.bind('blur', editor_on_blur)

def reset_theme():
    if storage is not None and STORE_THEME in storage:
        update_theme_button(storage[STORE_THEME])
    else:
        update_theme_button(MONOKAI_THEME)

def reset_src():
    if storage is not None and STORE_SRC in storage and storage[STORE_SRC]:
        editor.setValue(storage[STORE_SRC])
    else:
        editor.setValue(EXAMPLE)
    editor.scrollToRow(0)
    editor.gotoLine(0)

def write_out(*args):
    document[PRINT_OUTPUT].value += ''.join(args)

def write_err(*args):
    document[PRINT_OUTPUT].value += ''.join(args)

sys.stdout.write = write_out
sys.stderr.write = write_err


def to_str(xx):
    return str(xx)

def exec_code():
    src = editor.getValue()
    t0 = time.perf_counter()
    try:
        ns = {'__name__':'__main__'}
        exec(src, ns)
    except Exception as exc:
        document[PRINT_OUTPUT].style = {"color": "red"}
        traceback.print_exc()
    console.log('Execution completed in %6.2f ms' % ((time.perf_counter() - t0) * 1000.0))
    end_progress()

def save():
    src = editor.getValue()
    if storage is not None and storage.get(STORE_SRC) != src:
        storage[STORE_SRC] = src

def start_progress():
    document['run'].disabled = True
    window.showSpinner()

def end_progress():
    window.hideSpinner()
    document['run'].disabled = False

@document['run'].bind('click')
def run(*args):
    start_progress()
    clear_output()
    timer.set_timeout(exec_code, 50)

@document['clear'].bind('click')
def clear_output(*args):
    document[PRINT_OUTPUT].value = ''
    document[PRINT_OUTPUT].style = {"color": ""}

def update_theme_button(theme):
    editor.setTheme(theme)
    document['theme'].text = 'Dark' if theme == ECLIPSE_THEME else "Light"

@document['theme'].bind('click')
def toggle_theme(*args):
    theme = ECLIPSE_THEME
    if editor.getTheme() == theme:
        theme = MONOKAI_THEME
    update_theme_button(theme)
    if storage is not None:
       storage[STORE_THEME] = theme

reset_src()
reset_theme()
