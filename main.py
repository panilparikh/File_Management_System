# main.py

from file_manager import *
from command_parser import CommandParser

class FileManagerApp:
    def __init__(self):
        # Initialize the application with the current directory
        self.current_directory = os.getcwd()

    def display_prompt(self):
        # Display the current directory and a command prompt
        print("\nCurrent Directory:", self.current_directory)
        print("Enter a command or type 'help' for assistance.")

    def execute_command(self, command):
        # Parse the user input using the CommandParser class
        parsed_command = CommandParser.parse(command)
        action = parsed_command[0].lower()

        # Execute the appropriate action based on the parsed command
        if action == "create_file":
            create_file(os.path.join(self.current_directory, parsed_command[1]))
        elif action == "delete_file":
            delete_file(os.path.join(self.current_directory, parsed_command[1]))
        elif action == "rename_file":
            rename_file(
                os.path.join(self.current_directory, parsed_command[1]),
                os.path.join(self.current_directory, parsed_command[2])
            )
        elif action == "create_directory":
            create_directory(os.path.join(self.current_directory, parsed_command[1]))
        elif action == "delete_directory":
            delete_directory(os.path.join(self.current_directory, parsed_command[1]))
        elif action == "copy_file":
            copy_file(
                os.path.join(self.current_directory, parsed_command[1]),
                os.path.join(self.current_directory, parsed_command[2])
            )
        elif action == "move_file":
            move_file(
                os.path.join(self.current_directory, parsed_command[1]),
                os.path.join(self.current_directory, parsed_command[2])
            )
        elif action == "list_files":
            files = list_files(os.path.join(self.current_directory, parsed_command[1]))
            print("Files in", parsed_command[1] + ":")
            print("\n".join(files))
        elif action == "file_info":
            file_path = os.path.join(self.current_directory, parsed_command[1])
            file_info = get_file_info(file_path)
            print(f"File Information for {parsed_command[1]}:")
            print(f"Size: {file_info['size']} bytes")
            print(f"Permissions: {file_info['permissions']}")
            print(f"Creation Time: {file_info['creation_time']}")
        elif action == "search_files":
            query = parsed_command[1]
            matching_files = search_files(self.current_directory, query)
            print(f"Matching Files for '{query}':")
            print("\n".join(matching_files))
        elif action == "cd":
            self.change_directory(parsed_command[1])
        elif action == "help":
            self.display_help()
        elif action == "exit":
            exit()
        else:
            print("Invalid command. Type 'help' for assistance.")

    def change_directory(self, new_directory):
        # Change the current directory and handle exceptions if the directory does not exist
        try:
            os.chdir(os.path.join(self.current_directory, new_directory))
            self.current_directory = os.getcwd()
        except FileNotFoundError:
            print(f"Directory '{new_directory}' not found.")

    def display_help(self):
        # Display a list of available commands
        print("Available Commands:")
        print("create_file <file_name>")
        print("delete_file <file_name>")
        print("rename_file <old_file_name> <new_file_name>")
        print("create_directory <directory_name>")
        print("delete_directory <directory_name>")
        print("copy_file <source_file_path> <destination_path>")
        print("move_file <source_file_path> <destination_path>")
        print("list_files <directory_path>")
        print("file_info <file_path>")
        print("search_files <query>")
        print("cd <directory_name>")
        print("help")
        print("exit")

# Entry point of the application
if __name__ == "__main__":
    # Create an instance of FileManagerApp
    app = FileManagerApp()

    # Main loop to continuously prompt the user for commands
    while True:
        app.display_prompt()
        user_input = input(">> ")
        app.execute_command(user_input)
