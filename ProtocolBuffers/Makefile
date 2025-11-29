# Variables
PYTHON = python
PYTHON3 = python3
VENV_DIR = venv
VENV_PYTHON = $(VENV_DIR)/bin/python
VENV_PIP = $(VENV_DIR)/bin/pip

# Compile .proto file
compile-win:
	$(PYTHON) -m grpc_tools.protoc --python_out=. --proto_path=. .\telemetry.proto
# Compile .proto file (Linux with venv)
compile-linux:
	$(VENV_PYTHON) -m grpc_tools.protoc --python_out=. --proto_path=. telemetry.proto
# Clean compiled files
clean-linux:
	rm -f *_pb2.py
clean-win:
	del /Q *_pb2.py
# Run server
run-server-win:
	$(PYTHON) server.py
# Run server (Linux with venv)
run-server-linux:
	$(VENV_PYTHON) server.py
# Run client
run-client-win:
	$(PYTHON) client.py
# Run client (Linux with venv)
run-client-linux:
	$(VENV_PYTHON) client.py
# Create virtual environment (Linux)
venv-create:
	$(PYTHON3) -m venv $(VENV_DIR)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install grpcio-tools protobuf
# Remove virtual environment (Linux)
venv-clean:
	rm -rf $(VENV_DIR)

.PHONY: compile-win compile-linux clean-win clean-linux run-server-win run-server-linux run-client-win run-client-linux venv-create venv-clean