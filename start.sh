#!/bin/bash

uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload

chmod +x start.sh