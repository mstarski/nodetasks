import json
import os
from subprocess import call
from iterfzf import iterfzf


def main():
    package_file_path = find_nearest_package_file()
    with open(package_file_path) as file:
        scripts = json.load(file)["scripts"]
        script_keys = list(scripts.keys())
        chosen_script = iterfzf(script_keys)

        if chosen_script:
            call([f"npm run {chosen_script}"], shell=True)


def find_nearest_package_file():
    cwd = os.getcwd()

    if cwd == "/":
        raise LookupError(
            "package.json not found - are you sure, you are inside a valid node project directory?")

    if os.path.exists(f'{cwd}/package.json'):
        return f'{cwd}/package.json'
    else:
        os.chdir('../')
        find_nearest_package_file()


if __name__ == "__main__":
    main()
