import unittest

from citation_guard import check_grounded_answer, choose_output


class CitationGateTests(unittest.TestCase):
    def test_accepts_only_supplied_ids(self):
        r = check_grounded_answer(
            "Solution [sads:question:mathematics:q001]",
            {"q001", "q002"},
        )
        self.assertTrue(r.accepted)
        self.assertEqual(r.cited, ("q001",))

    def test_missing_citation_fails_closed(self):
        self.assertFalse(check_grounded_answer("The solution is 42", {"q001"}).accepted)

    def test_unretrieved_citation_fails_closed(self):
        r = check_grounded_answer(
            "Claim [sads:question:mathematics:made-up]", {"q001"}
        )
        self.assertEqual(r.reason, "citation outside retrieved evidence")

    def test_malformed_citation_rejected(self):
        r = check_grounded_answer(
            "Claim [sads:question:chemistry:q001]", {"q001"}
        )
        self.assertFalse(r.accepted)

    def test_rejects_partial_validity(self):
        r = check_grounded_answer(
            "A [sads:question:mathematics:q001], B [sads:question:mathematics:wrong]",
            {"q001"},
        )
        self.assertFalse(r.accepted)

    def test_repeats_deduplicated(self):
        r = check_grounded_answer(
            "[sads:question:mathematics:q001] [sads:question:mathematics:q001]",
            {"q001"},
        )
        self.assertTrue(r.accepted)
        self.assertEqual(r.cited, ("q001",))

    def test_retrieval_only_fallback(self):
        r = choose_output("No reliable source", {"q001": "original excerpt"})
        self.assertEqual(r["mode"], "retrieval_only")
        self.assertEqual(r["sources"][0]["id"], "q001")


if __name__ == "__main__":
    unittest.main()
