from datasets import load_dataset

ds = load_dataset("espejelomar/code_search_net_python_10000_examples")

print(ds['train'].column_names)


print("done")