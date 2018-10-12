import components
import sys

# the primary container for all possible commands
command_list = {"pipe": components.add_component,
                "elbow": components.add_component,
                "exit": sys.exit}


# primary input callback from ui
def input_manager(event, args):
    print("event type: " + str(event.type))
    command_input = args[0].get()
    output_label = args[1].label.label
    if command_input in command_list:
        output_label.config(text='creating ' + str(args[0].get()) + '...')
        command_list.get(command_input)(command_input)
    else:
        output_label.config(text='bad command!')
    args[0].delete(0, len(args[0].get()))
