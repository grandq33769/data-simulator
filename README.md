# Data Simulator

Data simulator for different project with custom configuration

## Development

### Dev Prerequisites

| Name | Version |
| --- | --- |
| Python | 3.7 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

1. Initialize environment variable

   ```bash
   cp sample.env .env
   ```

1. Initialize Dev Python environment with pre-commit

   ```bash
   make pre-commit
   ```

1. Enter the environment and start developing

   ```bash
   pipenv shell
   ```

1. Commit your code

   ```bash
   make commit
   ```

### Formatting

This project uses `black` and `isort` for formatting

   ```bash
   make reformat
   ```

### Linting

This project uses `pylint` and `flake8` for linting

   ```bash
   make lint
   ```

### Testing

This project uses `pytest` and its extension(`pytest-cov`) for testing

   ```bash
   make test
   ```

## Deployment

### Deployment Prerequisites

| Name | Version |
| --- | --- |
| Docker | 19.03.6 |
| docker-compose | 1.17.1 |

### Deployment Steps

1. Build the image or pull from ECR

   ```bash
   docker-compose build
   ```

   This will build the image with tag `private-cloud-streaming:test`

1. Start containers

   ```bash
   docker-compose up -d
   ```

## Contribution

* Darkborderman/Divik(reastw1234@gmail.com)
* grandq33769/Aiden Leung(grandq33769@gmail.com)
  