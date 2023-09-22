import datetime

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=23, minute=36, tzinfo=utc)

