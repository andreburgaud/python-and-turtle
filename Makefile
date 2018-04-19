# Makefile to help managing the project (run, deploy, clean...)

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -rf

run:
	dev_appserver.py app.yaml

debug:
	dev_appserver.py --log_level debug app.yaml

deploy:
	gcloud app deploy pythonandturtle/app.yaml --project=pythonandturtle


update:
	gcloud components update

help:
	@echo 'Makefile for Python and Turtle web site                                                 '
	@date
	@echo '                                                                                        '
	@echo 'Usage:                                                                                  '
	@echo '    make clean              Delete temp files (*.pyc), caches (__pycache__)             '
	@echo '    make run                Start server                                                '
	@echo '    make debug              Start server with debug log level                           '
	@echo '    make deploy             Deploy project to GAE                                       '

.PHONY: clean run debug deploy