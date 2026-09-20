import json
import tempfile
import unittest
from pathlib import Path

from executor.queue import load_request


class QueueTests(unittest.TestCase):
    def write_request(self, root, name, payload):
        path = Path(root) / f"{name}.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def base_request(self, request_id="auto-001"):
        return {
            "schema": "arca.public-executor-request.v0.1",
            "profile": "smoke",
            "request_id": request_id,
            "public_only": True,
            "secrets_allowed": False,
        }

    def test_valid_queue_request(self):
        with tempfile.TemporaryDirectory() as root:
            request, metadata = load_request(
                self.write_request(root, "auto-001", self.base_request())
            )
            self.assertEqual(request.request_id, "auto-001")
            self.assertEqual(metadata["source"], "git-queue")

    def test_filename_must_match_request_id(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                load_request(
                    self.write_request(root, "different", self.base_request())
                )

    def test_secrets_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            payload = self.base_request()
            payload["secrets_allowed"] = True
            with self.assertRaises(ValueError):
                load_request(self.write_request(root, "auto-001", payload))

    def test_non_public_job_is_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            payload = self.base_request()
            payload["public_only"] = False
            with self.assertRaises(ValueError):
                load_request(self.write_request(root, "auto-001", payload))

    def test_extra_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            payload = self.base_request()
            payload["shell"] = "caller-controlled"
            with self.assertRaises(ValueError):
                load_request(self.write_request(root, "auto-001", payload))


if __name__ == "__main__":
    unittest.main()
