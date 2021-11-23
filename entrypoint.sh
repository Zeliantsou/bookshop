#!/bin/sh

alembic upgrade head
python init_data.py
uvicorn main:app --reload --host 0.0.0.0 --port 8000
