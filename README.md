# Explaining Bugs with LLMs

Machine Learning for Software Engineering Seminar @HPI

## Setup 🛠

[Python](https://www.python.org/downloads/) and a package manager like [pip](https://pip.pypa.io/en/stable/installation/)
and/or [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) need to be installed on your system.

1. Open your terminal and clone the repository:

   ```bash
   git clone https://github.com/valeriatisch/ml4testing.git
   ```
   
   To update the repo with remote changes, run:
    
    ```bash
    git pull
    ```

2. We recommend using a virtual environment.
You can create and activate a new environment with conda or another package manager of your preference.

   ```bash
    conda create -n ml4testing pip python=3.8
    conda activate ml4testing
    ```
   
   You will be asked to proceed; type `y` and enter. This might take a while.
   
   To deactivate the environment, run:
   ```shell
   conda deactivate
   ```

   To remove the environment, run:
   ```shell
   conda remove -n ml4testing --all
   ```
   Hint: You can use [direnv](https://direnv.net/) to automatically (de)activate the environment when you enter the directory.
Install direnv and run `direnv allow .` inside the repo. That is what the `.envrc` file is for.

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory of the project and add the following variables:

   ```bash
   GITHUB_TOKEN=<your github token>
   REPO=<your username>/<your reponame>
   OPENAI_API_KEY=<your openai api key>
   ```
   
   Find an example in `.env.example`. <br>
   Note:
   - The GitHub Token needs to have permissions to read and write issues on this repository.
   - The OpenAI API Key can be generated [here](https://platform.openai.com/api-keys). You need to have a payment method set.

5. You can run the app with:

   ```bash
   python main.py
   ```

## Development 🚀

### Setting Up Pre-Commit in Your Local Development Environment

   To keep the code clean and consistent, we use [pre-commit](https://pre-commit.com/) as a linter
   and [black](https://black.readthedocs.io/en/stable/) as a code formatter.

   The configuration is stored in `.pre-commit-config.yaml`.

   Inside the repo, run:

   ```bash
   pre-commit install
   ```

   Now, pre-commit will run automatically on `git commit`.
   
   If you want to run it manually on all files, use `pre-commit run --all-files`
   or `pre-commit run <file>` for a specific file. This works only on files that are added.

   Run `black .` to format all files automatically or `black <file>` for a specific file.
