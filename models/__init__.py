#!/usr/bin/python3
"""
instanciates the filestorage class and reloads it
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
