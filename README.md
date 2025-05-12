# Legalogic

A system to query Costa Rica legal content, based on logic.

## Background
While LLMs (Large Language Models) have become the to-go 
systems to query about general knowledge, they make 
mistakes, producing wrong answers with some frequency.

There are environments where precision in the answers is 
a must.

As an alternative method to producing the answer to a 
question, we may also refer to logic.  This is an 
approach that has become less popular, over time, due to 
the success of LLMs and also due to its typical labor 
intensity.

Our purpose in this project is to develop an efficient, 
escalable process to produce logic-based mechanisms to 
answer questions on Costa Rica legislation.

The idea is using modern models like LLMs for human 
interface of the system, while using logic to produce 
the generated answers.

Main objectives are
- develop a scalable pipeline, as automated as possible
- produce answers from legal contents 
- develop the capability to detect contradictions across 
  different legal contents

## Overall architecture
As described in [LLM 
recommendations](docs/Arch_Recom_from_LLMs.md)

```text
Legal Texts (Costa Rica) 
   ↓
Text Extraction (pdfminer, spaCy)
   ↓
Syntactic Parsing (spaCy, CoreNLP)
   ↓
Information Extraction (Rules + Patterns)
   ↓
Logical Form Encoding (Prolog / ASP)
   ↓
Symbolic Reasoner (SWI-Prolog / Clingo)
   ↓
Answers to Questions (GUI or CLI)
```

[docs/Readme.md](docs/README.md) contains details of 
tools and architectures.

## Set-up
This repo was created to be used in a **Linux** environment; 
specifically Ubuntu 24.10.

If you want to use it in a different development 
environment, you will need to do the appropriate changes.

The repo is 
based on Python, Python-related utilities, SWI-Prolog 
and Makefiles, 
which are all available on the most common platforms.
We hope you 
should be able to run the code in this repo on 
other platforms with minimal 
adjustments.

### Install environment dependencies
Before using this repo, you will need to install these 
dependencies
- git
- mamba
- swi-prolog

Note: The corresponding version of Python will be 
  installed when the mamba environment is created, below.

### Clone the repo in the local system
```shell
git clone https://github.com/calang/legalogic.git
```

### Edit `.env` file
Adjusting environment variables to the local 
system.

### Create conda (mamba) environment
From a terminal on the repo root directory:
```shell
make update-env
```

### Initialize other utilities
From a terminal on the repo root directory:
```shell
make spacy
make dvc-init
```

## How to use
Become acquainted with
- git
- dvc
- spacy

and follow the scripts in `Makefile` and `dvc.yaml` files 
and in the 
`src` directory.

## Authors
- [Carlos Lang]
  - [Linked-in](https://www.linkedin.com/in/carlos-lang-b918893/)
  - carlos.lang (at) gmail.com

## Possible additions
- Use `poetry` to build and publish.
