"""Public, minimal example of an evidence-only citation gate.

A toy demonstration of one boundary used in source-grounded AI systems.
Not production SADS source; syntactic citations do not prove semantic truth.
"""
from dataclasses import dataclass
import re

CITATION = re.compile(r"\[sads:question:mathematics:([A-Za-z0-9_-]+)\]")
CITATION_LOOKALIKE = re.compile(r"\[sads:[^\]]+\]")


@dataclass(frozen=True)
class Check:
    accepted: bool
    reason: str
    cited: tuple[str, ...] = ()


def check_grounded_answer(answer: str, allowed_question_ids: set[str]) -> Check:
    """Accept an answer only if its citations belong to supplied evidence.

    Empty answers, absent citations, malformed same-family references and
    non-retrieved references are rejected. This is a syntactic guard only.
    """
    if not answer or not answer.strip():
        return Check(False, "empty answer")

    matches = list(CITATION.finditer(answer))
    if not matches:
        return Check(False, "no valid citations")

    lookalikes = [m.group() for m in CITATION_LOOKALIKE.finditer(answer)]
    if len(lookalikes) != len(matches):
        return Check(False, "malformed or unsupported citation")

    ids = tuple(dict.fromkeys(m.group(1) for m in matches))
    if any(q not in allowed_question_ids for q in ids):
        return Check(False, "citation outside retrieved evidence")

    return Check(True, "citation IDs constrained to provided evidence", ids)


def choose_output(answer: str, evidence: dict[str, str]) -> dict[str, object]:
    """Generate either a limited AI answer or inspectable retrieved sources."""
    gate = check_grounded_answer(answer, set(evidence))
    if gate.accepted:
        return {"mode": "grounded_ai", "answer": answer, "citations": gate.cited}
    return {
        "mode": "retrieval_only",
        "reason": gate.reason,
        "sources": [{"id": k, "text": v} for k, v in evidence.items()],
    }
