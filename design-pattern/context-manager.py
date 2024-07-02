class MyContextManager:
  def __enter__(self):
    print("enter")
    return self

  def __exit__(self, exc_type, exc_value, traceback):
      # Cleanup code
      print("Exiting the context")
      if exc_type is not None:
          print(f"An exception occurred: {exc_value}")
      # Return True if you want to suppress the exception
      return False
  
# Using the context manager with the 'with' statement
with MyContextManager() as manager:
    print("Inside the context")
    # You can raise an exception to see how the context manager handles it
    raise ValueError("Something went wrong")



# scenarios:

# File Handling:

# Opening and closing files safely to ensure resources are properly managed and files are not left open accidentally.
# python
# Copy code
# with open('example.txt', 'r') as file:
#     content = file.read()
# # File is automatically closed after the 'with' block
# Database Connections:

# Connecting to databases and ensuring connections are properly closed after use to avoid resource leaks.
# python
# Copy code
# import psycopg2

# with psycopg2.connect(database="mydatabase", user="myuser", password="mypassword") as conn:
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM mytable")
#         rows = cur.fetchall()
# # Connection is automatically closed after the 'with' block
# Locks and Synchronization:

# Acquiring locks and releasing them in multi-threaded or multi-process environments to prevent race conditions and ensure data integrity.
# python
# Copy code
# import threading

# lock = threading.Lock()

# def safe_increment():
#     with lock:
#         # Critical section where the lock is held
#         global counter
#         counter += 1
# Temporary Modifications:

# Temporarily modifying the environment or global state and ensuring that changes are reverted afterward.
# python
# Copy code
# import os

# with temporary_environment(PATH='/new/path'):
#     # Code that runs with modified environment variables
# # Environment changes are automatically reverted after the 'with' block
# Resource Allocation and Deallocation:

# Managing resources that need to be allocated and released in a specific sequence, ensuring proper cleanup.
# python
# Copy code
# with allocate_resources() as resources:
#     # Code that uses allocated resources
# # Resources are automatically deallocated after the 'with' block
# Custom Contexts:

# Implementing custom behavior or actions before and after a specific block of code executes, encapsulating complex setup and teardown logic.
