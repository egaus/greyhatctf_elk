FROM python:2
ADD scenario_loader.py /
RUN pip install elasticsearch
CMD [ "python", "./scenario_loader.py", "-i", "/DROP_SCENARIO_FILES_HERE", "-o", "/logs", "-hr", "10"]
