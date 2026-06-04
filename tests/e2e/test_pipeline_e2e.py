"""
Testes E2E para App Factory Pipeline
Validam a maquina de estados e transicoes completas.
"""

import pytest
from src.pipeline.state_machine import PipelineStateMachine, State, Checkpoint


class TestPipelineE2E:
    """Testes ponta a ponta do pipeline."""

    def test_full_pipeline_happy_path(self):
        """E2E: Pipeline completo do idle -> completed"""
        sm = PipelineStateMachine()

        # Sequencia completa de estados
        states = [
            (State.INTAKE, None),
            (State.DISCOVERY, Checkpoint.CP0),
            (State.PRD, Checkpoint.CP1),
            (State.BLUEPRINT, Checkpoint.CP2),
            (State.STACK, Checkpoint.CP4),
            (State.SCHEMA, Checkpoint.CP3),
            (State.API, Checkpoint.CP5),
            (State.FRONTEND, Checkpoint.CP6),
            (State.TEST, Checkpoint.CP7),
            (State.SCAFFOLD, Checkpoint.CP9),
            (State.SECURITY, Checkpoint.CP8),
            (State.DEPLOY, Checkpoint.CP11),
            (State.HANDOFF, Checkpoint.CP13),
            (State.AKASHA, Checkpoint.CP14),
            (State.KRATOS, Checkpoint.CP15),
            (State.COMPLETED, None),
        ]

        for target, cp in states:
            if cp:
                sm.pass_checkpoint(cp)
            result = sm.transition(target)
            assert result["success"], f"Falhou em {target.value}: {result.get('error')}"

        assert sm.is_terminal()
        assert sm.state == State.COMPLETED

    def test_discovery_blocked_without_cp0(self):
        """E2E: Discovery bloqueado sem CP0"""
        sm = PipelineStateMachine()
        sm.state = State.INTAKE

        result = sm.transition(State.DISCOVERY)
        assert not result["success"]
        assert "cp0" in result["required_checkpoint"]

    def test_prd_blocked_without_discovery(self):
        """E2E: PRD bloqueado sem discovery validado"""
        sm = PipelineStateMachine()
        sm.state = State.INTAKE
        sm.pass_checkpoint(Checkpoint.CP0)
        sm.transition(State.DISCOVERY)

        result = sm.transition(State.PRD)
        assert not result["success"]
        assert result["required_checkpoint"] == "cp1"

    def test_invalid_transition(self):
        """E2E: Transicao invalida rejeitada"""
        sm = PipelineStateMachine()
        result = sm.transition(State.COMPLETED)
        assert not result["success"]

    def test_next_states_from_idle(self):
        """E2E: Apenas intake alcancavel do idle"""
        sm = PipelineStateMachine()
        next_states = sm.get_next_states()
        assert len(next_states) == 1
        assert next_states[0] == State.INTAKE

    def test_checkpoint_persistence(self):
        """E2E: Checkpoints persistem entre transicoes"""
        sm = PipelineStateMachine()
        sm.pass_checkpoint(Checkpoint.CP0)
        sm.pass_checkpoint(Checkpoint.CP1)

        assert sm.checkpoints[Checkpoint.CP0] is True
        assert sm.checkpoints[Checkpoint.CP1] is True
        assert sm.checkpoints[Checkpoint.CP2] is False

    def test_state_dict_output(self):
        """E2E: Output da maquina em dict"""
        sm = PipelineStateMachine()
        sm.pass_checkpoint(Checkpoint.CP0)
        sm.transition(State.INTAKE)
        sm.transition(State.DISCOVERY)

        data = sm.to_dict()
        assert data["state"] == "discovery"
        assert len(data["history"]) == 2
        assert data["checkpoints"]["cp0"] is True
        assert data["is_terminal"] is False

    def test_skill_mapping(self):
        """E2E: Cada estado tem skill e squad"""
        sm = PipelineStateMachine()
        sm.state = State.PRD
        assert sm._get_skill_for_state(State.PRD) == "prd-generator"
        assert sm._get_squad_for_state(State.PRD) == "product"

    def test_security_gate_requires_build(self):
        """E2E: Security requer build passando (CP8)"""
        sm = PipelineStateMachine()
        sm.state = State.SCAFFOLD
        result = sm.transition(State.SECURITY)
        assert not result["success"]
        assert result["required_checkpoint"] == "cp8"

    def test_deploy_requires_gates(self):
        """E2E: Deploy requer gates passando (CP11)"""
        sm = PipelineStateMachine()
        sm.state = State.SECURITY
        result = sm.transition(State.DEPLOY)
        assert not result["success"]
        assert result["required_checkpoint"] == "cp11"

    def test_memory_squad_finalizes(self):
        """E2E: Memory squad persiste e finaliza"""
        sm = PipelineStateMachine()
        sm.state = State.HANDOFF
        sm.pass_checkpoint(Checkpoint.CP14)
        sm.transition(State.AKASHA)
        sm.pass_checkpoint(Checkpoint.CP15)
        sm.transition(State.KRATOS)
        sm.transition(State.COMPLETED)

        assert sm.state == State.COMPLETED
        assert sm.is_terminal()

    def test_no_skipping_states(self):
        """E2E: Nao pula estados no pipeline"""
        sm = PipelineStateMachine()
        sm.state = State.INTAKE
        sm.pass_checkpoint(Checkpoint.CP0)
        sm.pass_checkpoint(Checkpoint.CP1)

        # Tentar pular discovery -> prd direto (precisa estar em discovery primeiro)
        result = sm.transition(State.PRD)
        assert not result["success"]
