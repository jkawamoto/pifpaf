import logging

print("called")
try:
    logging.basicConfig(level=logging.DEBUG)
except Exception as e:
    print(e)
    raise
