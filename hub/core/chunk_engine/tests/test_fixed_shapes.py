from typing import Tuple

import numpy as np
import pytest
from hub.constants import GB, MB
from hub.core.chunk_engine.tests.common import (
    get_random_array,
    run_engine_test,
)
from hub.tests.common import (
    parametrize_dtypes,
    parametrize_chunk_sizes,
    parametrize_num_batches,
    SHAPE_PARAM,
)
from hub.core.tests.common import (
    parametrize_all_caches,
    parametrize_all_storages_and_caches,
)
from hub.core.typing import StorageProvider
from hub.tests.common import current_test_name

np.random.seed(1)


UNBATCHED_SHAPES = (
    (1,),
    (100,),
    (1, 1, 3),
    (20, 90),
    (3, 28, 24, 1),
)


BATCHED_SHAPES = (
    (1, 1),
    (10, 1),
    (1, 30, 30),
    (3, 3, 12, 12, 1),
)


@pytest.mark.parametrize(SHAPE_PARAM, UNBATCHED_SHAPES)
@parametrize_num_batches
@parametrize_chunk_sizes
@parametrize_dtypes
@parametrize_all_storages_and_caches
def test_unbatched(
    shape: Tuple[int],
    chunk_size: int,
    num_batches: int,
    dtype: str,
    storage: StorageProvider,
):
    """
    Samples have FIXED shapes (must have the same shapes).
    Samples are provided WITHOUT a batch axis.
    """

    arrays = [get_random_array(shape, dtype) for _ in range(num_batches)]
    run_engine_test(arrays, storage, batched=False, chunk_size=chunk_size)


@pytest.mark.parametrize(SHAPE_PARAM, BATCHED_SHAPES)
@parametrize_num_batches
@parametrize_chunk_sizes
@parametrize_dtypes
@parametrize_all_storages_and_caches
def test_batched(
    shape: Tuple[int],
    chunk_size: int,
    num_batches: int,
    dtype: str,
    storage: StorageProvider,
):
    """
    Samples have FIXED shapes (must have the same shapes).
    Samples are provided WITH a batch axis.
    """

    arrays = [get_random_array(shape, dtype) for _ in range(num_batches)]
    run_engine_test(arrays, storage, batched=True, chunk_size=chunk_size)