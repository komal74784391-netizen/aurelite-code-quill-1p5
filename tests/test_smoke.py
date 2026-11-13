"""Smoke tests for Quill-1.5."""

import torch

from src.model import Quill1p5Model


def test_forward_shape():
    model = Quill1p5Model(vocab_size=64, dim=64, n_layers=2, n_heads=4, hidden=128)
    tokens = torch.randint(0, 64, (2, 16))
    logits = model(tokens)
    assert logits.shape == (2, 16, 64)
