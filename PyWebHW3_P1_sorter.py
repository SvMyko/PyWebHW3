import os
import threading
import shutil

def process_directory(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            process_file(directory, filename)
        else:
            threading.Thread(target=process_directory, args=(os.path.join(directory, filename),)).start()

def process_file(directory, filename):
    extension = os.path.splitext(filename)[1]
    if not os.path.exists(extension):
        os.makedirs(extension)
    shutil.move(os.path.join(directory, filename), os.path.join(extension, filename))

def cleanup_directory(directory):
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            cleanup_directory(os.path.join(directory, filename))
            if not os.listdir(os.path.join(directory, filename)):
                os.rmdir(os.path.join(directory, filename))

def main():
    try:
        folder_path = input("Please enter the folder path: ")
        process_directory(folder_path)
        cleanup_directory(folder_path)
        print("Job done")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
