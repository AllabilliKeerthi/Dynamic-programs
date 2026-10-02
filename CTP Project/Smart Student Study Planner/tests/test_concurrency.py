import asyncio

from app.concurrency import (
    calculate_square,
    fetch_resource,
    process_subject,
    run_async,
    run_multiprocessing,
    run_threads,
)


def test_process_subject() -> None:
    result = process_subject("Python")

    assert result == "Processed Python"


def test_run_threads(capsys) -> None:
    run_threads()

    output = capsys.readouterr().out

    assert "Processed Python" in output
    assert "Processed Statistics" in output
    assert "Processed AI" in output
    assert "Processed Machine Learning" in output


def test_calculate_square() -> None:
    assert calculate_square(10) == 100
    assert calculate_square(20) == 400
    assert calculate_square(30) == 900
    assert calculate_square(40) == 1600


def test_run_multiprocessing(capsys) -> None:
    run_multiprocessing()

    output = capsys.readouterr().out

    assert "Multiprocessing:" in output
    assert "100" in output
    assert "400" in output
    assert "900" in output
    assert "1600" in output


def test_fetch_resource() -> None:
    result = asyncio.run(
        fetch_resource("Python Notes")
    )

    assert result == "Resource downloaded: Python Notes"


def test_run_async(capsys) -> None:
    asyncio.run(run_async())

    output = capsys.readouterr().out

    assert "Resource downloaded: Python Notes" in output
    assert "Resource downloaded: AI Notes" in output
    assert "Resource downloaded: Statistics Notes" in output