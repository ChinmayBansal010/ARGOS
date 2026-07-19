"""Logging configuration for ARGOS."""

from __future__ import annotations

import logging
import sys
from types import FrameType

from loguru import logger

from argos.settings import AppSettings


class InterceptHandler(logging.Handler):
    """Route standard logging records through Loguru."""

    def emit(self, record: logging.LogRecord) -> None:
        """Forward a logging record to Loguru."""

        try:
            level: str | int = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame: FrameType | None = logging.currentframe()
        depth = 2
        while frame is not None and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def configure_logging(settings: AppSettings) -> None:
    """Configure application logging once at process startup."""

    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.log_level.upper(),
        serialize=False,
        backtrace=False,
        diagnose=False,
    )
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    for name in ("uvicorn", "uvicorn.access", "uvicorn.error", "fastapi"):
        std_logger = logging.getLogger(name)
        std_logger.handlers = [InterceptHandler()]
        std_logger.propagate = False
