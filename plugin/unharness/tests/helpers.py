import signal
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


@contextmanager
def deadline(seconds: int) -> Iterator[None]:
    """Raise TimeoutError in the block when it runs longer than the seconds."""

    def expire(signum, frame):
        raise TimeoutError(f"the block ran past {seconds} seconds")

    previous = signal.signal(signal.SIGALRM, expire)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)
