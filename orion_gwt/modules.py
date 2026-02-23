"""Specialized processing modules for GWT"""
from dataclasses import dataclass, field
from typing import Any, Optional
import numpy as np

@dataclass
class ModuleOutput:
    content: Any
    strength: float
    source: str
    timestamp: float = 0.0

@dataclass
class Module:
    name: str
    capacity: int = 100
    activation: float = 0.0
    _buffer: list = field(default_factory=list)
    
    def process(self, input_data: Any) -> ModuleOutput:
        """Process input and produce output with activation strength"""
        self.activation = min(1.0, self.activation + np.random.exponential(0.3))
        return ModuleOutput(
            content=f"{self.name}_processed: {input_data}",
            strength=self.activation,
            source=self.name
        )
    
    def receive_broadcast(self, broadcast_data: Any):
        """Receive broadcast from global workspace"""
        self._buffer.append(broadcast_data)
        if len(self._buffer) > self.capacity:
            self._buffer = self._buffer[-self.capacity:]
    
    def reset(self):
        self.activation = 0.0
        self._buffer = []
