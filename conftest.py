import os
from collections.abc import Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Video, sync_playwright
from pytest_html import extras
from config import BASE_URL


_video_path_key = pytest.StashKey[Path]()
_screenshot_path_key = pytest.StashKey[Path]()
_video_key = pytest.StashKey[Video]()
_context_key = pytest.StashKey[BrowserContext]()


@pytest.fixture(scope="session")
def browser() -> Iterator[Browser]:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(request: pytest.FixtureRequest, browser: Browser) -> Iterator[Page]:
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir.resolve()),
    )
    request.node.stash[_context_key] = context

    video: Video | None = None
    try:
        page = context.new_page()
        video = page.video
        if video is None:
            raise RuntimeError("Playwright video recording was not initialized")

        request.node.stash[_video_key] = video
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        if not context.is_closed():
            context.close()
        if video is not None:
            request.node.stash[_video_path_key] = Path(video.path())


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    outcome = yield
    context = item.stash.get(_context_key, None)
    video = item.stash.get(_video_key, None)
    page = item.funcargs.get("page")

    if context is not None:
        exception = outcome.excinfo[1] if outcome.excinfo else None
        try:
            if (
                exception
                and not isinstance(exception, pytest.skip.Exception)
                and page
                and not page.is_closed()
            ):
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)
                screenshot_path = screenshots_dir / f"{item.name}.png"
                page.screenshot(path=str(screenshot_path))
                item.stash[_screenshot_path_key] = screenshot_path
        finally:
            if not context.is_closed():
                context.close()

        if video is not None:
            item.stash[_video_path_key] = Path(video.path())


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report_extras = getattr(report, "extras", [])

    if report.when == "call" or (
        report.when == "setup" and report.outcome in {"failed", "skipped"}
    ):
        test_script = Path(str(item.fspath))
        report_extras.append(
            extras.text(
                test_script.read_text(encoding="utf-8"),
                name=f"Test script: {test_script.name}",
            )
        )

        screenshot_path = item.stash.get(_screenshot_path_key, None)
        if report.when == "call" and report.failed and screenshot_path:
            report_extras.append(extras.image(str(screenshot_path)))

        video_path = item.stash.get(_video_path_key, None)
        if video_path and video_path.is_file():
            html_path = item.config.getoption("htmlpath")
            if html_path:
                report_dir = Path(html_path).resolve().parent
            else:
                report_dir = Path.cwd()
            relative_video_path = Path(
                os.path.relpath(video_path.resolve(), report_dir)
            ).as_posix()
            report_extras.append(
                extras.video(
                    relative_video_path,
                    name=f"Test recording: {item.name}",
                    mime_type="video/webm",
                    extension="webm",
                )
            )

        report.extras = report_extras
