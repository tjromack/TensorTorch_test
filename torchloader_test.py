import torch
from torch.utils.data import Dataset, DataLoader

class SimpleDataset(Dataset):
    def __init__(self):
        self.data = torch.tensor([1, 2, 3, 4, 5])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx] * 2

dataset = SimpleDataset()
loader = DataLoader(dataset, batch_size=2, shuffle=True)

for batch in loader:
    print(batch)
