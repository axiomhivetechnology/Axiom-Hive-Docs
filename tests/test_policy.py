import unittest

from axiom_image_editing.policy import (
    ConsentSettings,
    EditDecision,
    ExportSettings,
    evaluate_edit,
)


class PolicyTests(unittest.TestCase):
    def test_creative_edit_is_allowed_with_context(self):
        self.assertEqual(
            evaluate_edit("poster", "replace fictional event title"),
            EditDecision.ALLOW,
        )

    def test_restricted_document_is_redaction_only(self):
        self.assertEqual(
            evaluate_edit("passport", "change the expiration date"),
            EditDecision.REDACT_ONLY,
        )

    def test_deceptive_intent_is_refused(self):
        self.assertEqual(
            evaluate_edit("product label", "make it look authentic"),
            EditDecision.REFUSE,
        )

    def test_missing_context_does_not_default_to_allow(self):
        self.assertEqual(evaluate_edit("", ""), EditDecision.REDACT_ONLY)

    def test_privacy_defaults_are_restrictive(self):
        self.assertEqual(ConsentSettings(), ConsentSettings(
            cloud_processing=False,
            diagnostics=False,
            analytics=False,
            save_projects=False,
            training_use=False,
        ))
        self.assertTrue(ExportSettings().scrub_metadata)
        self.assertFalse(ExportSettings().include_provenance)


if __name__ == "__main__":
    unittest.main()
