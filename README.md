# Dagster Project Example

This is an example on how to structure a [Dagster] project in order to organize
the assets, jobs, repositories, schedules, and ops. The example also contains
examples on unit-tests and a docker-compose deployment file that utilizes a
Postgresql database for the run, event_log and schedule storage.

## Getting Started

```bash
pip install -r requirements.txt
```

Then to run dagster in development mode with full UI support. This exposes
the UI on http://localhost:3000 by default.

```bash
dagster dev
```

Note that you can run the main file directly as well since `__main__.py` will be
the entrypoint if you run the `dagster_example` module.

```bash
python -m dagster_example
```