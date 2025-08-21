# This is the Pymongo Code to interact
# import os
# from pymongo import MongoClient
# from dotenv import load_dotenv
# from django.core.exceptions import ImproperlyConfigured

# # Load env variables
# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# if not MONGO_URI or not MONGO_DB_NAME:
#     raise ImproperlyConfigured("❌ MongoDB credentials missing in .env")

# # Create Mongo client (singleton)
# client = MongoClient(
#     MONGO_URI,
#     maxPoolSize=100,                  # Connection pool for production
#     minPoolSize=1,
#     serverSelectionTimeoutMS=5000,    # Fail fast if DB unreachable
# )

# try:
#     client.admin.command("ping")  # Test connection
#     print("✅ MongoDB connected")
# except Exception as e:
#     raise ImproperlyConfigured(f"❌ MongoDB connection failed: {e}")

# # Expose database object
# db = client[MONGO_DB_NAME]
