# Evaluation metrics for large language models in a named entity extraction task documentation!

## Description

...

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `gsutil rsync` to recursively sync files in `data/` up to `gs://ms-24-12-bk/data/`.
* `make sync_data_down` will use `gsutil rsync` to recursively sync files in `gs://ms-24-12-bk/data/` to `data/`.


