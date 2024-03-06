# Importing all the neccessary packages.
from huey import RedisHuey
import redis
from models import pair
import os

# Getting the important environment variables.
redis_host = os.environ.get('REDIS_HOST', '172.17.0.2')
redis_port = int(os.environ.get('REDIS_PORT', 6379))


# Making connection to redis and redis queue through huey.
redisdb = redis.Redis(host = redis_host, port = redis_port)
huey = RedisHuey('huey_my_app', host=redis_host, port = redis_port)

# Read task --> to get the existing key-value pair.
@huey.task()
def readTask(key: str):
    # If exists, returs the pair with sucess message.
    if redisdb.exists(key):
        return {
            'message': 'Found.',
            'key': key,
            'value': redisdb.get(key).decode('utf-8')
        }
    
    # If does not exist, returns could not found message.
    return {
        'message': 'Could not found.'
    }

# Create task --> to create new key-value pair.
@huey.task()
def createTask(record: pair):
    key = record.key
    value = record.value

    # If exists, does not create.
    if redisdb.exists(key):
        return {
            'message': 'Already exists.'
        }
    
    # Otherwise, creates new pair.
    redisdb.set(key, value)

    # If creation, successful, returns the new pair with success message.
    if redisdb.exists(key):
        return {
            'message': 'Inserted.',
            'key': key,
            'value': redisdb.get(key).decode('utf-8')
        }
    
    # Otherwise, returns unsuccessful message.
    return {
        'message': 'Unsuccessful insertion.'
    }

# Update task --> to udpate existing key-value pair.
@huey.task()
def updateTask(key: str, value: str):
    # Checks whether the pair exists or not.
    if redisdb.exists(key):
        redisdb.set(key, value.value)

        # If updation is successful, returns the new pair with success messsage.
        if value == redisdb.get(key).decode('utf-8'):
            return {
                'message': 'Updated.',
                'key': key,
                'value': redisdb.get(key).decode('utf-8')
            }

        # Otherwise, returns a message with unsuccessful operation.
        return {
            'message': 'Unsuccessful updation.'
        }
    
    # If not present, returns could not found.
    return {
        'message': 'Could not found.'
    }

# Delete task --> to delete existing key-value pair.
@huey.task()
def deleteTask(key: str):
    # If exists, delete it.
    if redisdb.exists(key):
        value = redisdb.get(key).decode('utf-8')
        
        redisdb.delete(key)

        return {
            'message': 'Deleted.',
            'key': key,
            'value': value
        }
    
    # Otherwise, returns message could not found.
    return {
        'message': 'Could not found.'
    }
