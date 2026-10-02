from hypothesis import given
from hypothesis import strategies as st

from app.algorithms import merge_sort


@given(
    st.lists(
        st.integers(),
        max_size=100,
    )
)
def test_merge_sort_returns_sorted_list(
    data: list[int],
) -> None:
    result = merge_sort(data)

    assert result == sorted(data)


@given(
    st.lists(
        st.integers(),
        max_size=100,
    )
)
def test_merge_sort_preserves_elements(
    data: list[int],
) -> None:
    result = merge_sort(data)

    assert sorted(result) == sorted(data)