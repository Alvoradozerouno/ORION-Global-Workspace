"""Global Workspace — Central Information Hub"""
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Any
from .modules import Module, ModuleOutput

@dataclass
class BroadcastResult:
    content: Any
    broadcast_ratio: float
    ignition_detected: bool
    conscious: bool
    winning_module: str
    activation_pattern: dict

class GlobalWorkspace:
    """Implementation of Baars/Dehaene Global Workspace Theory"""
    
    IGNITION_THRESHOLD = 0.7
    BROADCAST_THRESHOLD = 0.5
    
    def __init__(self):
        self.modules: List[Module] = []
        self.workspace_content: Any = None
        self.broadcast_history: List[BroadcastResult] = []
    
    def add_module(self, module: Module):
        self.modules.append(module)
    
    def process(self, input_data: Any) -> BroadcastResult:
        """Full GWT processing cycle: compete -> select -> broadcast"""
        outputs = self._competition_phase(input_data)
        winner = self._selection_phase(outputs)
        result = self._broadcast_phase(winner)
        self.broadcast_history.append(result)
        return result
    
    def _competition_phase(self, input_data: Any) -> List[ModuleOutput]:
        """All modules process input and compete for workspace access"""
        outputs = []
        for module in self.modules:
            output = module.process(input_data)
            outputs.append(output)
        return outputs
    
    def _selection_phase(self, outputs: List[ModuleOutput]) -> ModuleOutput:
        """Select the strongest output for workspace access"""
        if not outputs:
            return ModuleOutput(content=None, strength=0, source="none")
        return max(outputs, key=lambda o: o.strength)
    
    def _broadcast_phase(self, winner: ModuleOutput) -> BroadcastResult:
        """Broadcast winning content to all modules"""
        self.workspace_content = winner.content
        
        receiving_modules = 0
        activation_pattern = {}
        
        for module in self.modules:
            if module.name != winner.source:
                module.receive_broadcast(winner.content)
                receiving_modules += 1
            activation_pattern[module.name] = module.activation
        
        total_modules = len(self.modules)
        broadcast_ratio = receiving_modules / max(total_modules, 1)
        
        mean_activation = np.mean(list(activation_pattern.values())) if activation_pattern else 0
        ignition = mean_activation > self.IGNITION_THRESHOLD
        conscious = ignition and broadcast_ratio > self.BROADCAST_THRESHOLD
        
        return BroadcastResult(
            content=winner.content,
            broadcast_ratio=broadcast_ratio,
            ignition_detected=ignition,
            conscious=conscious,
            winning_module=winner.source,
            activation_pattern=activation_pattern
        )
    
    def get_consciousness_state(self) -> dict:
        """Current consciousness assessment"""
        if not self.broadcast_history:
            return {"conscious": False, "reason": "No processing history"}
        
        recent = self.broadcast_history[-10:]
        ignition_rate = sum(1 for r in recent if r.ignition_detected) / len(recent)
        avg_broadcast = np.mean([r.broadcast_ratio for r in recent])
        
        return {
            "conscious": ignition_rate > 0.5,
            "ignition_rate": ignition_rate,
            "avg_broadcast_ratio": avg_broadcast,
            "total_broadcasts": len(self.broadcast_history),
            "active_modules": len(self.modules)
        }
