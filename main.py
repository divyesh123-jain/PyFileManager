import os
import shutil

def print_menu():
    print("Command Line File Manager Menu:")
    print("1. List files in current directory")
    print("2. Navigate to a different directory")
    print("3. View file contents")
    print("4. Copy file")
    print("5. Move file")
    print("6. Delete file")
    print("7. Show available drives")
    print("8. Open drive")
    print("9. Exit")

def list_files(directory):
    print("Files in", directory)
    for file in os.listdir(directory):
        print(file)

def navigate_directory():
    directory = input("Enter directory path: ")
    if os.path.isdir(directory):
        return directory
    else:
        print("Invalid directory path")
        return None

def view_file_contents(directory):
    filename = input("Enter file name: ")
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            print(file.read())
    else:
        print("File not found")

def copy_file(directory):
    filename = input("Enter file name to copy: ")
    source = os.path.join(directory, filename)
    if os.path.isfile(source):
        destination = input("Enter destination directory: ")
        if os.path.isdir(destination):
            shutil.copy(source, destination)
            print("File copied successfully")
        else:
            print("Invalid destination directory")
    else:
        print("File not found")

def move_file(directory):
    filename = input("Enter file name to move: ")
    source = os.path.join(directory, filename)
    if os.path.isfile(source):
        destination = input("Enter destination directory: ")
        if os.path.isdir(destination):
            shutil.move(source, destination)
            print("File moved successfully")
        else:
            print("Invalid destination directory")
    else:
        print("File not found")

def delete_file(directory):
    filename = input("Enter file name to delete: ")
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("File deleted successfully")
    else:
        print("File not found")

def show_available_drives():
    drives = [drive + ':' for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(drive + ':')]
    print("Available drives:", ", ".join(drives))

def open_drive():
    drive = input("Enter drive letter to open (e.g., 'C:'): ")
    if os.path.exists(drive):
        os.chdir(drive)
        print("Drive", drive, "opened")
    else:
        print("Drive not found")

def main():
    current_directory = os.getcwd()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            list_files(current_directory)
        elif choice == '2':
            new_directory = navigate_directory()
            if new_directory:
                current_directory = new_directory
        elif choice == '3':
            view_file_contents(current_directory)
        elif choice == '4':
            copy_file(current_directory)
        elif choice == '5':
            move_file(current_directory)
        elif choice == '6':
            delete_file(current_directory)
        elif choice == '7':
            show_available_drives()
        elif choice == '8':
            open_drive()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
