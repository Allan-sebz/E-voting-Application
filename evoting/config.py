"""
Configuration constants for the E-Voting System.
Contains all magic numbers and constant values extracted from the monolith.
"""

# Age constraints
MIN_CANDIDATE_AGE = 25
MAX_CANDIDATE_AGE = 75
MIN_VOTER_AGE = 18

# Education levels required for candidates
REQUIRED_EDUCATION_LEVELS = [
    "Bachelor's Degree",
    "Master's Degree",
    "PhD",
    "Doctorate"
]

# Valid position levels
POSITION_LEVELS = ["national", "regional", "local"]

# Valid election types
ELECTION_TYPES = ["General", "Primary", "By-election", "Referendum"]

# Admin roles
import os

# Get the workspace directory (parent of evoting folder)
_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(_PACKAGE_DIR)

# Admin roles
ADMIN_ROLES = [
    "super_admin",
    "election_officer",
    "station_manager",
    "auditor"
]

# Gender options
VALID_GENDERS = ["M", "F", "OTHER"]

# Password constraints
MIN_PASSWORD_LENGTH = 6

# Data file path - stored in workspace root
DATA_FILE_PATH = os.path.join(WORKSPACE_DIR, "evoting_data.json")

# Voter card number length
VOTER_CARD_LENGTH = 12

# Position defaults
DEFAULT_POSITION_SEATS = 1
DEFAULT_TERM_LENGTH_YEARS = 5
