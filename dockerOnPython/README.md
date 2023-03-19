# Python Docker

This repository contains a simple Python script that demonstrates how to use the Docker Python library to run a Docker container and print its hostname to the console.
## Prerequisites

Docker must be installed on your local machine.
    If you are running behind a Netfri security certificate, you will need to use the --trusted-host flags when running the pip install command (see step 3 below).

## Usage

To run the Python script, follow these steps:

1.  Open a terminal or command prompt on your local machine.
2.  Navigate to the directory containing the repository.
3.  Run the following command to install the Docker Python library:

```bash
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org docker
```
If you are running behind a Netfri security certificate, you may need to add additional --trusted-host flags for your internal package repository.

Next, run the Python script using the following command:

```bash
python docker_python.py
```

The Python script will create a Docker container running the busybox image and running the command sleep 3600. The container will run in the background, and its hostname will be printed to the console.

Note: The purpose of this script is to demonstrate how to use the Docker Python library, and the specific command _(sleep 3600)_ is used simply as an example. You can modify this command to run any container or command that you like.

  Finally, the script will stop and remove the container.
 
## Troubleshooting

-   If you encounter any issues while running the Python script, make sure that Docker is installed and running on your local machine.
-   If you encounter any other issues, please refer to the Docker documentation or open an issue on this repository.

