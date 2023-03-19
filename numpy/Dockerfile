FROM python:latest
RUN mkdir ~/.pip && echo "[global] \ntrusted-host = pypi.python.org pypi.org files.pythonhosted.org \n" > ~/.pip/pip.conf RUN pip install cv2
RUN pip install numpy matplotlib
COPY rgb_by_numpy.py /app/

COPY assets/light_blue.png /app/images/
WORKDIR /app
CMD ["python", "rgb_by_numpy.py"]

