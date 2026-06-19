### Using Basic Python Virtual Manager
1. create requirements.txt and go to https://pypi.org/
2. Open terminal, execute this command python -m venv .venv
3. Activate virtual environment:
On Windows: ``` .venv\Scripts\activate```
On Linux/macos: ```source .venv/bin/activate```
4. Use ```pip list``` for testing
5. Install the packages using ```pip install -r requirements.txt```
6. Use ```pip list``` to validate

### Using uv 
1. deactivate old python env and delete .venv
1. uv init
2. Create Virtual Environment: uv venv
3. Activate virtual environment:
On Windows: ``` .venv\Scripts\activate```
On Linux/macos: ```source .venv/bin/activate```
4. Install packages:  ``` uv add requests==2.34.2 torch```
5. uv pip list
