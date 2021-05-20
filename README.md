# Dagster Project Example

This is an example on how to structure a [Dagster] project in order to organize
the pipelines, repositories, schedules, and solids. The example also contains
examples on unit-tests and a docker-compose deployment file that utilizes a
Postgresql database for the run, event_log and schedule storage.

This example should in no way be considered suitable for production and is
marely my own example of a possible file structure. I personally felt that it
was difficult to put the Dagster concepts to use since the projects own examples
had widely different structure and was difficult to overview as a beginner.

The example is based on the official [tutorial].

# Getting Started

To run the example simply do

```
docker-compose up -d
```

This will build the Docker image and pull Postgresql dependency. The dagster
dashboard is then available on http://localhost:3000

# Running outside Docker

There is an example on how to run a single pipeline in `src/main.py`. First
install the dependencies in an isolated Python environment.

```
pip install -r requirements
```

Then run the `main.py` script from the `src/` folder.

```
cd src/
python -m main
```

# Other Examples

- https://github.com/pybokeh/dagster-sklearn
    - Gave me the inspiration for the primary folder structure. Although that
      example is more advanced and utilizes sklearn.
- https://github.com/dagster-io/dagster/tree/master/examples
    - Dagster's own examples.
- https://github.com/sephib/dagster-graph-project
- https://github.com/sspaeti-com/practical-data-engineering

[Dagster]:(https://dagster.io/)
[tutorial]:(https://docs.dagster.io/tutorial)
