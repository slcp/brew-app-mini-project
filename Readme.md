## Running the app
  - From the root of the repo run `python -m src.app`

## VSCode
  - If you are using VSCode with DevContainers there is a container config in the repo

## Virtual Environment
  - To create a `venv` when first pulling this/a python project run `python -m venv .venv` fromt the root of the repo
    - Your `python` command may be different eg. `py, python3`
  - To activate a `venv` run:
    - Windows (in GitBash): `source .venv/Scripts/activate` 
    - OSX/Linux: `source .venv/bin/activate` 
  - To check if you `venv` is activated:
    - Windows (in GitBash): after each shell command it will print `(<name of venv>)` - probably `(venv)`
    - OSX/Linux: The command prompt in your terminal will be prefixed with `(<name of venv>)` - probably `(venv)`
    - On either you can also run `echo $VIRTUAL_ENV` - this environment variable is set by the venv activate script
      - If it prints nothing then the `venv` is not active
      - If it prints `(<name of venv>)` - probably `(venv)` then the `venv` is active
  - To deactivate the `venv` run `deactivate` in the shell when the `venv` is active

## Requirements
  - Installing requirements
    - After creating/activating the `venv` run `pip install -r requirements.txt` from the root of the repo
      - Your `pip` command may be different eg. `pip3`
  - Updating requirements
    - The `venv` should be active. Run `pip freeze > requirements.txt` from the root of your project 

## MySQL DB
  - Start in background: `docker-compose up -d` to run in the background
  - Start in active shell `docker-compose up` to run in the active shell
  - Stop: `docker-compose stop`