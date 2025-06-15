FROM apache/airflow:3.0.2

USER root

RUN apt-get update \
&& apt-get install -y --no-install-recommends \
        vim \
&& apt-get autoremove -yqq --purge \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Install OpenJDK-17
RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
RUN export JAVA_HOME

USER airflow
# Install Python packages
COPY requirements.txt .

RUN pip install -r requirements.txt 
