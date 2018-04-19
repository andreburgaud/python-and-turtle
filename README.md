# Overview

Source code for web site https://pythonandturtle.com

# Update gcloud

```
$ gcloud components update
```

# Running Server

```
$ dev_appserver.py --log_level debug app.yaml
```

# Deploying Server

```
$ gcloud app deploy pythonandturtle/app.yaml --project=pythonandturtle
```