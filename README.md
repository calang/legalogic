# Legalogic

A system to query Costa Rica legal content, based on logic.

## Background
While LLMs (Large Language Models) have become the to-go 
systems to query about general knowledge, they make 
mistakes, producing wrong answers, with some frequency.

There are environments where precision in the answers is 
a must.

As an alternative to producing the answer to a 
question, we may also refer to logic.  This is an 
approach that has become less popular, over time, due to 
the success of LLMs and also due to its typical labor 
intensity.

Our purpose in this project is to develop an efficient, 
escalable process to produce logic-based mechanisms to 
answer questions on Costa Rica legislation.

The idea is using modern models like LLMs for human 
interface of the system, while using logic to produce 
the actual content of the generated answers.

Main objectives are
- producing answers from literal legal contents
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

### Install environment dependencies
Before using this repo, you will need to install these 
dependencies
- git
- mamba
- swi-prolog

Note: The corresponding version of Python will be 
  installed when the mamba environment is created, below.

### Edit `.env` file
To adjust environment variables to the local 
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
