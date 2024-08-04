FROM alpine:3.20.1

# Install dependencies
RUN apk add --no-cache python3=3.12.3-r1 py3-flask=3.0.3-r0 py3-werkzeug=3.0.3-r0

# Copy the app data *after* dependencies so we can use the cache in testing
COPY ./src/ /app
WORKDIR /app

# This already exists but commented just in case that changes
#RUN addgroup -S www-data
# The user does not exist
RUN adduser -S www-data -G www-data &&\
    chown -R www-data:www-data /app

USER www-data

# Pass in Flask app name
ENV FLASK_APP main.py
# For some reason middleware injection
# only works in debug mode (seems smart tbh)
ENV FLASK_DEBUG 1

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV FLAG "pecan{1t_h45_4_c00l_5173M4P_tO0!}"

# Run the app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "-p", "8000"]

EXPOSE 8000
