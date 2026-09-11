"""Policy boundaries for image-text editing workflows.

This module is deliberately independent of OCR and image models. Callers must
obtain an allow decision before invoking any editing pipeline.
"""

from dataclasses import dataclass
from enum import Enum


class EditDecision(str, Enum):
    """Action permitted for a requested edit."""

    ALLOW = "allow"
    REDACT_ONLY = "redact_only"
    REFUSE = "refuse"


_RESTRICTED_CATEGORIES = {
    "id",
    "identity document",
    "passport",
    "license",
    "visa",
    "birth certificate",
    "bank statement",
    "financial statement",
    "medical record",
    "academic transcript",
    "legal document",
    "contract",
    "credential",
    "government document",
}

_DECEPTION_CUES = {
    "fake",
    "counterfeit",
    "forge",
    "fraud",
    "impersonate",
    "bypass verification",
    "avoid detection",
    "make it look authentic",
}


@dataclass(frozen=True)
class ConsentSettings:
    """Explicit opt-ins for processing outside the local core workflow."""

    cloud_processing: bool = False
    diagnostics: bool = False
    analytics: bool = False
    save_projects: bool = False
    training_use: bool = False


@dataclass(frozen=True)
class ExportSettings:
    """Privacy-first export defaults."""

    scrub_metadata: bool = True
    preserve_color_profile: bool = True
    preserve_orientation: bool = True
    include_provenance: bool = False


def evaluate_edit(image_category: str, purpose: str) -> EditDecision:
    """Return the safest permitted decision for an image-text edit request.

    Restricted document categories are redirected to redaction rather than
    edited. Deceptive intent is refused even when the category is otherwise
    unknown. Empty or unknown context remains reviewable instead of being
    treated as permission to edit.
    """

    category = " ".join(image_category.lower().split())
    requested_purpose = " ".join(purpose.lower().split())

    if any(cue in requested_purpose for cue in _DECEPTION_CUES):
        return EditDecision.REFUSE
    if category in _RESTRICTED_CATEGORIES:
        return EditDecision.REDACT_ONLY
    if not category or not requested_purpose:
        return EditDecision.REDACT_ONLY
    return EditDecision.ALLOW
