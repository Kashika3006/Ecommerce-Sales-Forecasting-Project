import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ecommerce_forecast"

list_of_files = [
    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",

    # Core ML pipeline
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",

    # Forecasting logic
    f"src/{project_name}/forecasting/__init__.py",
    f"src/{project_name}/preprocessing/__init__.py",

    # Config
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    # Entities (schemas/contracts)
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    # Utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    # Constants
    f"src/{project_name}/constants/__init__.py",

    # Logging (IMPORTANT)
    f"src/{project_name}/logger/__init__.py",

    # Artifacts (VERY IMPORTANT)
    "artifacts/.gitkeep",

    # Config files
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",

    # Entry points
    "main.py",
    "app/app.py",

    # Streamlit pages
    "app/pages/forecast.py",
    "app/pages/dashboard.py",

    # MLOps
    "Dockerfile",
    "requirements.txt",
    "setup.py",

    # Experiments
    "research/trials.ipynb",

    # Testing
    "test.py"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")