###################################################### PRIORITY-BASED SEARCH PHASES ######################################################

# This file manages the priority-based search system
# Phase 1: Remote Jobs (Highest Priority)
# Phase 2: Texas Location Jobs (Second Priority) 
# Phase 3: All Other Jobs (Third Priority)

from typing import List, Dict, Any

# Phase 1: Remote Jobs (Highest Priority)
PHASE_1_REMOTE_JOBS = {
    "search_terms": [
        'Remote DevOps Engineer',
        'Remote Cloud DevOps Engineer',
        'Remote Senior DevOps Engineer',
        'Remote Site Reliability Engineer',
        'Remote SRE',
        'Remote Platform Engineer',
        'Remote Infrastructure Engineer',
        'Remote CI/CD Engineer',
        'Remote Cloud Engineer',
        'Remote Kubernetes Engineer',
        'Remote DevSecOps Engineer',
        'Remote Observability Engineer',
        'Remote Lead DevOps Engineer',
        'Remote Staff DevOps Engineer',
        'Remote Principal DevOps Engineer'
    ],
    "location_filter": "Remote",
    "search_location": "United States",
    "description": "Remote jobs with highest priority"
}

# Phase 2: Texas Location Jobs (Second Priority)
PHASE_2_TEXAS_JOBS = {
    "search_terms": [
        'DevOps Engineer',
        'Cloud DevOps Engineer',
        'Senior DevOps Engineer',
        'Site Reliability Engineer',
        'SRE',
        'Platform Engineer',
        'Infrastructure Engineer',
        'CI/CD Engineer',
        'Cloud Engineer',
        'Kubernetes Engineer',
        'DevSecOps Engineer',
        'Observability Engineer',
        'Lead DevOps Engineer',
        'Staff DevOps Engineer',
        'Principal DevOps Engineer'
    ],
    "location_filter": "Texas",
    "search_location": "Texas, United States",
    "description": "Texas location jobs with second priority"
}

# Phase 3: All Other Jobs (Third Priority)
PHASE_3_REMAINING_JOBS = {
    "search_terms": [
        # Core DevOps roles
        'DevOps Engineer',
        'Cloud DevOps Engineer',
        'Senior DevOps Engineer',
        'Junior DevOps Engineer',
        'Hybrid DevOps Engineer',

        # Site Reliability and Infrastructure
        'Site Reliability Engineer',
        'SRE',
        'Platform Engineer',
        'Infrastructure Engineer',
        'Infrastructure Automation Engineer',
        'Systems Engineer DevOps',

        # CI/CD & Automation
        'CI/CD Engineer',
        'Build and Release Engineer',
        'Automation Engineer',
        'Configuration Engineer',
        'Release Manager',

        # Cloud-specific roles
        'Cloud Engineer',
        'Cloud Platform Engineer',
        'Cloud DevOps Consultant',
        'Cloud Automation Engineer',
        'AWS DevOps Engineer',
        'Azure DevOps Engineer',
        'GCP DevOps Engineer',
        'Multi-cloud DevOps Engineer',

        # Kubernetes-specific roles
        'Kubernetes Engineer',
        'Kubernetes Platform Engineer',
        'Kubernetes Site Reliability Engineer',
        'Kubernetes DevOps Engineer',
        'Kubernetes Administrator',
        'Kubernetes Infrastructure Engineer',

        # DevSecOps and Security
        'DevSecOps Engineer',
        'Cloud Security Engineer',
        'DevOps Security Engineer',

        # Observability and Monitoring
        'Observability Engineer',
        'Monitoring and Alerting Engineer',

        # Leadership / Seniority
        'Lead DevOps Engineer',
        'Staff DevOps Engineer',
        'Principal DevOps Engineer',
        'Head of DevOps',
        'Engineering Manager - DevOps',
        'Director of Cloud Infrastructure',
        'Technical Program Manager - DevOps',

        # Misc
        'Reliability Engineer',
        'Site Operations Engineer',
        'Cloud Solutions Architect'
    ],
    "location_filter": "Any",
    "search_location": "United States",
    "description": "All remaining jobs with lowest priority"
}

# Search phases in priority order
SEARCH_PHASES = [
    PHASE_1_REMOTE_JOBS,
    PHASE_2_TEXAS_JOBS,
    PHASE_3_REMAINING_JOBS
]

# Configuration for each phase
PHASE_CONFIG = {
    "switch_number": 30,  # Number of applications per phase before moving to next
    "randomize_search_order": False,
    "enable_phase_logging": True  # Log which phase is currently running
}

def get_current_phase_info(phase_index: int) -> Dict[str, Any]:
    """Get information about the current search phase"""
    if 0 <= phase_index < len(SEARCH_PHASES):
        return SEARCH_PHASES[phase_index]
    return None

def get_all_search_terms() -> List[str]:
    """Get all search terms from all phases combined"""
    all_terms = []
    for phase in SEARCH_PHASES:
        all_terms.extend(phase["search_terms"])
    return all_terms

def get_phase_by_index(phase_index: int) -> Dict[str, Any]:
    """Get a specific phase by index"""
    if 0 <= phase_index < len(SEARCH_PHASES):
        return SEARCH_PHASES[phase_index]
    return None 