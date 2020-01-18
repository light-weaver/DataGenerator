# %%
from datagenerator.generateData import create_datasets

# %% Create training benchmark data
create_datasets(folder="./datasets/benchmark_train")

# %% create testing benchmark data
create_datasets(
    folder="./datasets/benchmark_test", distribution=["uniform"], num_samples=[10000]
)

# %% create optimal benchmark data
create_datasets(
    folder="./datasets/benchmark_optimal", distribution=["optimal"], num_samples=[10000]
)


# %% Create training engineering data
from datagenerator.generateengineeringdata import create_datasets as cd_eng

cd_eng(name="train")

# %% Create testing engineering data

cd_eng(num_samples_options=[10000], distribution=["lhs"], name="test")
