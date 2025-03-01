#!/bin/bash

# Define the .env file path
ENV_FILE=".env"

# Prompt user for DB credentials (optional, can press Enter to use defaults)
read -p "Enter Database User [default: root]: " DB_USER
DB_USER=${DB_USER:-root}

read -p "Enter Database Password [default: 1234]: " DB_PASSWORD
DB_PASSWORD=${DB_PASSWORD:-1234}

read -p "Enter Database Host [default: localhost]: " DB_HOST
DB_HOST=${DB_HOST:-localhost}

read -p "Enter Database Name [default: car_rental]: " DB_NAME
DB_NAME=${DB_NAME:-car_rental}

# Create or overwrite the .env file
echo "Creating $ENV_FILE file..."
cat <<EOL > $ENV_FILE
DB_USER=$DB_USER
DB_PASSWORD=$DB_PASSWORD
DB_HOST=$DB_HOST
DB_NAME=$DB_NAME
EOL

echo "$ENV_FILE file created successfully!"
echo "Contents of $ENV_FILE:"
cat $ENV_FILE
