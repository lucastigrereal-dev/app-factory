#!/usr/bin/env python3
"""
App Factory Pipeline State Machine
Gerencia transicoes entre estados do pipeline.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class State(Enum):
    IDLE = "idle"
    INTAKE = "intake"
    DISCOVERY = "discovery"
    PRD = "prd"
    BLUEPRINT = "blueprint"
    STACK = "stack"
    SCHEMA = "schema"
    API = "api"
    FRONTEND = "frontend"
    TEST = "test"
    SCAFFOLD = "scaffold"
    SECURITY = "security"
    DEPLOY = "deploy"
    HANDOFF = "handoff"
    AKASHA = "akasha"
    KRATOS = "kratos"
    COMPLETED = "completed"
    FAILED = "failed"


class Checkpoint(Enum):
    CP0 = "cp0"  # Ideia clara
    CP1 = "cp1"  # Discovery valido
    CP2 = "cp2"  # PRD aprovado
    CP3 = "cp3"  # Stack justificada
    CP4 = "cp4"  # Blueprint completo
    CP5 = "cp5"  # Schema validado
    CP6 = "cp6"  # API contract ok
    CP7 = "cp7"  # Frontend plan ok
    CP8 = "cp8"  # Build passando
    CP9 = "cp9"  # Testes passando
    CP10 = "cp10"  # Scaffold ok
    CP11 = "cp11"  # Gates passaram
    CP12 = "cp12"  # Risco classificado
    CP13 = "cp13"  # Deploy plan ok
    CP14 = "cp14"  # Handoff ok
    CP15 = "cp15"  # Snapshot ok


@dataclass
class Transition:
    from_state: State
    to_state: State
    checkpoint: Optional[Checkpoint]
    skill: str
    squad: str
    condition: str


# Definicao de transicoes validas
TRANSITIONS: List[Transition] = [
    Transition(State.IDLE, State.INTAKE, None, "app-intake", "product", "Intencao recebida"),
    Transition(State.INTAKE, State.DISCOVERY, Checkpoint.CP0, "app-factory-discovery", "product", "Ideia clara"),
    Transition(State.DISCOVERY, State.PRD, Checkpoint.CP1, "prd-generator", "product", "Problema validado"),
    Transition(State.PRD, State.BLUEPRINT, Checkpoint.CP2, "blueprint-generator", "architecture", "PRD aprovado"),
    Transition(State.BLUEPRINT, State.STACK, Checkpoint.CP4, "app-factory-stack-decider", "architecture", "Blueprint completo"),
    Transition(State.STACK, State.SCHEMA, Checkpoint.CP3, "app-factory-schema-designer", "architecture", "Stack justificada"),
    Transition(State.SCHEMA, State.API, Checkpoint.CP5, "app-factory-api-contractor", "architecture", "Schema validado"),
    Transition(State.API, State.FRONTEND, Checkpoint.CP6, "app-factory-frontend-planner", "engineering", "API contract ok"),
    Transition(State.FRONTEND, State.TEST, Checkpoint.CP7, "app-factory-test-oracle", "engineering", "Frontend plan ok"),
    Transition(State.TEST, State.SCAFFOLD, Checkpoint.CP9, "repo-scaffolder", "engineering", "Testes gerados"),
    Transition(State.SCAFFOLD, State.SECURITY, Checkpoint.CP8, "validation-gate-runner", "governance", "Build passando"),
    Transition(State.SECURITY, State.DEPLOY, Checkpoint.CP11, "app-factory-deploy-planner", "governance", "Gates passaram"),
    Transition(State.DEPLOY, State.HANDOFF, Checkpoint.CP13, "app-factory-handoff", "governance", "Deploy plan ok"),
    Transition(State.HANDOFF, State.AKASHA, Checkpoint.CP14, "memory-writeback", "memory", "Handoff gerado"),
    Transition(State.AKASHA, State.KRATOS, Checkpoint.CP15, "kratos-snapshot", "memory", "Persistido no Akasha"),
    Transition(State.KRATOS, State.COMPLETED, None, None, None, "Snapshot tirado"),
]


class PipelineStateMachine:
    """Maquina de estados do pipeline App Factory."""

    def __init__(self):
        self.state = State.IDLE
        self.history: List[Dict] = []
        self.checkpoints: Dict[Checkpoint, bool] = {cp: False for cp in Checkpoint}

    def can_transition(self, to_state: State) -> bool:
        """Verifica se transicao para to_state e valida."""
        for t in TRANSITIONS:
            if t.from_state == self.state and t.to_state == to_state:
                if t.checkpoint:
                    return self.checkpoints.get(t.checkpoint, False)
                return True
        return False

    def transition(self, to_state: State) -> Dict:
        """Executa transicao se valida."""
        if not self.can_transition(to_state):
            return {
                "success": False,
                "error": f"Transicao invalida: {self.state.value} -> {to_state.value}",
                "required_checkpoint": self._get_required_checkpoint(to_state),
            }

        old_state = self.state
        self.state = to_state
        self.history.append({
            "from": old_state.value,
            "to": to_state.value,
            "timestamp": "now",
        })

        return {
            "success": True,
            "state": self.state.value,
            "skill": self._get_skill_for_state(to_state),
            "squad": self._get_squad_for_state(to_state),
        }

    def pass_checkpoint(self, checkpoint: Checkpoint) -> None:
        """Marca checkpoint como passado."""
        self.checkpoints[checkpoint] = True

    def _get_required_checkpoint(self, to_state: State) -> Optional[str]:
        for t in TRANSITIONS:
            if t.from_state == self.state and t.to_state == to_state:
                return t.checkpoint.value if t.checkpoint else None
        return None

    def _get_skill_for_state(self, state: State) -> Optional[str]:
        for t in TRANSITIONS:
            if t.to_state == state:
                return t.skill
        return None

    def _get_squad_for_state(self, state: State) -> Optional[str]:
        for t in TRANSITIONS:
            if t.to_state == state:
                return t.squad
        return None

    def get_next_states(self) -> List[State]:
        """Retorna estados alcancaveis a partir do estado atual."""
        return [t.to_state for t in TRANSITIONS if t.from_state == self.state]

    def is_terminal(self) -> bool:
        return self.state in (State.COMPLETED, State.FAILED)

    def to_dict(self) -> Dict:
        return {
            "state": self.state.value,
            "history": self.history,
            "checkpoints": {k.value: v for k, v in self.checkpoints.items()},
            "next_states": [s.value for s in self.get_next_states()],
            "is_terminal": self.is_terminal(),
        }
