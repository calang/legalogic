# Legalogic

A system to query Costa Rica legal content, based on logic.

Overall architecture is as described in [LLM 
recommendations](docs/Arch_Recom_from_LLMs.md):

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
possible tools and architectures to use.


