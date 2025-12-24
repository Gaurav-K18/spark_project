FROM apache/spark:3.5.1

USER root

# ---------- System packages ----------
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    curl \
    gnupg2 \
    unixodbc \
    unixodbc-dev \
    vim \
    nano \
    bash-completion \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---------- Microsoft ODBC Driver ----------
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list \
       > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# ---------- Python packages ----------
RUN pip3 install --no-cache-dir \
    jupyterlab \
    pyspark \
    numpy \
    pandas \
    ipython \
    pyodbc

# ---------- Jupyter directories ----------
RUN mkdir -p /home/spark/.local/share/jupyter/runtime \
    && mkdir -p /opt/spark-notebooks \
    && chown -R spark:spark /home/spark \
    && chown -R spark:spark /opt/spark-notebooks

# ---------- Switch user ----------
USER spark
ENV SHELL=/bin/bash
WORKDIR /opt/spark-notebooks

EXPOSE 8888 4040

# ---------- Start Jupyter ----------
CMD ["python3", "-m", "jupyterlab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]
