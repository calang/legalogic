# Description

# variable definitions, available to all rules
# root directory of this git repo
REPO_ROOT := $(shell git rev-parse --show-toplevel)
# BRANCH := $(shell git branch --show-current)
# BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
LOCAL_REMOTE_DIR := /home/calang/proyects/dvc_localremote/legalogic
# Notes:
# all env variables are available
# = uses recursive substitution
# :=  uses immediate substitution


# ENV_NAME is second word, separated by one space, in file env.yml
ENV_NAME := $(shell head -1 env.yml | cut -d ' ' -f 2)
CUDA_DIR := /home/calang/installed/miniforge3/envs/${ENV_NAME}
XLA_FLAGS := --xla_gpu_cuda_data_dir=${CUDA_DIR}
TF_SETENV := export CUDA_DIR=${CUDA_DIR} XLA_FLAGS=${XLA_FLAGS}


# target: help - Display callable targets.
help:
	@echo "Usage:  make <target>"
	@echo "  where <target> may be"
	@echo
	@egrep -h "^# target:" [Mm]akefile | sed -e 's/^# target: //'


# # target: .venv - create local venv
# .venv:	ALWAYS
# 	python3 -m venv .venv
# 	. .venv/bin/activate; pip install --upgrade pip

# target: requirements - install/update python required packages
requirements:	ALWAYS
	pip install --upgrade -r requirements.txt

# target: update-env - update conda environment based on latest content of environment.yml file
update-env:
	conda env update -f env.yml

# target: rm-env - update conda environment based on latest content of environment.yml file
rm-env:
	conda env remove -n ${ENV_NAME}

# target: spacy -
spacy:	update-env
	python -m spacy download en_core_web_sm
	python -m spacy download en_core_web_md
	python -m spacy download en_core_web_lg
	python -m spacy download en_core_web_trf
	python -m spacy download es_core_news_sm
	python -m spacy download es_core_news_md
	python -m spacy download es_core_news_lg
	python -m spacy download es_dep_news_trf

# target: dvc-init
dvc-init:
	[ -d .dvc ] || dvc init
	mkdir -p data/rawdata
	mkdir -p ${LOCAL_REMOTE_DIR}
	dvc remote add -d localremote ${LOCAL_REMOTE_DIR}

# target: jupl - start jupiter lab server
jupl:	ALWAYS
	@${TF_SETENV}; jupyter lab &


# target push - sample docker image push, asking for passwords
# push: TEMPUSR := $(shell mktemp)
# push:
#	@$$SHELL -i -c 'read -p "username: " user;  echo -n $${user} >$(TEMPUSR)'
#	@$$SHELL -i -c 'read -s -p "password: " user;  echo -n $${user} >$(TEMPUSR)1'
#	@docker login -u $$(cat $(TEMPUSR)) -p $$(cat $(TEMPUSR)1) amr-registry.caas.intel.com
#	docker image push ${APP_IMAGE}
#	@rm $(TEMPUSR)*

# 	@rm $(TEMPUSR)*

# ignore files with any of these names
# so that the rules with those as target are always executed
.PHONY: ALWAYS

# always do/refresh ALWAYS target
ALWAYS:
