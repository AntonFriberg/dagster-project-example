from dagster import schedule
from pipelines.cereal_pipelines import complex_pipeline

# https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules
@schedule(
    cron_schedule="0 9 * * 1-5",
    pipeline_name='complex_pipeline',
    execution_timezone='Europe/Stockholm'
)
def every_weekday_9am():
    return {}