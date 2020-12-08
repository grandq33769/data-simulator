# Third Party Library
import schedule

SCHEDULE = schedule


def every_hour_at(minute: str):
    return SCHEDULE.every().hour.at(f':{minute}')


def every_day_at(trigger_time: str):
    return SCHEDULE.every().day.at(trigger_time)
