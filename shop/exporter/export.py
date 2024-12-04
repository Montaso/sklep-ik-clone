import os
import random
import shutil
import subprocess


folders_to_copy = ["config", "img", "modules", "themes"]
source_path = "../src"
destination_path = "../../config/export"
db_destination_path = "../"

os.makedirs(destination_path, exist_ok=True)

for folder in folders_to_copy:
    source_folder = os.path.join(source_path, folder)
    dest_folder = os.path.join(destination_path, folder)
    if os.path.exists(source_folder):
        os.makedirs(dest_folder, exist_ok=True)
        shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)
        print(f"Copied: {source_folder} -> {dest_folder}")
    else:
        print(f"Source folder not found: {source_folder}")

CONTAINER_NAME = 'mysql'
USER = 'root'
PASSWORD = ('kocham_biznes')
DATABASE = 'sklepik'


dump_filename = f"../dbdump/database-dump{random.randint(0, 1000000)}.sql"

command = [
    "docker", "exec", "-i", CONTAINER_NAME,
    "mysqldump", "-u", USER, f"-p{PASSWORD}", DATABASE
]

try:
    with open(dump_filename, 'w') as dump_file:
        subprocess.run(command, stdout=dump_file, check=True)
    print(f"Dump successful. The dump is saved to {dump_filename}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred during dump: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")