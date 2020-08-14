FROM vyahello/pep8-checker-base:0.0.1
LABEL version=0.0.2 \
      metadata="The main image for pep8-checker application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ARG REPOSITORY
ARG AWS_ENDPOINT
ENV CODE_DIR="/code" \
    IMAGE_VERSION=${VERSION} \
    IMAGE_REPO=${REPOSITORY} \
    AWS_ENDPOINT=${AWS_ENDPOINT}
WORKDIR ${CODE_DIR}
COPY checker checker
COPY requirements.txt docker-entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/code/docker-entry.sh"]