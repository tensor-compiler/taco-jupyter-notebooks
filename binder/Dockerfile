FROM python:3.7-slim

RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook

RUN pip install numpy
RUN pip install scipy

RUN apt-get update && apt-get install -y build-essential && apt-get -y install cmake protobuf-compiler

RUN apt-get install -y git

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

WORKDIR ${HOME}
USER ${USER}

COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

RUN git clone https://github.com/tensor-compiler/taco.git -b second-taco
RUN cd taco && \
	mkdir build && \
	cd build && \
	cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON=ON .. && \
	make -j8

ENV PYTHONPATH "${PYTHONPATH}:taco/python_bindings"
