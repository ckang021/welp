from flask.cli import AppGroup
from .users import seed_users, undo_users
from .businesses import seed_businesses, undo_businesses
from .reviews import seed_reviews, undo_reviews
from .categories import seed_categories, undo_categories
from .business_images import seed_business_images,undo_business_images
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_reviews()
        undo_business_images()
        undo_businesses()
        undo_categories()
        undo_users()

    seed_users()
    seed_categories()
    seed_businesses()
    seed_business_images()
    seed_reviews()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_reviews()
    undo_business_images()
    undo_businesses()
    undo_categories()
    undo_users()
    # Add other undo functions here
