from redis import Redis
import time
import threading


class StatsManager(object):
    """Manages a connection with redis and maintains statisitcal
    information about the session.
    """

    def __init__(self):
        """Hold a Redis connection for ourselves."""
        self.conn = Redis()
        self.rates = []

        # Poll on another thread.
        t = threading.Thread(target=self.poll_db)
        t.setDaemon(True)
        t.start()

    def get_rate(self):
        """Get the most recent rate."""
        if not self.rates:
            return -1
        return self.rates[-1]

    def poll_db(self):
        """Infinitely poll Redis for new values."""
        while True:
            keys = self.conn.keys()

            if not keys:
                continue

            # Get all keys at all values
            self.values = [self.conn.hgetall(key) for key in keys]

            # Keys are an entire filtered_story object. Here we just pull out
            # the deltas.
            try:
                self.deltas = [int(v['delta']) for v in self.values]
                print self.deltas
            except TypeError as e:
                # print keys
                print e
                continue

            # Compute the rate.
            if self.deltas:
                rate = sum(self.deltas) / float(len(self.deltas))
            else:
                rate = 0

            self.rates.append(rate)
            time.sleep(2)
