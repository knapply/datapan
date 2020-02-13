import os
import sift

# files = os.listdir("test-data")
test_data_dir = "test-data"

# target_extensions = [".json", ".ndjson"]

# target_files = []
# for file in os.listdir(test_data_dir):
#     for ext in target_extensions:
#         if file.endswith(ext):
#             target_files.append(os.path.join(test_data_dir, file))
#             break

# print(target_files)

test = sift.hello_rust(test_data_dir)

for t in test:
    print(t, end="\n\n")

