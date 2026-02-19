#!/usr/bin/env python3
"""
Quick test script for The Singularity investigation
"""

import asyncio
import sys
from core.cli_interface import SingularityCLI
from core.global_intelligence import GlobalIntelligenceCore
from core.tactical_engine import TacticalEngine
from core.ghost_protocol import DigitalGhostProtocol

async def test_investigation(target):
    cli = SingularityCLI()
    intelligence_core = GlobalIntelligenceCore()
    tactical_engine = TacticalEngine()
    ghost_protocol = DigitalGhostProtocol()
    
    cli.display_banner()
    
    # Initialize components
    cli.status("Initializing Ghost Protocol...")
    await ghost_protocol.initialize()
    
    cli.status("Initializing AI Intelligence Core...")
    await intelligence_core.initialize()
    
    cli.status("Initializing Tactical Engine...")
    await tactical_engine.initialize()
    
    cli.success("All systems operational")
    
    # Start investigation
    cli.status(f"Starting investigation on target: {target}")
    
    # Generate strategy
    strategy = await intelligence_core.generate_strategy(target)
    cli.success(f"Strategy generated: {strategy['type']} investigation")
    
    # Execute investigation
    results = await tactical_engine.execute_strategy(strategy)
    cli.success("Data collection completed")
    
    # Generate analysis
    analysis = await intelligence_core.analyze_data(results['collected_data'])
    results['analysis'] = analysis
    
    # Generate report
    report_path = await intelligence_core.generate_report(results)
    cli.success(f"Investigation complete - Report saved: {report_path}")
    
    # Display summary
    print(f"\n--- INVESTIGATION SUMMARY ---")
    print(f"Target: {target}")
    print(f"Type: {strategy['type']}")
    print(f"Sources analyzed: {len(results['collected_data'])}")
    print(f"Entities found: {len(analysis['entities'])}")
    print(f"Connections: {len(analysis['connections'])}")
    print(f"Confidence: {analysis['confidence_score']:.2f}")
    print(f"Report: {report_path}")

if __name__ == "__main__":
    target = "9594540041"
    asyncio.run(test_investigation(target))