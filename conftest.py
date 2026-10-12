import base64
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
import pytest_html
from config import BASE_URL


video_path_key = pytest.StashKey[Path]()


@pytest.fixture
def page(request):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()
    video = page.video

    try:
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        try:
            context.close()
        finally:
            try:
                if video is not None:
                    request.node.stash[video_path_key] = Path(video.path())
            finally:
                try:
                    browser.close()
                finally:
                    p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "setup":
        test_script = item.path.read_text(encoding="utf-8")
        extras.append(
            pytest_html.extras.text(
                test_script,
                name=f"Test script: {item.path.name}",
            )
        )

    if report.when == "teardown":
        video_path = item.stash.get(video_path_key, None)
        if video_path is not None:
            video_content = base64.b64encode(video_path.read_bytes()).decode("ascii")
            extras.append(
                pytest_html.extras.video(
                    video_content,
                    name=f"Test video: {item.name}",
                    mime_type="video/webm",
                    extension="webm",
                )
            )

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extras.append(pytest_html.extras.image(str(file_name)))

    report.extras = extras