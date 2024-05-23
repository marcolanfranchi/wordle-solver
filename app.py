from nicegui import ui
from wordleSolver import findPossibleWords

# Create the UI
def create_ui():
    dark = ui.dark_mode()
    dark.enable()
    # giving the ui a title
    ui.label('Wordle Solver').classes('text-2xl font-bold mt-4')
    # changing default secondary colour from blue to green
    ui.colors(primary='#42496B')  
    
    with ui.row().classes('items-center justify-center'):
        char_list = [
            ui.input(label='Char 1', value='').classes('w-16'), 
            ui.input(label='Char 2', value='').classes('w-16'), 
            ui.input(label='Char 3', value='').classes('w-16'), 
            ui.input(label='Char 4', value='').classes('w-16'), 
            ui.input(label='Char 5', value='').classes('w-16')
        ]

    # result = ui.label().classes('mt-4')
    log = ui.log().classes('mt-4')

    def on_generate_click():
        input_chars = [str.lower(char.value) for char in char_list]
        # print(input_chars)
        words = findPossibleWords(input_chars)
        log.push('Found words: ' + ', '.join(words) if words else 'No valid words found.')
        # result.text = ', '.join(words) if words else 'No valid words found.'

    ui.button('Generate', on_click=on_generate_click).classes('mt-4')
    ui.button('Clear History', on_click=lambda: log.clear()).classes('mt-4')

    ui.run()


ui.page('/')
create_ui()