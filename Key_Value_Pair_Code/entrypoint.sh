#!/bin/bash

# Run the huey_consumer.py command
python huey_consumer.py huey_tasks.huey -w 4 &

# Run the main.py command
python main.py