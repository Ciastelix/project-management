#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Capture the output of alembic heads
current_heads=$(alembic heads)

# Use the captured output properly quoted within grep
pending_migrations=$(alembic history --verbose | grep -E 'down revision|revision' | grep -vF "$current_heads")

if [[ ! -z "$pending_migrations" ]]; then
    echo "There are pending migrations. Would you like to apply them now? (y/n)"
    read apply_migrations
    if [[ "$apply_migrations" == "y" ]]; then
        alembic upgrade head
    else
        echo "Please apply pending migrations before creating a new one."
        exit 1
    fi
fi

# Prompt for migration name and create a new migration
echo "Enter the name of the migration: "
read migration_name
alembic revision --autogenerate -m "$migration_name"

echo "Applying new migration..."
alembic upgrade head