import logging

# Create a custom logger
logger = logging.getLogger()
logger.setLevel('DEBUG')

# Create handlers
stdout_handler = logging.StreamHandler()

stdout_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
logging_format = logging.Formatter('%(asctime)s - %(process)d - %(levelname)s - %(name)s - %(message)s')
stdout_handler.setFormatter(logging_format)

# Add handlers to the logger
logger.addHandler(stdout_handler)
