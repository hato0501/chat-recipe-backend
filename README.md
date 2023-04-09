Here's a detailed breakdown of the functionality provided by the backend repository for ChatGPT Recipe Assistant:

## Quick Guide
### Settings
- Set `.env` file in root directory:
  ```
  OPENAI_API_KEY=sk-...
  ```

### Local Run
`poetry run uvicorn app.main:app --reload`

## API spec
### API Routers:
- `recipes` - This router allows users to search for recipes with specific ingredients and get recipe suggestions based on menu images

## Structure

### Domain Entities and Interfaces:
- `Recipe` entity - represents information about a recipe, including its name, ingredients, instructions, and portion sizes.
- `IRecipeRepository` interface - defines the contract for interacting with the recipe repository.

### Services:
- `RecipeService` - handles user requests related to recipes by invoking the appropriate repository methods.

### Infrastructure:
- `DynamoRecipeRepository` - implements the `IRecipeRepository` interface using AWS DynamoDB as storage.

### Utilities:
- Various utility functions and classes that support the backend functionality.

### Serverless Architecture:
- Serverless architecture has been used to achieve scalability, and cost-effectiveness

### Authentication and Authorization
- Authentication and authorization are implemented using AWS Cognito

### Database:
- A NoSQL database has been used which is DynamoDB

## Directory Structure:
- The `app` directory contains the core application code for handling API requests and business logic.
- `api/routes` contain Python scripts that define the routing of our RESTful API.
- `domain/entities` contain the entities that store data of the recipes.
- `domain/interfaces` contain the interface(s) that define the contracts to be followed by the repositories.
- `infrastructure/repositorities` define the implementation of the repositories using cloud services like dynamo DB or S3.
- `services` contain Utility functions acting as managers for the operations related to the app
- `utils` holds utilities like logger, validators etc.
- `main.py` initializes the FastAPI app and its routes.
- `tests` directory includes tests for the backend functionality.

## Deployment:
- The `Dockerfile`, `serverless.yml`, `requirements.txt` and `uvicorn.sh` files are included to ensure the application can be built, deployed, and launched consistently across various environments.
Sure, here are the further details on how to use and deploy the ChatGPT Recipe Assistant backend:

### Requirements:
- Python 3.8+
- AWS CLI
- Docker
- Serverless Framework
- An AWS account with admin access

### Usage:
1. Clone the repository.
2. In the project directory, create a virtual environment and activate it.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Set up your AWS credentials by running `aws configure`.
5. Navigate to the `app/core` directory and set up the required environment variables in the `.env` file.
6. Run the application using `python main.py`.

### Deployment:
1. Follow the above steps to set up the app and validate that it works locally.
2. Run `sls deploy`. This will build and package the application using Docker and Serverless framework, and deploy it to your AWS account.
3. Once deployed, you can test the API routes using Postman or cURL.

For more information on how to configure and deploy the ChatGPT Recipe Assistant backend, please refer to the README.md file in the root directory of the repository.