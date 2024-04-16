import torch
import numpy
model = torch.hub.load("gmberton/eigenplaces", "get_trained_model", backbone = "REsNet50", fc_output_dim = 2048)