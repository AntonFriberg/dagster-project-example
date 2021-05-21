"""Collection of Cereal schedules"""

from dagster import schedule

from pipelines.cereal_pipelines import complex_pipeline  # pylint: disable=unused-import


# https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules
@schedule(
    cron_schedule="0 9 * * 1-5",
    pipeline_name="complex_pipeline",
    execution_timezone="Europe/Stockholm",
)
def every_weekday_9am():
    """Example of how to setup a weekday schedule for a pipeline."""
    return {}
