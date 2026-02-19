#!/usr/bin/env python3
"""
The Singularity - Unified AI Intelligence Framework
Main Entry Point
"""

import sys
import time
import asyncio
from pathlib import Path
from core.cli_interface import SingularityCLI
from core.global_intelligence import GlobalIntelligenceCore
from core.tactical_engine import TacticalEngine
from core.ghost_protocol import DigitalGhostProtocol

class Singularity:
    def __init__(self):
        self.cli = SingularityCLI()
        self.intelligence_core = GlobalIntelligenceCore()
        self.tactical_engine = TacticalEngine()
        self.ghost_protocol = DigitalGhostProtocol()
        
    async def initialize(self):
        """Initialize all components"""
        self.cli.display_banner()
        await self.ghost_protocol.initialize()
        await self.intelligence_core.initialize()
        await self.tactical_engine.initialize()
        
    async def run_investigation(self, target_input):
        """Execute autonomous investigation"""
        strategy = await self.intelligence_core.generate_strategy(target_input)
        results = await self.tactical_engine.execute_strategy(strategy)
        report = await self.intelligence_core.generate_report(results)
        return report
        
    async def main_loop(self):
        """Main interactive loop"""
        await self.initialize()
        
        while True:
            try:
                command = self.cli.get_input()
                
                if command.lower() in ['exit', 'quit']:
                    break
                elif command.startswith('investigate '):
                    target = command[12:]
                    self.cli.status("Starting autonomous investigation...")
                    report = await self.run_investigation(target)
                    self.cli.success(f"Investigation complete. Report: {report}")
                else:
                    self.cli.error("Unknown command. Use 'investigate <target>' or 'exit'")
                    
            except KeyboardInterrupt:
                self.cli.warning("Operation interrupted")
                break
            except Exception as e:
                self.cli.error(f"Error: {e}")

if __name__ == "__main__":
    singularity = Singularity()
    asyncio.run(singularity.main_loop())