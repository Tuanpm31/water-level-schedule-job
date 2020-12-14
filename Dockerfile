FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

ENV TZ=Asia/Ho_Chi_Minh

# install dependencies
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install \
  git+https://github.com/ozgur/python-firebase@0d79d7609844569ea1cec4ac71cb9038e834c355

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "./main.py" ]