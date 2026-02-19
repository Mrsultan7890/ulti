"""
Global Intelligence Core - AI Brain of The Singularity
"""

import json
import hashlib
import asyncio
from datetime import datetime
from pathlib import Path

class GlobalIntelligenceCore:
    def __init__(self):
        self.knowledge_base = {}
        self.investigation_history = []
        self.ai_model = None
        
    async def initialize(self):
        """Initialize AI models and knowledge base"""
        self._load_knowledge_base()
        await self._initialize_ai_model()
        
    def _load_knowledge_base(self):
        """Load existing knowledge base"""
        kb_path = Path("data/knowledge_base.json")
        if kb_path.exists():
            with open(kb_path, 'r') as f:
                self.knowledge_base = json.load(f)
                
    async def _initialize_ai_model(self):
        """Initialize lightweight AI model for pattern recognition"""
        # Simplified AI model for autonomous operation
        self.ai_model = {
            'patterns': {},
            'strategies': {
                'social_media': ['username_search', 'profile_analysis', 'connection_mapping'],
                'email': ['domain_analysis', 'breach_check', 'pattern_matching'],
                'phone': ['carrier_lookup', 'location_analysis', 'social_correlation'],
                'name': ['social_search', 'public_records', 'cross_reference']
            }
        }
        
    async def generate_strategy(self, target_input):
        """Generate investigation strategy based on input type and AI analysis"""
        strategy = {
            'target': target_input,
            'timestamp': datetime.now().isoformat(),
            'phases': [],
            'priority_sources': [],
            'stealth_level': 'maximum'
        }
        
        # Determine input type and generate appropriate strategy
        if '@' in target_input:
            strategy['type'] = 'email'
            strategy['phases'] = self.ai_model['strategies']['email']
        elif target_input.isdigit():
            strategy['type'] = 'phone'
            strategy['phases'] = self.ai_model['strategies']['phone']
        elif ' ' in target_input:
            strategy['type'] = 'name'
            strategy['phases'] = self.ai_model['strategies']['name']
        else:
            strategy['type'] = 'username'
            strategy['phases'] = self.ai_model['strategies']['social_media']
            
        # AI-driven priority source selection
        strategy['priority_sources'] = self._select_priority_sources(strategy['type'])
        
        return strategy
        
    def _select_priority_sources(self, target_type):
        """AI selects optimal data sources based on target type"""
        source_map = {
            'email': ['haveibeenpwned', 'social_platforms', 'public_records'],
            'phone': ['carrier_db', 'social_platforms', 'reverse_lookup'],
            'name': ['social_platforms', 'public_records', 'news_sources'],
            'username': ['social_platforms', 'forums', 'gaming_platforms']
        }
        return source_map.get(target_type, ['social_platforms'])
        
    async def analyze_data(self, collected_data):
        """AI analysis of collected data for pattern recognition"""
        analysis = {
            'entities': [],
            'connections': [],
            'behavioral_patterns': [],
            'risk_indicators': [],
            'confidence_score': 0.0
        }
        
        # Entity extraction
        for source, data in collected_data.items():
            entities = self._extract_entities(data)
            analysis['entities'].extend(entities)
            
        # Connection analysis
        analysis['connections'] = self._find_connections(analysis['entities'])
        
        # Behavioral analysis
        analysis['behavioral_patterns'] = self._analyze_behavior(collected_data)
        
        # Risk assessment
        analysis['risk_indicators'] = self._assess_risk(analysis)
        analysis['confidence_score'] = self._calculate_confidence(analysis)
        
        return analysis
        
    def _extract_entities(self, data):
        """Extract key entities from data"""
        entities = []
        # Simplified entity extraction
        if isinstance(data, dict):
            for key, value in data.items():
                if key in ['username', 'email', 'phone', 'location', 'name']:
                    entities.append({'type': key, 'value': value})
        return entities
        
    def _find_connections(self, entities):
        """Find connections between entities"""
        connections = []
        for i, entity1 in enumerate(entities):
            for entity2 in entities[i+1:]:
                similarity = self._calculate_similarity(entity1, entity2)
                if similarity > 0.7:
                    connections.append({
                        'entity1': entity1,
                        'entity2': entity2,
                        'similarity': similarity
                    })
        return connections
        
    def _calculate_similarity(self, entity1, entity2):
        """Calculate similarity between entities"""
        # Simplified similarity calculation
        if entity1['type'] == entity2['type']:
            return 0.8 if entity1['value'] == entity2['value'] else 0.3
        return 0.1
        
    def _analyze_behavior(self, data):
        """Analyze behavioral patterns"""
        patterns = []
        # Simplified behavioral analysis
        for source, content in data.items():
            if 'posts' in str(content).lower():
                patterns.append({'type': 'social_activity', 'frequency': 'high'})
        return patterns
        
    def _assess_risk(self, analysis):
        """Assess risk indicators"""
        indicators = []
        if len(analysis['connections']) > 5:
            indicators.append({'type': 'high_connectivity', 'severity': 'medium'})
        return indicators
        
    def _calculate_confidence(self, analysis):
        """Calculate overall confidence score"""
        base_score = 0.5
        base_score += len(analysis['entities']) * 0.1
        base_score += len(analysis['connections']) * 0.05
        return min(base_score, 1.0)
        
    async def generate_report(self, investigation_results):
        """Generate comprehensive investigation report"""
        report_id = hashlib.sha256(str(datetime.now()).encode()).hexdigest()[:8]
        report_path = f"reports/investigation_{report_id}.json"
        
        report = {
            'report_id': report_id,
            'timestamp': datetime.now().isoformat(),
            'target': investigation_results.get('target', 'Unknown'),
            'summary': self._generate_summary(investigation_results),
            'findings': investigation_results.get('analysis', {}),
            'timeline': investigation_results.get('timeline', []),
            'chain_of_custody': self._generate_custody_chain(investigation_results),
            'recommendations': self._generate_recommendations(investigation_results)
        }
        
        # Save report
        Path("reports").mkdir(exist_ok=True)
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
            
        return report_path
        
    def _generate_summary(self, results):
        """Generate executive summary"""
        return {
            'total_sources': len(results.get('collected_data', {})),
            'entities_found': len(results.get('analysis', {}).get('entities', [])),
            'connections_mapped': len(results.get('analysis', {}).get('connections', [])),
            'confidence_level': results.get('analysis', {}).get('confidence_score', 0.0)
        }
        
    def _generate_custody_chain(self, results):
        """Generate chain of custody for legal admissibility"""
        chain = []
        for source, data in results.get('collected_data', {}).items():
            chain.append({
                'source': source,
                'timestamp': datetime.now().isoformat(),
                'hash': hashlib.sha256(str(data).encode()).hexdigest(),
                'method': 'automated_collection'
            })
        return chain
        
    def _generate_recommendations(self, results):
        """Generate actionable recommendations"""
        recommendations = []
        confidence = results.get('analysis', {}).get('confidence_score', 0.0)
        
        if confidence > 0.8:
            recommendations.append("High confidence findings - recommend further investigation")
        elif confidence > 0.5:
            recommendations.append("Moderate confidence - additional verification needed")
        else:
            recommendations.append("Low confidence - expand search parameters")
            
        return recommendations