from datetime import datetime, timezone


class TimeUtil:

    @staticmethod
    def get_current_time_utc_str():
        current_time_utc = datetime.now(timezone.utc)

        # Zeit als String ausgeben
        time_str = current_time_utc.strftime("%Y-%m-%d %H:%M:%S")

        return time_str
