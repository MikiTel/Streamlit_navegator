#!/bin/sh
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
python3 -m venv local_test_env
source local_test_env/bin/activate
pip3 install -r requirements.txt
streamlit run datafiltering.py --server.port=8080 --server.enableCORS=false --server.enableXsrfProtection=false
deactivate