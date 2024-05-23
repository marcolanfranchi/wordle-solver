from nicegui import ui
from wordleSolver import findPossibleWords

# Create the UI
def create_ui():
    dark = ui.dark_mode()
    dark.enable()
    # giving the ui a title
    ui.label('Wordle Solver').classes('text-2xl font-bold mt-4')
    ui.label('Enter your characters below and leave missing characters blank to find possible words:').classes('text-medium mt-4')
    # changing default secondary colour from blue to green
    ui.colors(primary='#42496B') 

    ui.space().classes('mt-4')
 

    with ui.row().classes('items-center justify-center'):
        char_list = [
            ui.input(label='1st', value='',
                     validation={'too many letters': lambda value: len(value) < 2}).classes('w-16'), 
            ui.input(label='2nd', value='',
                     validation={'too many letters': lambda value: len(value) < 2}).classes('w-16'), 
            ui.input(label='3rd', value='',
                     validation={'too many letters': lambda value: len(value) < 2}).classes('w-16'), 
            ui.input(label='4th', value='', 
                     validation={'too many letters': lambda value: len(value) < 2}).classes('w-16'), 
            ui.input(label='5th', value='', 
                     validation={'too many letters': lambda value: len(value) < 2}).classes('w-16')
        ]

    ui.space().classes('mt-4')


    # result = ui.label().classes('mt-4')
    log = ui.log().classes('mt-4')

    def on_generate_click():
        input_chars = [str.lower(char.value) for char in char_list]
        # print(input_chars)
        words = findPossibleWords(input_chars)
        log.push('Found words: ' + ', '.join(words) if words else 'No valid words found.')

    ui.button('Generate', on_click=on_generate_click).classes('mt-4')
    ui.button('Clear History', on_click=lambda: log.clear()).classes('mt-4')

    ui.run()


ui.page('/')
create_ui()