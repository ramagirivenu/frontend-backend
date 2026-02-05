from db import engine, Base
import models

# Create tables
Base.metadata.create_all(bind=engine)
